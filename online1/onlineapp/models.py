from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.conf import settings

class LoanRequest(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    description_loan = models.TextField()


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'student'),
        (2, 'faculty'),
        (3, 'college_admin'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    name = models.CharField(max_length=100,blank=True,null=True)
    age = models.IntegerField(blank=True,null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    clg_name = models.CharField(max_length=100,blank=True,null=True)
    email = models.CharField(max_length=100,blank=True,null=True)
    contact = models.CharField(max_length=15, blank=True, null=True)
    qualification = models.CharField(max_length=255, blank=True, null=True)
    class_name = models.CharField(max_length=255, blank=True, null=True)
    fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    verifi = models.CharField(max_length=255, blank=True, null=True)
    student_guid = models.CharField(max_length=20, blank=True, null=True) 
    student_conformation = models.CharField(max_length=20, blank=True, null=True) 
    payment = models.CharField(max_length=20, blank=True, null=True)
    reason =  models.CharField(max_length=100, blank=True, null=True)


class question_paper(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    test_id = models.IntegerField(blank=True,null=True)     
    question = models.CharField(max_length=200)
    obtionA = models.CharField(max_length=50,blank=True,null=True)
    obtionB = models.CharField(max_length=50,blank=True,null=True)
    obtionC = models.CharField(max_length=50,blank=True,null=True)
    obtionD = models.CharField(max_length=50,blank=True,null=True)
    correct_answer = models.CharField(max_length=50,blank=True,null=True)

class score(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    test_id = models.CharField(max_length=100,blank=True,null=True)     
    worng_ans = models.IntegerField(blank=True,null=True)
    tot =  models.IntegerField(blank=True,null=True)
    student_score = models.IntegerField(blank=True,null=True)


class subject_name(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sub = models.CharField(max_length=105)

 
class category(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    categoryy = models.CharField(max_length=105)
    subject = models.CharField(max_length=105)


class study_meterial(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, blank=True,null=True)
    meterial =  models.FileField(upload_to='meterial')
    subject = models.CharField(max_length=255)  # Ensure this field exists



class video_meterial(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, blank=True,null=True)
    video =  models.FileField(upload_to='video')
    subject = models.CharField(max_length=255)  # Ensure this field exists


class Grant(models.Model):
    title = models.CharField(max_length=105)
    point = models.TextField()


class job(models.Model):
    img =  models.FileField(upload_to='job')
    title = models.CharField(max_length=105)
    point = models.TextField()

class Loan(models.Model):
    title = models.CharField(max_length=105)
    point = models.TextField()

class incentive(models.Model):
    title = models.CharField(max_length=105)
    point = models.TextField()
