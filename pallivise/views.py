from django.shortcuts import render
import math
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64

def pall(v0,a1,h,g): # v0 - algkiirus (m/s); a1 - viskenurk (°); h - viskekõrgus maapinnast (m); g - gravitatsioonivälja kiirendus (m/s^2)
    
    if a1 != 0: a1 = math.pi/(180/a1) # viskenurk radiaanides 
    H = (v0**2*(math.sin(a1))**2)/(2*g) + h # haripunkti kõrgus maapinnast
    t = (v0*math.sin(a1))/g # haripunkti jõudmiseks kulunud aeg
    l1 = (pow(v0,2)*math.cos(a1)*math.sin(a1))/g # horisontaalne läbitud kaugus haripunkti jõudmisel
    l2 = (v0*math.cos(a1)*math.sqrt(pow((v0*math.sin(a1)),2)+2*g*h))/g 
    L = l1 + l2 # läbitud horisontaalne pikkus
    T = (v0*math.sin(a1)+math.sqrt(pow((v0*math.sin(a1)),2)+2*g*h))/g # lennuaeg
    v = math.sqrt(v0**2+2*g*h) # kiirus vahetult enne kokkupuudet maapinnaga
    a2 = math.acos((v0*math.cos(a1))/(math.sqrt(v0**2+2*g*h))) # maandumisnurk
    a2 = (a2/math.pi)*180 # maandumisnurk kraadides
    
    # palli trajektoori (parabooli) valemi arvutamine
    if h != 0:
        c = h
        a = (-h)/(L*(l2-l1))
        b = -2*a*l1
        if h > 0: c = '+ '+str(h)
        if b >= 0: valem = '{:.18f}'.format(a)+'*x**2 + '+'{:.18f}'.format(b)+'*x '+str(c)
        elif b < 0: valem = '{:.18f}'.format(a)+'*x**2 +'+'{:.18f}'.format(b)+'*x '+str(c)
    else:
        a = (-H)/(l1**2)
        b = (2*H)/l1
        if b >= 0: valem = '{:.18f}'.format(a)+'*x**2 + '+'{:.18f}'.format(b)+'*x'
        elif b < 0: valem = '{:.18f}'.format(a)+'*x**2 +'+'{:.18f}'.format(b)+'*x'

    return {'H':H, 't':t, 'l1':l1, 'L':L, 'T':T, 'v':v, 'a2':a2, 'valem':valem}

def avarii(v, m, d):
    F = (m*v*v)/(2*d)
    t = (m*v/F)*1000
    a = F/m
    Fm = (m*a)/9.81
    return {'F':F, 't':t, 'a': a, 'Fm':Fm}

def pallivise(request):
    if request.method == 'POST':
        v0 = float(request.POST.get('algkiirus'))
        h = float(request.POST.get('korgus'))
        a1 = float(request.POST.get('nurk'))
        planeet = request.POST.get('planeet')
        kiirendused = {
            'merkuur':3.7,
            'veenus':8.87,
            'maa':9.81,
            'marss':3.71,
            'jupiter':24.79,
            'saturn':10.44,
            'uraan':8.69,
            'neptuun':11.15,
            'pluuto':0.62,
            'kuu':1.62,
            'paike':274.0,
        }
        g = kiirendused[planeet]
        tulemused = pall(v0,a1,h,g)

        # graafiku joonestamine
        plt.clf()
        x  = np.linspace(0,tulemused['L'],100)
        y = eval(tulemused['valem'])
        plt.plot(x,y)
        plt.grid(True)
        plt.title('Palli trajektoor')
        plt.xlabel('Kaugus (m)')
        plt.ylabel('Kõrgus (m)')

        # graafiku pildifailina salvestamine
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
        buffer.close()
        context = {
            'kaugus': tulemused['L'],
             'aeg_lennul': tulemused['T'],
             'max_korgus': tulemused['H'],
             'aeg_haripunktis': tulemused['t'],
             'kaugus_haripunktis': tulemused['l1'],
             'loppkiirus': tulemused['v'],
             'maandumisnurk': tulemused['a2'],
             'algkiirus': v0,
             'korgus': h,
             'nurk': a1,
             'planeet': planeet,
             'graafik': image_base64,
        }
        # graafiku ja andmete HTML-i edastamine
        return render(request, 'pallivise.html', context)
    else:
        return render(request, 'pallivise.html')

def autoavarii(request):
    if request.method == 'POST':
        v = float(request.POST.get('auto_kiirus'))
        m = float(request.POST.get('kaal'))
        turvavoo = request.POST.get('turvavoo')
        if turvavoo == 'jah':
            d = 0.04
        if turvavoo == 'ei':
            d = 0.2
        avarii_andmed = avarii(v,m,d)
        context = {
            'loogijoud': avarii_andmed['F'],
            'peatumisaeg': avarii_andmed['t'],
            'aeglustus': avarii_andmed['a'],
            'surumismass': avarii_andmed['Fm'],
            }
        return render(request, 'autoavarii.html', context) 
    else:
        return render(request, 'autoavarii.html') 

