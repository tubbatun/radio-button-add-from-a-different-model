from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse

import json
from django.core import serializers

from . import forms
from .models import *


def package_add(request):
    if request.user == request.user.is_staff or request.user.is_superuser:
        if request.method == 'POST':
            form = forms.PackageForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                ajaxData = {}
                ajaxData['msg'] = 'Thank you!'
                return HttpResponse(json.dumps(ajaxData))
            else:
                ajaxData = {}
                ajaxData['msg'] = 'Sorry no data saved!'
                return HttpResponse(json.dumps(ajaxData))
        else:
            form = forms.PackageForm()
        context = {
            "form": form,
        }
        return render(request, "package/package_form.html", context)
    else:
        raise Http404
