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
                                            'id':'customer_id',
                                            'class':'form-control mr-sm-2',
                                            'name':'customer'}),

            'product':forms.TextInput(attrs={
                                            'class':'form-control',
                                            'id':'product_id',
                                            'name':'product',
                                            'placeholder':'Enter the product'}),

            'issue':forms.TextInput(attrs={
                                            'class':'form-control',
                                            'id':'issue_id',
                                            'name':'issue',
                                            'placeholder':'Enter the issue'}),

            'estimate_hours':forms.NumberInput(attrs={
                                                    'id':'estimate_hours_id',
                                                    'type':'number',
                                                    'class':'form-control mr-sm-2'}),

            'priority':forms.Select(attrs={
                                            'id':'priority_id',
                                            'class':'form-control mr-sm-2',
                                            'name':'priority'}),

            'engineer':forms.Select(attrs={
                                            'id':'engineer_id',
                                            'class':'form-control mr-sm-2',
                                            'name':'engineer'}),
            'status':forms.Select(attrs={
                                            'id':'status_id',
                                            'class':'form-control mr-sm-2',
                                            'name':'status'}),   
            'start_date':forms.DateInput(attrs={    
                                                    'id':'start_date_id',
                                                    'type': 'date', 
                                                    'class':'form-control mr-sm-2',
                                                    'name':'start_date',
                                                    }),

            'start_time':forms.TimeInput(attrs={
                                                    'id':'start_time_id',
                                                    'type': 'time', 
                                                    'class':'form-control mr-sm-2',
                                                    'name':'start_time'}),
            'end_time':forms.TimeInput(attrs={
                                                    'id':'end_time_id',
                                                    'type':'time',
                                                    'class':'form-control mr-sm-2',
                                                    'name':'end_time'}),
            'end_date':forms.DateInput(attrs={          
                                                    'id':'end_date_id',
                                                    'type': 'date', 
                                                    'class':'form-control mr-sm-2',
                                                    'name':'end_date'}),

            'remarks':forms.Textarea(attrs={
                                            'id':'remarks_id',
                                            'class':'form-control mr-sm-2',
                                            'name':'remarks',
                                            'cols':24,
                                            'rows':5
            })
        }  