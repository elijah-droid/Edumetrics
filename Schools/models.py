from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, Crop

states = (
    ('Uganda', 'Uganda'),
)

setup_steps = (
    ('levels', 'levels'),
)


class School(models.Model):
    name = models.CharField(max_length=100)
    motto = models.CharField(max_length=100, null=True)
    badge = ProcessedImageField(
        upload_to='Schools/Badges',
        processors=[ResizeToFill(200, 200), Crop(200, 200)],
        format='JPEG',
        options={'quality': 90},
        null=True, blank=True
    )
    setup_step = models.CharField(max_length=20, choices=setup_steps, null=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    current_term = models.ForeignKey('Terms.Term', models.SET_NULL, null=True, blank=True)
    Dues = models.ManyToManyField('FeesManagement.PaymentDue', blank=True)
    state = models.CharField(max_length=100, choices=states)
    zip_code = models.CharField(max_length=10)
    mtn_account = models.PositiveIntegerField(null=True, blank=True)
    Enrollments = models.ManyToManyField('Enrollments.Enrollment', blank=True)
    airtel_account =  models.PositiveIntegerField(null=True, blank=True)
    Levels = models.ManyToManyField('Levels.Level', blank=True)
    students = models.ManyToManyField('Students.Student', related_name='school_children', blank=True)
    old_students = models.ManyToManyField('Students.Student', through='EducationHistory.EducationHistory', related_name='school_old_students')
    Teachers = models.ManyToManyField('Teachers.Teacher', through='Teachers.WorkProfile')
    Administrators = models.ManyToManyField('SchoolAdministrators.SchoolAdministrator', through="SchoolAdministrators.Adminship")
    Parents = models.ManyToManyField('Parents.Parent', blank=True)
    Terms = models.ManyToManyField('Terms.Term', blank=True, related_name="school_terms")
    classes = models.ManyToManyField('Classes.Class', blank=True)
    Events = models.ManyToManyField('Events.Event', blank=True, related_name='school_events')
    Reports = models.ManyToManyField('Reports.Report', blank=True, related_name='school_reports')
    Examinations = models.ManyToManyField('Examinations.Examination', blank=True)
    Grades = models.ManyToManyField('Grading.Grade', blank=True)
    Divisions = models.ManyToManyField('Grading.Division', blank=True)
    Subjects = models.ManyToManyField('Subjects.Subject', blank=True)
    Combinations = models.ManyToManyField('Subjects.Combination', blank=True)
    Lessons = models.ManyToManyField('Lessons.Lesson', blank=True)
    attendance = models.ManyToManyField('Attendance.Attendance', blank=True)
    Circulars = models.ManyToManyField('Circulars.Circular', blank=True)
    Books = models.ManyToManyField('LibraryManagement.Book', blank=True)
    Programmes = models.ManyToManyField('Programmes.Programme', blank=True)
    patient_admissions = models.ManyToManyField('SickBay.Admission', blank=True)
    mark_sheets = models .ManyToManyField('MarkSheets.MarkSheet', blank=True)
    Applications = models.ManyToManyField('Applications.Application', related_name='parent_applications', blank=True)

    def __str__(self):
        return self.name
