from django.shortcuts import render, redirect
from .models import Event
from .forms import ScheduleEventForm
from django.core.mail import send_mail


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
            event = form.save(commit=False)
            event.School = request.user.schooladministrator.current_school
            event.save()
            request.user.schooladministrator.current_school.Events.add(event)
            message = f'''
            {event.School} has scheduled a {event.title}, Please endeavour to attend if your child attends.
            {', '.join(event.Classes.all())}.

            See you There.
            '''
            send_mail(
                f'{request.user.schooladministrator.current_school} {event.title} Event.',
                message,
                'edumetrics@sparklehandscs.com',
                [parent.user.email for parent in list(event.School.Parents.all())]
            )
            return redirect('events')
    else:
        form = ScheduleEventForm()
    form.fields['Classes'].queryset = request.user.schooladministrator.current_school.classes.all()
    context = {
        'form': form
    }
    return render(request, 'schedule_event.html', context)
