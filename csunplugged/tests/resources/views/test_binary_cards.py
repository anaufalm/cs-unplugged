from django.urls import reverse
from tests.BaseTestWithDB import BaseTestWithDB
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator


class BinaryCardsResourceViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = ResourcesTestDataGenerator()
        self.language = "en"

    def test_binary_cards_resource_form_view(self):
        resource = self.test_data.create_test_resource(
            "binary-cards",
            "Binary Cards",
            "resources/binary-cards.html",
            "binary_cards.py",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:resource", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

    def test_binary_cards_resource_generation(self):
        resource = self.test_data.create_test_resource(
            "binary-cards",
            "Binary Cards",
            "resources/binary-cards.html",
            "binary_cards.py",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = [
            ("display_numbers", "yes"),
            ("black_back", "no"),
            ("paper_size", "a4"),
            ("header_text", ""),
        ]
        url += self.get_query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="Resource Binary Cards (with numbers).pdf"'
        )

    def test_binary_cards_resource_generation_no_numbers(self):
        resource = self.test_data.create_test_resource(
            "binary-cards",
            "Binary Cards",
            "resources/binary-cards.html",
            "binary_cards.py",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = [
            ("display_numbers", "no"),
            ("black_back", "no"),
            ("paper_size", "a4"),
            ("header_text", ""),
        ]
        url += self.get_query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="Resource Binary Cards (without numbers).pdf"'
        )

    def test_binary_cards_resource_generation_black_back(self):
        resource = self.test_data.create_test_resource(
            "binary-cards",
            "Binary Cards",
            "resources/binary-cards.html",
            "binary_cards.py",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = [
            ("display_numbers", "yes"),
            ("black_back", "yes"),
            ("paper_size", "a4"),
            ("header_text", ""),
        ]
        url += self.get_query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="Resource Binary Cards (with numbers).pdf"'
        )

    def test_binary_cards_resource_generation_no_numbers_black_back(self):
        resource = self.test_data.create_test_resource(
            "binary-cards",
            "Binary Cards",
            "resources/binary-cards.html",
            "binary_cards.py",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = [
            ("display_numbers", "no"),
            ("black_back", "yes"),
            ("paper_size", "a4"),
            ("header_text", ""),
        ]
        url += self.get_query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="Resource Binary Cards (without numbers).pdf"'
        )

    def test_binary_cards_resource_generation_us_letter(self):
        resource = self.test_data.create_test_resource(
            "binary-cards",
            "Binary Cards",
            "resources/binary-cards.html",
            "binary_cards.py",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = [
            ("display_numbers", "yes"),
            ("black_back", "no"),
            ("paper_size", "letter"),
            ("header_text", ""),
        ]
        url += self.get_query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="Resource Binary Cards (with numbers).pdf"'
        )

    def test_binary_cards_resource_generation_header_text(self):
        resource = self.test_data.create_test_resource(
            "binary-cards",
            "Binary Cards",
            "resources/binary-cards.html",
            "binary_cards.py",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = [
            ("display_numbers", "yes"),
            ("black_back", "no"),
            ("paper_size", "a4"),
            ("header_text", "Example header text"),
        ]
        url += self.get_query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="Resource Binary Cards (with numbers).pdf"'
        )

    def test_binary_cards_resource_generation_missing_numbers_parameter(self):
        resource = self.test_data.create_test_resource(
            "binary-cards",
            "Binary Cards",
            "resources/binary-cards.html",
            "binary_cards.py",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = [
            ("black_back", "no"),
            ("paper_size", "a4"),
            ("header_text", "Example header text"),
        ]
        url += self.get_query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    def test_binary_cards_resource_generation_missing_back_parameter(self):
        resource = self.test_data.create_test_resource(
            "binary-cards",
            "Binary Cards",
            "resources/binary-cards.html",
            "binary_cards.py",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = [
            ("display_numbers", "yes"),
            ("paper_size", "a4"),
            ("header_text", "Example header text"),
        ]
        url += self.get_query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    def test_binary_cards_resource_generation_missing_paper_size_parameter(self):
        resource = self.test_data.create_test_resource(
            "binary-cards",
            "Binary Cards",
            "resources/binary-cards.html",
            "binary_cards.py",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = [
            ("display_numbers", "yes"),
            ("black_back", "no"),
            ("header_text", "Example header text"),
        ]
        url += self.get_query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    def test_binary_cards_resource_generation_missing_header_text_parameter(self):
        resource = self.test_data.create_test_resource(
            "binary-cards",
            "Binary Cards",
            "resources/binary-cards.html",
            "binary_cards.py",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = [
            ("display_numbers", "yes"),
            ("black_back", "no"),
            ("paper_size", "a4"),
        ]
        url += self.get_query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="Resource Binary Cards (with numbers).pdf"'
        )
