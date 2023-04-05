from django.db import models


methods = (
    ('Cash', 'Cash'),
    ('Bank', 'Bank'),
    ('Mobile Money', 'Mobile Money'),
    ('Other', 'Other')
)

class Payment(models.Model):
    parent = models.ForeignKey('Parents.Parent', models.CASCADE)
    Students = models.ManyToManyField('Students.Student', blank=True)
    Due = models.ForeignKey('PaymentDue', models.CASCADE)
    Method = models.CharField(max_length=20, choices=methods)
    Amount = models.PositiveIntegerField(null=True)


class PaymentDue(models.Model):
    School = models.ForeignKey('Schools.School', models.CASCADE)
    Term = models.ForeignKey('Terms.Term', models.SET_NULL, null=True)
    Reason = models.CharField(max_length=100)
    Amount_Required = models.PositiveIntegerField(null=True)
    Classes = models.ManyToManyField('Classes.Class', blank=True)
