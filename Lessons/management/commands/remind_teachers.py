from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.contrib.auth.models import User



class Command(BaseCommand):
    help = 'Send Reminders For Teachers Lessons'

    def handle(self, *args, **options):
        for user in User.objects.exclude(email=None):
            ls = ', '(f'{lessons.filter(School=p.School).count()} in {p.School} that is {", ".join(f'{l} @ {l.time} in {l.Class}' for l in lessons.filter(School=p.School))}' for p in teacher.work_profile if lessons.filter(School=p.School).count() >= 1)
            lessons_to_teach = ", ".join(f'{l} @ {l.time} in {l.Class}' for l in lessons)
            message = f'''
            You have {ls} Today,
            {lessons_to_teach}
            '''
            send_mail(
                f'Good Morning Teacher {teacher.user.first_name}',
                message,
                'edumetrics@edu-metrics.com',
                [teacher.user.email]
            )
        self.stdout.write('sent successfully')
