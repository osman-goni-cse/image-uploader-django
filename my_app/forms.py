from django import forms
from .models import Image
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from django.contrib.admin import widgets
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker

class ImageForm(forms.ModelForm):
  # event = forms.DateTimeField(input_formats=['%Y/%m/%d %H:%M'])
  event = forms.DateTimeField(
    widget=DateTimePicker(
      options={
          'useCurrent': True,
          'collapse': False,
      },
      attrs={
          'append': 'fa fa-calendar',
          'icon_toggle': True,
      }
  ),
)
  
  class Meta:
    model = Image
    fields = '__all__'
    labels = {'photo':'Image'}
    # widgets = {
    #   'event':forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input', 'data-target': '#datetimepicker1'}),
    # }

    # date = forms.DateTimeField(
    #   input_formats=['%d/%m/%Y %H:%M'],
    #   widget=forms.DateTimeInput(attrs={
    #       'class': 'form-control datetimepicker-input',
    #       'data-target': '#datetimepicker1'
    #   })
    # )

# class ImageForm(forms.ModelForm):
#   start_time = forms.SplitDateTimeField(widget=AdminSplitDateTime())
#   end_time = forms.SplitDateTimeField(widget=AdminSplitDateTime())

#   class Meta:
#       model = Image
#       fields = "__all__"
#       widgets = {
#           "date": AdminDateWidget(),
#           "time": AdminTimeWidget(),
#       }
  
    