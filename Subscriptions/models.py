from django.db import models
from django.utils.timezone import now

amount = (
    (30000, 30000),
)

methods = (
    ('MTN MOMO', 'MTN MOMO'),
    ('Airtel Money', 'Airtel Money'),
)

class Subscription(models.Model):
    School = models.ForeignKey('Schools.School', models.CASCADE)
    Parent = models.ForeignKey('Parents.Parent', models.CASCADE)
    Date = models.DateTimeField(default=now)
    Payment = models.ForeignKey('Payments.Payment', models.SET_NULL, null=True)



