"""Process image pages in resource data."""

from PIL import Image
from io import BytesIO
import base64

MM_TO_PIXEL_RATIO = 6


def resize_encode_resource_images(paper_size, data):
    """Process image pages in resource.

    - Resizes images to required paper size.
    - Encodes images in base64 for PDF rendering.

    Args:
        paper_size: Paper size of requested resource (str).
        data: List of generated resource (list).

    Returns:
        List of processed resource pages.
    """
    if paper_size == "a4":
        max_pixel_height = 267 * MM_TO_PIXEL_RATIO
    elif paper_size == "letter":
        max_pixel_height = 249 * MM_TO_PIXEL_RATIO
    else:
        raise ValueError("Invalid paper size given.")

    # Resize images to reduce file size
    for index in range(len(data)):
        if data[index]["type"] == "image":
            image = data[index]["data"]
            (width, height) = image.size
            if height > max_pixel_height:
                ratio = max_pixel_height / height
                width *= ratio
                height *= ratio
                image = image.resize((int(width), int(height)), Image.ANTIALIAS)
            # Convert from Image object to base64 string
            image_buffer = BytesIO()
            image.save(image_buffer, format="PNG")
            data[index]["data"] = base64.b64encode(image_buffer.getvalue())
    return data
