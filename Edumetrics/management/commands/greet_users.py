from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.contrib.auth.models import User



class Command(BaseCommand):
    help = 'Send Greetings To Users'

    def handle(self, *args, **options):
        for user in User.objects.exclude(email=None):
            send_mail(
                f'Good Morning {user.first_name}',
                'Remember to start your day with a prayer.',
                'edumetrics@edu-metrics.com',
                [user.email]
            )
        self.stdout.write('greeted users successfully')
