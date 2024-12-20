from django import forms
from django.contrib.auth.models import User
from . import models



#for admin signup
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets = {
        'password': forms.PasswordInput()
        }


#for student related form
class DoctorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
        
class DoctorForm(forms.ModelForm):
    class Meta:
        model=models.Doctor
        fields=['address','mobile','department','status','profile_pic']



#for teacher related form
class PatientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username']
        widgets = {
        'password': forms.PasswordInput()
        }

class PatientForm(forms.ModelForm):
    class Meta:
        model=models.Patient
        fields = [
            'sex', 'age', 'test_description', 'symptoms', 
            'hospital_referred_by', 'assigned_doctor', 
            'scans', 'emergency', 'report_status',
            'patient_id', 'study_date', 'study_time', 
            'accession', 'department', 'modality', 
            'images', 'center', 
            'is_printed'
        ]
