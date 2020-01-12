from django import forms

from .models import CallAllocation
import datetime
from django.contrib.admin import widgets
class ItCallAllocation(forms.ModelForm):

    # start_date = forms.DateTimeInput(widget=forms.DateInput(format = '%d/%m/%Y'), 
    #                              input_formats=('%d/%m/%Y',))
    # end_date = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), 
    #                            input_formats=('%d/%m/%Y',), 
    #                            required=False)

    class Meta:
        model = CallAllocation
        fields = ['customer','product','issue','priority','estimate_hours','engineer','status','start_date','end_date','remarks','start_time','end_time']

        widgets = {
            'customer':forms.Select(attrs={
                                            'id':'inputState',
                                            'class':'form-control mr-sm-2',
                                            'name':'customer'}),

            'product':forms.TextInput(attrs={
                                            'class':'form-control',
                                            'id':'nk_product',
                                            'name':'product',
                                            'placeholder':'Enter the product'}),

            'issue':forms.TextInput(attrs={
                                            'class':'form-control',
                                            'id':'inputEmail4',
                                            'name':'issue',
                                            'placeholder':'Enter the issue'}),

            'estimate_hours':forms.NumberInput(attrs={
                                                    'type':'number',
                                                    'class':'form-control mr-sm-2'}),

            'priority':forms.Select(attrs={
                                            'id':'inputState',
                                            'class':'form-control mr-sm-2',
                                            'name':'priority'}),

            'engineer':forms.Select(attrs={
                                            'id':'inputState',
                                            'class':'form-control mr-sm-2',
                                            'name':'engineer'}),
            'status':forms.Select(attrs={
                                            'id':'inputEmail4',
                                            'class':'form-control mr-sm-2',
                                            'name':'status'}),   
            'start_date':forms.DateInput(attrs={
                                                    'type': 'date', 
                                                    'class':'form-control mr-sm-2',
                                                    'name':'start_date',
                                                    }),

            'start_time':forms.TimeInput(attrs={
                                                    'type': 'time', 
                                                    'class':'form-control mr-sm-2',
                                                    'name':'start_time'}),
            'end_time':forms.TimeInput(attrs={
                                                    'type':'time',
                                                    'class':'form-control mr-sm-2',
                                                    'name':'end_time'}),
            'end_date':forms.DateInput(attrs={
                                                    'type': 'date', 
                                                    'class':'form-control mr-sm-2',
                                                    'name':'end_date'}),

            'remarks':forms.Textarea(attrs={
                                            'class':'form-control mr-sm-2',
                                            'name':'remarks',
            })
        }  