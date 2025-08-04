from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('fullname', 'mobile', 'emp_num', 'job_position')
        labels = {'fullname': 'Full Name', 'emp_num' : 'Employee number'}

    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['job_position'].empty_label = "Select"  