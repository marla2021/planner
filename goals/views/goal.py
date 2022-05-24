from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.pagination import LimitOffsetPagination

from goals.filters import GoalDateFilter
from goals.models import Goal
from goals.permissions import GoalPermissions
from goals.serializers import GoalCreateSerializer, GoalSerializer


class GoalCreateView(CreateAPIView):
    model = Goal
    permission_classes = [GoalPermissions]
    serializer_class = GoalCreateSerializer


class GoalView(RetrieveUpdateDestroyAPIView):
    model = Goal
    permission_classes = [GoalPermissions]
    serializer_class = GoalSerializer

    def get_queryset(self):
        return Goal.objects.filter(category__board__participants__user_id=self.request.user.id)

    def perform_destroy(self, instance):
        instance.status = Goal.Status.archived
        instance.save()
        return instance


class GoalListView(ListAPIView):
    model = Goal
    permission_classes = [GoalPermissions]
    serializer_class = GoalSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    filterset_class = GoalDateFilter
    ordering_fields = ["due_date", "priority"]
    ordering = ["title"]
    search_fields = ["title", 'description']

    def get_queryset(self):
        return Goal.objects.filter(category__board__participants__user_id=self.request.user.id)


