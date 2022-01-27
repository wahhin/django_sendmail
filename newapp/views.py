from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
import pandas as pd
import numpy as np
from datetime import datetime
import calendar

import os
from django.conf import settings
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from datetime import datetime
from xhtml2pdf import pisa
from django_xhtml2pdf.utils import generate_pdf
#import imgkit
from django.core.mail import send_mail, EmailMultiAlternatives
#from AstroProject.settings import EMAIL_HOST_USER

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


def generate_PDF(request):

    nysestuff = nyse.objects.all()
    riskappstuff = riskapp.objects.all()
    feargreedstuff = feargreed.objects.all()
    putcallstuff = putcall.objects.all()
    feargreednm = [float(feargreedstuff[i].Fear_Greed / 100) for i in range(len(feargreedstuff))]
    outputdata = [(float(nysestuff[i].NYSE_Up_Vol) + feargreednm[i] + float(putcallstuff[i].Put_Call) + float(
        riskappstuff[i].Risk_App)) / 4 for i in range(len(feargreedstuff))]
    yesno = [outputdata[i] > 0.5 for i in range(len(outputdata))]
    colors = ["red" if i == True else "black" for i in yesno]
    # notation = ["Risk Indicator > 0.5" if colors =="red" else "Risk Indicator <= 0.5" for i in colors]
    labels = [convert_timestamp(str(nysestuff[i].Daily_NYSE)) for i in range(len(nysestuff))]
    p25 = outputdata.index(np.percentile(outputdata, 25))
    p75 = outputdata.index(np.percentile(outputdata, 75))

    context = {
        'outputdata': outputdata,
        'labels': labels,
        'yesno': yesno,
        'colors': colors,
        # 'notation': notation,
        'p25': p25,
        'p75': p75,
    }

    # resp = HttpResponse(content_type='application/pdf')
    # result = generate_pdf('newapp/index.html', file_object=resp, context=context)
    # return result

    template = get_template('newapp/index.html')
    html = template.render(context)

    file = open('test.pdf', "w+b")
    pisaStatus = pisa.CreatePDF(html, dest=file)

    file.seek(0)
    pdf = file.read()
    file.close()
    return HttpResponse(pdf, 'application/pdf')


def SaveScreenshot(request):

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

    return render(request, 'newapp/SaveScreenshot.html', context=context)

def emails (request):

    # get the context for html
    nysestuff = nyse.objects.all()
    riskappstuff = riskapp.objects.all()
    feargreedstuff = feargreed.objects.all()
    putcallstuff = putcall.objects.all()
    # define context
    feargreednm = [float(feargreedstuff[i].Fear_Greed / 100) for i in range(len(feargreedstuff))]
    outputdata = [(float(nysestuff[i].NYSE_Up_Vol) + feargreednm[i] + float(putcallstuff[i].Put_Call) + float(
        riskappstuff[i].Risk_App)) / 4 for i in range(len(feargreedstuff))]
    yesno = [outputdata[i] > 0.5 for i in range(len(outputdata))]
    colors = ["red" if i == True else "black" for i in yesno]
    # notation = ["Risk Indicator > 0.5" if colors =="red" else "Risk Indicator <= 0.5" for i in colors]
    labels = [convert_timestamp(str(nysestuff[i].Daily_NYSE)) for i in range(len(nysestuff))]
    p25 = outputdata.index(np.percentile(outputdata, 25))
    p75 = outputdata.index(np.percentile(outputdata, 75))

    context = {
        'outputdata': outputdata,
        'labels': labels,
        'yesno': yesno,
        'colors': colors,
        # 'notation': notation,
        'p25': p25,
        'p75': p75,
    }

    # since the graph cannot be very large, get the subset of the whole dataset
    l = len(feargreedstuff)
    feargreednm_sub = [float(feargreedstuff[i].Fear_Greed / 100) for i in range(l-250,l)]
    outputdata_sub = [(float(nysestuff[i].NYSE_Up_Vol) + feargreednm[i] + float(putcallstuff[i].Put_Call) + float(
        riskappstuff[i].Risk_App)) / 4 for i in range(l-250,l)]
    yesno_sub = [outputdata[i] > 0.5 for i in range(l-250,l)]
    colors_sub = ["red" if i == True else "black" for i in yesno_sub]
    # notation = ["Risk Indicator > 0.5" if colors =="red" else "Risk Indicator <= 0.5" for i in colors]
    labels_sub = [convert_timestamp(str(nysestuff[i].Daily_NYSE)) for i in range(l-250,l)]

    chart_config = {
        'type': 'line',
        'data': {
            'labels': labels_sub,
            'datasets': [{
                'label': 'Risk Indicator',
                'data':  outputdata_sub,
                'fill': False,
                'pointBackgroundColor': colors_sub,
                'backgroundColor': 'grey',
                'borderWidth': 1
            }]
        },
        'options': {
            'scales': {
                'y': {
                    'beginAtZero': False
                }
            }
        },
        'plugins': {
            'annotation': {
                'annotations': {
                    'line1': {
                        'id': 'a-line-1',
                        'type': 'line',
                        'mode': 'horizontal',
                        'scaleID': 'y-axis-0',
                        'value': 0.5,
                        'borderColor': 'red',
                        'borderWidth': 2,
                        'label': {
                            'enabled': True,
                            'position': "top",
                            'content': "somelabel"
                        }
                    }
                }
            }
         },
    }

    import json
    from urllib.parse import quote
    import requests

    postdata = {
        'chart': json.dumps(chart_config),
        'width': 500,
        'height': 300,
        'backgroundColor': 'transparent',
    }

    resp = requests.post('https://quickchart.io/chart/create', json=postdata)
    parsed = json.loads(resp.text)

    #encoded_config = quote(json.dumps(chart_config))
    #chart_url = f'https://quickchart.io/chart?c={encoded_config}'

    r = requests.get(parsed['url'], stream=True)
    #r = requests.get(chart_url, stream=True)
    if r.status_code == 200:
        with open('risk.png', 'wb') as f:
            for chunk in r:
                f.write(chunk)

    email_message = f"""Hello, this is my email body containing a chart image. Please see the chart in the attachment:
    """
    #
    #send the email
    from_email = settings.EMAIL_HOST_USER
    to_email = ['']
    subject = 'Risk Indicator'
    msg = EmailMultiAlternatives(subject, email_message, from_email,
                                 ['shannontan@wah-hin.com.sg','whwebapp@gmail.com'])

    # html_template = get_template('newapp/index.html').render(context=context)
    # msg.attach_alternative(html_template, "text/html")
    #from email.mime.text import MIMEText
    #msg.attach(MIMEText(html_template, 'html'))

    from email.mime.image import MIMEImage
    with open('risk.png', 'rb') as f:
         img = MIMEImage(f.read())


    msg.attach(img)
    msg.send()

    return render(request, 'newapp/index.html', context=context)
