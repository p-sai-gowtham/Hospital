from django.db import models
from django.contrib.auth.models import User



departments=[('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]
class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    department= models.CharField(max_length=50,choices=departments,default='Cardiologist')
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.id)
    @property
    def assigned_patients_count(self):
        return Patient.objects.filter(assigned_doctor=self).count()



class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True, null=True)
    symptoms = models.CharField(max_length=100,blank=True, null=False)
    assigned_doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    sex = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')],blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    hospital_referred_by = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True, null=True,related_name='hospital_referred_by')
    test_description = models.TextField(blank=True, null=True)
    scans = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('to_do', 'To Do'), ('in_review', 'In Review'), ('done', 'Done')], default='to_do',blank=True, null=True)
    emergency = models.BooleanField(default=False)
    report_status = models.CharField(max_length=20, blank=True, null=True)
    patient_id = models.CharField(max_length=50, unique=True, blank=True, null=True)
    study_date = models.DateField(blank=True, null=True)
    study_time = models.TimeField(blank=True, null=True)
    accession = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    modality = models.CharField(max_length=50, blank=True, null=True)
    images = models.IntegerField(blank=True,null=True) # Consider changing to FileField if uploading images
    center = models.CharField(max_length=100, blank=True, null=True)
    is_printed = models.BooleanField(default=False)

    @property 
    def get_name(self):
        return self.user.username
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.username

class Reports(models.Model):
    report = models.FileField(upload_to='reports',null=True,blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True, related_name='report')