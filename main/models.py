from django.db import models


class Student(models.Model):
    GENDERS = (
        ("male", "Male"),
        ("female", "Female"),
        ("unknown", "Not specified")
    )
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    gender = models.CharField(max_length=15, choices=GENDERS)
    age = models.PositiveIntegerField()
    contact = models.EmailField()

    def __str__(self):
        return f"{self.fname} {self.lname}"


class SchoolYear(models.Model):
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.year}"


class Subject(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class Registration(models.Model):
    std = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='students')
    subject = models.ManyToManyField(Subject, "subjects")
    school_year = models.ForeignKey(SchoolYear, on_delete=models.CASCADE, related_name='years')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.std} {self.subject} {self.school_year} {self.date}"
