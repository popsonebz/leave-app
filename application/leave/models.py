# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from workdays import networkdays

from django.contrib.auth.models import User

class employee(models.Model):
    user = models.OneToOneField(User, null=True, blank=True)
    employment_date = models.DateField()
    number_of_leave_days_left = models.IntegerField(default=18)

    def __unicode__(self):
        return "employee"

class leave(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    days_of_leave = models.IntegerField()
    employee = models.ForeignKey(employee, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)

    def __unicode__(self):
        return "leave"


    def save(self, *a, **kw):

        self.days_of_leave = networkdays(self.start_date, self.end_date)

        self.status = "Approved"

        obj = employee.objects.get(id = self.employee.id)

        obj.number_of_leave_days_left = obj.number_of_leave_days_left - self.days_of_leave

        obj.save()

        super(leave, self).save(*a, **kw)
