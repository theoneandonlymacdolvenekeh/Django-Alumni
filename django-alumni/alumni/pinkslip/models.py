from django.db import models

# Create your models here.

#creating the profile model
from django.contrib.auth.models import User

class profile(models.Model):
    user               = models.OneToOneField(User, unique=True, null=False, db_index=True, on_delete=models.CASCADE )


    student_id                     = models.IntegerField( blank=False, null=True, help_text='enter your student id here')
    year_of_graduation              = models.IntegerField(null=False, blank=False)
    date_of_birth                   = models.DateField(blank=False, null=False)
    technical_program               = models.CharField(max_length=255, blank=False, null=False)
    street_address                  = models.CharField(max_length=255, blank=False, null=False)
    city                            = models.CharField(max_length=255, blank=False, null=False)
    apt                             = models.IntegerField(blank=False, null=False)
    state                           = models.CharField(max_length=255, blank=False, null=False)
    zip_code                        = models.IntegerField(blank=False, null=False)
    phone_number                    = models.IntegerField(blank=False, null=False)
    company_name                    = models.CharField(max_length=255, blank=False, null=False)
    company_adddress                = models.CharField(max_length=255, blank=False, null=False)
    job_title                       = models.CharField(max_length=255, blank=False, null=False)
    wage                            = models.IntegerField(blank=True, null=True, default=0)
    college_acceptance_letter       = models.FileField(blank=True, null=True)
    college_attend                  = models.CharField(max_length=255, null=True, blank=True, default='none')
    college_year_lenght             = models.IntegerField(blank=False, null=True, help_text='enter your student id here')
    military_branch                 = models.CharField(max_length=255, null=True, blank=False, default='none')
    military_letter                 = models.FileField(null=True, blank=True)
    A_adams_scholarship             = models.BooleanField(default=False, blank=False, null=True)
    technical_certification         = models.CharField(default='none', max_length=255, blank=True, null=True, help_text='enter your student id here')
    osha_training                   = models.BooleanField(null=True, blank=False)
    osha_number                     = models.IntegerField(blank=True, null=True)
    WTHS_certification              = models.CharField(max_length=255, blank=True, null=True, help_text='enter your student id here')
    future_plans                    = models.TextField(blank=False, null=True, help_text='what are your future plans')






