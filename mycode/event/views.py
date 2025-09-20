from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from django.contrib import messages

# Home page (Add event form)
def home(request):
    if request.method == "POST":
        event_name = request.POST.get("event_name")
        event_type = request.POST.get("event_type")
        description = request.POST.get("description")
        location = request.POST.get("location")
        date = request.POST.get("date")
        time = request.POST.get("time")
        entry_fee = request.POST.get("entry_fee")

        Event.objects.create(
            event_name=event_name,
            event_type=event_type,
            description=description,
            location=location,
            date=date,
            time=time,
            entry_fee=entry_fee,
        )
        return redirect("events")

    return render(request, "home.html")


def events(request):
    events = Event.objects.all().order_by("date")
    return render(request, "events.html", {"events": events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, "event_detail.html", {"event": event})


def register_participant(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == "POST":
        members_count = request.POST.get("members")
        messages.success(
            request,
            f"The number of members ({members_count}) has been registered for the event: {event.event_name}"
        )
    return redirect("event_detail", event_id=event.id)


def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    messages.success(request, f"The event '{event.event_name}' has been deleted successfully.")
    return redirect("events")