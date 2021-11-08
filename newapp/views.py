from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

import pandas as pd
import numpy as np
from datetime import datetime
import calendar


# Create your views here.
def data(request):
    nysestuff = nyse.objects.all()
    riskappstuff = riskapp.objects.all()
    feargreedstuff = feargreed.objects.all()
    putcallstuff = putcall.objects.all()
    feargreednm = [float(feargreedstuff[i].Fear_Greed/100) for i in range(len(feargreedstuff))]
    outputdata = [(float(nysestuff[i].NYSE_Up_Vol) + feargreednm[i] + float(putcallstuff[i].Put_Call) + float(riskappstuff[i].Risk_App))/4 for i in range(len(feargreedstuff))]
    yesno = [outputdata[i] > 0.5 for i in range(len(outputdata))]
    colors = ["red" if i==True else "black" for i in yesno]
    #notation = ["Risk Indicator > 0.5" if colors =="red" else "Risk Indicator <= 0.5" for i in colors]
    labels = [convert_timestamp(str(nysestuff[i].Daily_NYSE)) for i in range(len(nysestuff))]
    p25 = outputdata.index(np.percentile(outputdata, 25))
    p75 = outputdata.index(np.percentile(outputdata, 75))

    context= {
        'outputdata': outputdata,
        'labels': labels,
        'yesno': yesno,
        'colors': colors,
        #'notation': notation,
        'p25': p25,
        'p75': p75,
    }
    return render(request, 'newapp/index.html', context=context)

def convert_timestamp(dt):
    dt = datetime.strptime(dt, '%Y-%m-%d')
    month = dt.month
    month_char = calendar.month_abbr[month]
    return str(dt.year) +'-'+ str(month_char)