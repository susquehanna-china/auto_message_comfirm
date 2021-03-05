from django.shortcuts import render, HttpResponse
from .models import PortfolioCompany
from django.template import loader
from django.views.decorators import csrf
from django.db.models import F
from django.http import HttpResponse
import json


# Create your views here.
def index(request):
    if request.POST:
        try:
            company = PortfolioCompany.objects.get(tele_number=request.POST['tele_number'])
            if company.status:
                return render(request, 'index.html', {'result': 'exist'})
            else:
                # company = PortfolioCompany.objects.get(tele_number=request.POST['tele_number'])
                company.status = 1
                company.save()
                return render(request, 'index.html', {'result': 'commit success'})
        except PortfolioCompany.DoesNotExist:
            return render(request, 'index.html', {'result': 'no such info'})

    return render(request, 'index.html', {})


def report(request):
    if request.method == 'POST':
        result = json.loads(request.body)
        for item in result:
            print(item)
            if item['content'] == '1':
                tele_number = item['mobile']
                try:
                    company = PortfolioCompany.objects.get(phone=tele_number)
                    company.status = True
                    company.save()
                except PortfolioCompany.DoesNotExist:
                    pass

        return HttpResponse('ok')
    else:
        result = request
        print(result)
    return HttpResponse('method error')


