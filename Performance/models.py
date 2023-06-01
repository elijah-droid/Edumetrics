from django.db import models

class Performance(models.Model):
    School = models.ForeignKey('Schools.School', models.CASCADE)
    Class = models.ForeignKey('Classes.Class', models.CASCADE)
    Subject = models.ForeignKey('Subjects.Subject', models.CASCADE)
    