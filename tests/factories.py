import factory

from goals.models import GoalCategory


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GoalCategory