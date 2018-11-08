from django.urls import path

from .views import EventCreateView,MyEventListView, HomePageView,EventListView,EventDetailView,EventUpdateView

urlpatterns = [
    path("", HomePageView.as_view(), name = "home"),
    path("events/", EventListView.as_view(), name = "event_list"),
    path("events/myevents/", MyEventListView.as_view(), name = "myevent_list"),
    path("events/addevent/", EventCreateView.as_view(), name = "event_create"),
    path("events/<int:pk>/updateevent/", EventUpdateView.as_view(), name = "event_update"),
    path("events/<int:pk>/", EventDetailView.as_view(), name = "event_detail")


]