from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("events/", views.events, name="events"),
    path("events/<int:event_id>/", views.event_detail, name="event_detail"),
    path("events/<int:event_id>/register/", views.register_participant, name="register_participant"),
    path("events/<int:event_id>/delete/", views.delete_event, name="delete_event"),
]

