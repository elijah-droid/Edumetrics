from django.db import models
from django.utils.timezone import now


methods = (
    ('Cash', 'Cash'),
    ('MTNUG', 'MTNUG'),
    ('AIRTELUG', 'AIRTELUG'),
    ('Other', 'Other')
)

paid_via = (
    ('School', 'School'),
    ('Mobile', 'Mobile')
)

class Payment(models.Model):
    parent = models.ForeignKey('Parents.Parent', models.CASCADE)
    Student = models.ForeignKey('Students.Student', models.SET_NULL, null=True)
    Due = models.ForeignKey('PaymentDue', models.CASCADE)
    Method = models.CharField(max_length=20, choices=methods)
    Amount = models.PositiveIntegerField(null=True)
    Paid_Via = models.CharField(max_length=100, choices=paid_via, null=True)
    Date = models.DateTimeField(default=now)


class PaymentDue(models.Model):
    School = models.ForeignKey('Schools.School', models.CASCADE)
    Term = models.ForeignKey('Terms.Term', models.SET_NULL, null=True, blank=True)
    Reason = models.CharField(max_length=100)
    Amount_Required = models.PositiveIntegerField(null=True)
    Payments = models.ManyToManyField('Payment', blank=True)
    Classes = models.ManyToManyField('Classes.Class', blank=True)
    Compulsory = models.BooleanField(default=False)

    def __str__(self):
        return self.Reason
