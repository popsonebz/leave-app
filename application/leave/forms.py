from django import forms
from .models import employee, leave
from django.forms import DateField, DateInput
from functools import partial
from datetime import date, datetime
from workdays import networkdays
from django.contrib.auth.models import User
from Hr import settings


DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class LeaveForm(forms.ModelForm):
    start_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    end_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    error_css_class = 'error'
    user = None

    class Meta:
        model = leave
        fields = ['start_date', 'end_date']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(LeaveForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(LeaveForm, self).clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and end_date:
            if start_date < date.today():
                self._errors["start_date"] = self.error_class([(u"This date has passed.")])
            elif end_date < date.today():
                self._errors["end_date"] = self.error_class([(u"This date has passed.")])
            elif end_date < start_date:
                self._errors["end_date"] = self.error_class([(u"End date cannot earlier than start date.")])
            elif start_date > end_date:
                self._errors["start_date"] = self.error_class([(u"Start date cannot later than end date.")])
            elif start_date == end_date:
                self._errors["end_date"] = self.error_class([(u"End date cannot be the same as start date.")])
            elif networkdays(start_date, end_date) > 18 :
                self._errors["other_errors"] = self.error_class([(u"You cannot take more than 18 days of leave")])
            elif networkdays(start_date, end_date) == 0 :
                self._errors["other_errors"] = self.error_class([(u"No working days within this period.")])
            #else:
            #    self._errors["other_errors"] = self.error_class([(u"Something is wrong with the date entered. Please, Select from the calender.")])

        try:
            obj = User.objects.select_related().get(username=str(self.user))
        except User.DoesNotExist:
            obj = None

        def diff_month(start_date, end_date):
            return (start_date.year - end_date.year) * 12 + start_date.month - end_date.month

        if diff_month(start_date, obj.employee.employment_date) < 3:
            self._errors["other_errors"] = self.error_class([(
            u"You cannot apply for leave as you just got employed less than 3 months ago.")])

        elif obj.employee.number_of_leave_days_left == 0:
            self._errors["other_errors"] = self.error_class([(
            u"You have exhausted your leave for the year")])
        elif networkdays(start_date, end_date) > obj.employee.number_of_leave_days_left:
            self._errors["other_errors"] = self.error_class([(
            u'Sorry, you have %s day(s) leave left. kindly select a shorter period' % obj.employee.number_of_leave_days_left )])

        return cleaned_data
