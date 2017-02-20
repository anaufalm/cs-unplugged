from django.shortcuts import get_object_or_404, get_list_or_404
from django.views import generic

from .models import Topic, FollowUpActivity, UnitPlan, Lesson, ProgrammingExercise

class IndexView(generic.ListView):
    template_name = 'topics/index.html'
    context_object_name = 'all_topics'

    def get_queryset(self):
        """Return all topics"""
        return Topic.objects.order_by('name')


class TopicView(generic.DetailView):
    model = Topic
    template_name = 'topics/topic.html'
    slug_url_kwarg = 'topic_slug'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TopicView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the connected unit plans
        context['unit_plans'] = UnitPlan.objects.filter(topic=self.object).order_by('name')
        # Add in a QuerySet of all the connected programming exercises
        context['programming_exercises'] = ProgrammingExercise.objects.filter(topic=self.object).order_by('exercise_number')
        # Add in a QuerySet of all the connected follow up activities
        context['follow_up_activities'] = FollowUpActivity.objects.filter(topic=self.object).order_by('name')
        return context


class UnitPlanView(generic.DetailView):
    model = UnitPlan
    template_name = 'topics/unit_plan.html'
    context_object_name = 'unit_plan'

    def get_object(self, **kwargs):
        return get_object_or_404(
            self.model,
            topic__slug=self.kwargs.get('topic_slug', None),
            slug=self.kwargs.get('unit_plan_slug', None)
        )

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(UnitPlanView, self).get_context_data(**kwargs)
        # Add connected topic
        context['topic'] = get_object_or_404(Topic, slug=self.kwargs.get('topic_slug', None))
        # Add all the connected lessons
        context['lessons'] = self.object.unit_plan_lessons.order_by('age_bracket', 'number')
        return context


class LessonView(generic.DetailView):
    model = Lesson
    template_name = 'topics/lesson.html'
    context_object_name = 'lesson'

    def get_object(self, **kwargs):
        return get_object_or_404(
            self.model,
            topic__slug=self.kwargs.get('topic_slug', None),
            unit_plan__slug=self.kwargs.get('unit_plan_slug', None),
            age_bracket_slug=self.kwargs.get('age_bracket', None),
            slug=self.kwargs.get('lesson_slug', None),
        )

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(LessonView, self).get_context_data(**kwargs)
        # Add all the connected curriculum links
        context['lesson_curriculum_links'] = self.object.curriculum_links.all()
        # Add all the connected learning outcomes
        context['lesson_learning_outcomes'] = self.object.learning_outcomes.all()
        return context


class ProgrammingExerciseList(generic.ListView):
    model = ProgrammingExercise
    template_name = 'topics/programming_exercise_list.html'
    context_object_name = 'all_programming_exercises'

    def get_queryset(self, **kwargs):
        """Return all activities for topic"""
        # TODO: Is this the best way to raise 404 if invalid topic?
        topic = get_object_or_404(Topic, slug=self.kwargs.get('topic_slug', None))
        return ProgrammingExercise.objects.filter(topic__slug=self.kwargs.get('topic_slug', None)).order_by('exercise_number')

    def get_context_data(self, **kwargs):
        context = super(ProgrammingExerciseList, self).get_context_data(**kwargs)
        context['topic'] = get_object_or_404(Topic, slug=self.kwargs.get('topic_slug', None))
        return context


class ProgrammingExerciseView(generic.DetailView):
    model = ProgrammingExercise
    template_name = 'topics/programming_exercise.html'
    context_object_name = 'programming_exercise'

    def get_object(self, **kwargs):
        return get_object_or_404(
            self.model,
            topic__slug=self.kwargs.get('topic_slug', None),
            slug=self.kwargs.get('programming_exercise_slug', None)
        )

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProgrammingExerciseView, self).get_context_data(**kwargs)
        # Add all the connected learning outcomes
        context['programming_exercise_learning_outcomes'] = self.object.learning_outcomes.all()
        return context


class ActivityList(generic.ListView):
    model = FollowUpActivity
    template_name = 'topics/activity_list.html'
    context_object_name = 'all_follow_up_activities'

    def get_queryset(self, **kwargs):
        """Return all activities for topic"""
        # TODO: Is this the best way to raise 404 if invalid topic?
        topic = get_object_or_404(Topic, slug=self.kwargs.get('topic_slug', None))
        return FollowUpActivity.objects.filter(topic__slug=self.kwargs.get('topic_slug', None)).order_by('name')

    def get_context_data(self, **kwargs):
        context = super(ActivityList, self).get_context_data(**kwargs)
        context['topic'] = get_object_or_404(Topic, slug=self.kwargs.get('topic_slug', None))
        return context


class ActivityView(generic.DetailView):
    model = FollowUpActivity
    queryset = FollowUpActivity.objects.all()
    template_name = 'topics/activity.html'
    context_object_name = 'activity'

    def get_object(self, **kwargs):
        return get_object_or_404(
            self.model,
            topic__slug=self.kwargs.get('topic_slug', None),
            slug=self.kwargs.get('activity_slug', None)
        )

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ActivityView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the connected curriculum links
        context['activity_curriculum_links'] = self.object.curriculum_links.all()
        return context


class OtherResourcesView(generic.DetailView):
    model = Topic
    template_name = 'topics/topic-other-resources.html'
    slug_url_kwarg = 'topic_slug'