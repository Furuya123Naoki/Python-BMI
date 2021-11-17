from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from cms.models import UserHealth
from cms.forms import UserHealthForm
import logging
from django.utils import timezone
from datetime import date, datetime

# Create your views here.


@login_required
def userhealth_list(request):
    """ユーザー健康状態の一覧"""
    #return HttpResponse('ユーザー健康状態の一覧')
    #userhealths = UserHealth.objects.all().order_by('id')
    userhealths = UserHealth.objects.filter(name=request.user).order_by('date').reverse()
    return render(request, 'cms/userhealth_hist.html', {"userhealths": userhealths, })


@login_required
def userhealth_edit(request, userhealth_id=None):
    """ユーザー健康状態の編集"""
    #return HttpResponse('ユーザー健康状態の編集')
    if userhealth_id:
        userhealth = get_object_or_404(UserHealth, pk=userhealth_id)
    else:
        userhealth = UserHealth()

    if request.method == 'POST':
        form = UserHealthForm(request.POST, instance=userhealth)
        if form.is_valid():
            userhealth = form.save(commit=False)
            userhealth.name = request.user
            userhealth.BMI = float(request.POST['Weight']) / (float(request.POST['Height'])/100 )**2
            if userhealth.BMI < 18.5:
                userhealth.condition = "痩せすぎです（BMI：18.5未満）"
            elif 18.5 <= userhealth.BMI < 25:
                userhealth.condition = "標準体型です（BMI：18.5～25）"
            elif userhealth.BMI >= 25:
                userhealth.condition = "肥満気味です（BMI：25以上）"

            #groups = request.user.groups.all()
            #userhealth.group = userhealth.objects.filter(group__in=groups)
            userhealth.save()
            return redirect('cms:userhealth_list')
    else:
        form = UserHealthForm(instance=userhealth)
        form.fields["date"].queryset = request.user.groups.all()

    return render(request, 'cms/userhealth_edit.html', dict(form=form, userhealth_id=userhealth_id))


@login_required
def userhealth_del(request, userhealth_id):
    """ユーザー健康状態の削除"""
    #return HttpResponse('ユーザー健康状態の削除')
    userhealth = get_object_or_404(UserHealth, pk=userhealth_id)
    userhealth.delete()
    return redirect('cms:userhealth_list')