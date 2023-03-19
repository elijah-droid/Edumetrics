from django.shortcuts import render, redirect
from .models import Event
from .forms import ScheduleEventForm


def events(request):
    events = Event.objects.all().order_by('-start_time')
    context = {
        'events': events
    }
    return render(request, 'events.html', context)


def schedule_event(request):
    if request.method == 'POST':
        form = ScheduleEventForm(request.POST)
        if form.is_valid():
            event = form.save()
            request.user.schooladministrator.current_school.Events.add(event)
            return redirect('events')
    else:
        form = ScheduleEventForm()
    form.fields['Classes'].queryset = request.user.schooladministrator.current_school.classes.all()
    context = {
        'form': form
    }
    return render(request, 'schedule_event.html', context)
