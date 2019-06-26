from django.shortcuts import render

# Create your views here.

from django_tables2.tables import Table
import pandas as pd
from jeelizGlasses.models import AddSku

def jeeliz(request):
	skul = AddSku.objects



	return render(request,'demo.html',{'skul':skul})