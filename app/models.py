from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=20)
    period = models.CharField(max_length=20)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    mentor = models.ForeignKey('Mentor', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=20)
    birth_date = models.DateField()

    def __str__(self):
        return self.name


class Mentor(models.Model):
    name = models.CharField(max_length=20)
    job_expirience = models.CharField(max_length=20)

    def __str__(self):
        return self.name
