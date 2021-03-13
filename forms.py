from django import forms

class videoupload(forms.Form):
    Choose_File= forms.FileField()

class fadeinn(forms.Form):
    initial_color= forms.FloatField()
    duration=forms.IntegerField()
class speedx1(forms.Form):
    final_duration= forms.IntegerField()
class volumex1(forms.Form):
    factor=forms.FloatField()
class rotate1(forms.Form):
    angle=forms.FloatField()
class gammacorrection1(forms.Form):
    factor1=forms.FloatField()
class subclip1(forms.Form):
    start_time=forms.FloatField()
    end_time=forms.FloatField()
