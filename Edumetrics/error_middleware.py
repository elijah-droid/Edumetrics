from django.core.mail import send_mail




class ErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            # Call the next middleware or view
            response = self.get_response(request)
        except Exception as exception:
            print('h')
            send_mail(
                'Application Error',
                exception,
                'debug@edu-metrics.com',
                'mukisaelijah293@gmail.com'
            )
            raise exception
