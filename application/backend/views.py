# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date, datetime
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from leave.models import employee
from forms import EmployeeForm


# Create your views here.

def newEmployee(request):
    
    if request.method == 'POST':


        form = EmployeeForm(request.POST)

        if form.is_valid():
            
            username = form['username'].value()
            password = form['password'].value()
            first_name = form['first_name'].value()
            last_name = form['last_name'].value()
        
            new_user = User.objects.create_user(username=username,
                                 first_name = first_name,
                                 password=password, last_name = last_name)
            new_user.save()

            user = User.objects.get(username=username)
            obj = employee()
            obj.user_id = user.id
            obj.employment_date = request.POST['employment_date']
            obj.save()
            return redirect('backend:admin')

    else:
    	form = EmployeeForm()
    return render(request, 'backend/add_new_employee.html', {'form':form})
