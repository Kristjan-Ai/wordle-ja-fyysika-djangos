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

def home(request):
    return render(request, 'home.html')

def calculate(request):
    if request.method == 'POST':
        v0 = float(request.POST.get('algkiirus'))
        h = float(request.POST.get('korgus'))
        a1 = float(request.POST.get('nurk'))
        planeet = request.POST.get('planeet')

        if planeet == 'merkuur':
            g = 3.7
        elif planeet == 'veenus':
            g = 8.87
        elif planeet == 'maa':
            g = 9.81
        elif planeet == 'marss':
            g = 3.71
        elif planeet == 'jupiter':
            g = 24.79
        elif planeet == 'saturn':
            g = 10.44
        elif planeet == 'uraan':
            g = 8.69
        elif planeet == 'neptuun':
            g = 11.15
        elif planeet == 'pluuto':
            g = 0.62
        elif planeet == 'kuu':
            g = 1.62
        elif planeet == 'paike':
            g = 274

        # graafiku joonestamine
        plt.clf()
        x  = np.linspace(0,pall(v0,a1,h,g)['L'],100)
        y = eval(pall(v0,a1,h,g)['valem'])
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

        # graafiku ja andmete HTML-i edastamine
        return render(request, 'home.html', {'kaugus': pall(v0,a1,h,g)['L'], 'aeg_lennul': pall(v0,a1,h,g)['T'], 'max_korgus': pall(v0,a1,h,g)['H'], 'aeg_haripunktis': pall(v0,a1,h,g)['t'], 'kaugus_haripunktis': pall(v0,a1,h,g)['l1'], 'loppkiirus': pall(v0,a1,h,g)['v'], 'maandumisnurk': pall(v0,a1,h,g)['a2'], 'algkiirus': v0, 'korgus': h, 'nurk': a1, 'planeet': planeet, 'graafik': image_base64})

    return render(request, 'home.html')

