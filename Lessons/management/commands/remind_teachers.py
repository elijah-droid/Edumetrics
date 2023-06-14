from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.contrib.auth.models import User
from Teachers.models import Teacher
from django.utils.timezone import now



class Command(BaseCommand):
    help = 'Send Reminders For Teachers Lessons'

    def handle(self, *args, **options):
        day = now().strftime("%A")
        teachers = Teacher.objects.filter(Lessons__Day=day).distinct()
        print(teachers)
        for teacher in teachers:
            lessons = teacher.Lessons.filter(Day=day)
            message = f'''
            Good Morning Teacher {teacher.user.first_name},

            You have {lessons.count()} Lesson(s) to teach today.

            {', '.join(f'{lesson.Subject} at {lesson.From}' for lesson in lessons)}.

            Have a nice day

            '''
            send_mail(
                "Teacher's Lessons reminder",
                message,
                'edumetrics@edu-metrics.com',
                [teacher.user.email]
            )
        self.stdout.write('Lesson reminders sent successfully')
