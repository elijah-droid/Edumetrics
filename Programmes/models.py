from django.db import models

names = (
    ('Boarding', 'Boarding'),
    ('Day School', 'Day School')
)


class Programme(models.Model):
    School = models.ForeignKey('Schools.School', models.SET_NULL, null=True)
    Name = models.CharField(max_length=100, choices=names)
    Fees = models.ManyToManyField('FeesManagement.PaymentDue', blank=True)
    Students = models.ManyToManyField('Students.Student', blank=True)
    Requirements = models.TextField(max_length=10000, null=True)

    def __str__(self):
        return self.Name
