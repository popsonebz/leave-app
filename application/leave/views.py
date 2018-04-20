# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from leave.forms import LeaveForm
from .models import employee

# Create your views here.

@login_required(login_url='/leave/login/')
def leave(request):

    
    if request.method == 'POST':

    	user = request.user

        try:
            obj = User.objects.select_related().get(username=str(user))
        except employee.DoesNotExist:
            obj = None
            return redirect('leave:login')


        form = LeaveForm(request.POST, user=request.user)

        if form.is_valid():
            form = form.save(commit=False)
            if obj.employee:
                form.employee = obj.employee
            form.save()
            return redirect('leave:leave')

    else:
    	form = LeaveForm()
    return render(request, 'leave/leaveApplication.html', {'form':form})
