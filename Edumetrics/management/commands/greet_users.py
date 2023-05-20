from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.contrib.auth.models import User



class Command(BaseCommand):
    help = 'Send Greetings To Users'

    def handle(self, *args, **options):
        send_mail(
            'Good Morning Elijah',
            'Start your day with ',
            'edumetrics@edu-metrics.com',
            ['mukisaelijah293@gmail.com']
        )
        self.stdout.write('greeted users successfully')
