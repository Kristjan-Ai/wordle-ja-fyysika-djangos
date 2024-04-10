from urllib.request import HTTPRedirectHandler
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.template import Library
from wordle.models import mang
from django.urls import reverse
from Sõnade_loend.valmis_sonad import sonade_list
import random as r

# Create your views here.
def valik(request, viga):
    vead = {
        1:"Sellise id-ga mängu ei ole!"
    }
    sonum = vead[viga]
    return render(request, "wordle/valik.html", sonum)

def algus(request):
    sonade_arv = len(sonade_list)-1
    mitmes_suvaline = r.randint(0, sonade_arv)
    oige_sona  = sonade_list[mitmes_suvaline]
    # Teeb vahet uuel mängul ja valitud id-ga mängul
    if request.method == "POST" and request.POST.get("mangu_id")!="" and int(request.POST.get("mangu_id"))>=0:
        mangu_id = request.POST.get("mangu_id")
        try:
            mangu_objekt = mang.objects.get(id=mangu_id)
            mitmes = mangu_objekt.mitmes
            print(mangu_objekt)
            # Teeb listid värvide ja tähtedega template'i saatmiseks
            sona1 = mangu_objekt.sona1
            sona1.extend(mangu_objekt.sona1_varv)
            sona2 = mangu_objekt.sona2
            sona2.extend(mangu_objekt.sona2_varv)
            sona3 = mangu_objekt.sona3
            sona3.extend(mangu_objekt.sona3_varv)
            sona4 = mangu_objekt.sona4
            sona4.extend(mangu_objekt.sona4_varv)
            sona5 = mangu_objekt.sona5
            sona5.extend(mangu_objekt.sona5_varv)
            context = {
                "sona1": sona1,
                "sona2": sona2,
                "sona3": sona3,
                "sona4": sona4,
                "sona5": sona5,
                "sonum": "Meil on "+str(sonade_arv+1)+" viietähelist sõna.",
                "mitmes": mitmes,
                "mangu_id": mangu_id,}
            return render(request, "wordle/wordle.html", context)
        except:
            return HttpResponseRedirect(reverse("valik/viga1"))
    else:
        uus_mang = mang(oige_sona=oige_sona)
        uus_mang.save()
        mangu_id = uus_mang.id
        mitmes = 1
        print(uus_mang)
        context = {"sonum": "Meil on "+str(sonade_arv+1)+" viietähelist sõna.", "mitmes": mitmes, "mangu_id": mangu_id,}
        return render(request, "wordle/wordle.html", context)

def kontroll(request):
    if request.method=="POST":
        mangu_id = request.POST.get("mangu_id")
        mangu_objekt = mang.objects.get(id=mangu_id)
        mitmes = mangu_objekt.mitmes
        print("mitmes:", mitmes)
        sona = request.POST.get("taht1")+request.POST.get("taht2")+request.POST.get("taht3")+request.POST.get("taht4")+request.POST.get("taht5")
        oige_sona = mangu_objekt.oige_sona
        #salvesta sona vastavalt mitmes on ning leia oiged varvid kastide jaoks
        sona_pole = False
        oige_varv = "green"
        sees_varv = "yellow"
        pole_varv = "lightgrey"
        if mitmes == 1:
            if sona in sonade_list:
                mangu_objekt.sona1 = list(sona)
                mangu_objekt.save()
                mitmes_taht = 0
                for taht in mangu_objekt.sona1:
                    if taht == list(oige_sona)[mitmes_taht]:
                        (mangu_objekt.sona1_varv).pop(mitmes_taht)
                        (mangu_objekt.sona1_varv).insert(mitmes_taht, oige_varv)
                        mangu_objekt.save()
                        mitmes_taht += 1
                    elif taht in list(oige_sona):
                        (mangu_objekt.sona1_varv).pop(mitmes_taht)
                        (mangu_objekt.sona1_varv).insert(mitmes_taht, sees_varv)
                        mangu_objekt.save()
                        mitmes_taht += 1
                    else:
                        (mangu_objekt.sona1_varv).pop(mitmes_taht)
                        (mangu_objekt.sona1_varv).insert(mitmes_taht, pole_varv)
                        mangu_objekt.save()
                        mitmes_taht += 1
            else:
                sona_pole = True
        elif mitmes == 2:
            if sona in sonade_list:
                mangu_objekt.sona2 = list(sona)
                mangu_objekt.save()
                mitmes_taht = 0
                for taht in mangu_objekt.sona2:
                    if taht == list(oige_sona)[mitmes_taht]:
                        (mangu_objekt.sona2_varv).pop(mitmes_taht)
                        (mangu_objekt.sona2_varv).insert(mitmes_taht, oige_varv)
                        mangu_objekt.save()
                        mitmes_taht += 1
                    elif taht in list(oige_sona):
                        (mangu_objekt.sona2_varv).pop(mitmes_taht)
                        (mangu_objekt.sona2_varv).insert(mitmes_taht, sees_varv)
                        mangu_objekt.save()
                        mitmes_taht += 1
                    else:
                        (mangu_objekt.sona2_varv).pop(mitmes_taht)
                        (mangu_objekt.sona2_varv).insert(mitmes_taht, pole_varv)
                        mangu_objekt.save()
                        mitmes_taht += 1
            else:
                sona_pole = True
        elif mitmes == 3:
            if sona in sonade_list:
                mangu_objekt.sona3 = list(sona)
                mangu_objekt.save()
                mitmes_taht = 0
                for taht in mangu_objekt.sona3:
                    if taht == list(oige_sona)[mitmes_taht]:
                        (mangu_objekt.sona3_varv).pop(mitmes_taht)
                        (mangu_objekt.sona3_varv).insert(mitmes_taht, oige_varv)
                        mangu_objekt.save()
                        mitmes_taht += 1
                    elif taht in list(oige_sona):
                        (mangu_objekt.sona3_varv).pop(mitmes_taht)
                        (mangu_objekt.sona3_varv).insert(mitmes_taht, sees_varv)
                        mangu_objekt.save()
                        mitmes_taht += 1
                    else:
                        (mangu_objekt.sona3_varv).pop(mitmes_taht)
                        (mangu_objekt.sona3_varv).insert(mitmes_taht, pole_varv)
                        mangu_objekt.save()
                        mitmes_taht += 1
            else:
                sona_pole = True
        elif mitmes == 4:
            if sona in sonade_list:
                mangu_objekt.sona4 = list(sona)
                mangu_objekt.save()
                mitmes_taht = 0
                for taht in mangu_objekt.sona4:
                    if taht == list(oige_sona)[mitmes_taht]:
                        (mangu_objekt.sona4_varv).pop(mitmes_taht)
                        (mangu_objekt.sona4_varv).insert(mitmes_taht, oige_varv)
                        mangu_objekt.save()
                        mitmes_taht += 1
                    elif taht in list(oige_sona):
                        (mangu_objekt.sona4_varv).pop(mitmes_taht)
                        (mangu_objekt.sona4_varv).insert(mitmes_taht, sees_varv)
                        mangu_objekt.save()
                        mitmes_taht += 1
                    else:
                        (mangu_objekt.sona4_varv).pop(mitmes_taht)
                        (mangu_objekt.sona4_varv).insert(mitmes_taht, pole_varv)
                        mangu_objekt.save()
                        mitmes_taht += 1
            else:
                sona_pole = True
        elif mitmes == 5:
            if sona in sonade_list:
                mangu_objekt.sona5 = list(sona)
                mangu_objekt.save()
                mitmes_taht = 0
                for taht in mangu_objekt.sona5:
                    if taht == list(oige_sona)[mitmes_taht]:
                        (mangu_objekt.sona5_varv).pop(mitmes_taht)
                        (mangu_objekt.sona5_varv).insert(mitmes_taht, oige_varv)
                        mangu_objekt.save()
                        mitmes_taht += 1
                    elif taht in list(oige_sona):
                        (mangu_objekt.sona5_varv).pop(mitmes_taht)
                        (mangu_objekt.sona5_varv).insert(mitmes_taht, sees_varv)
                        mangu_objekt.save()
                        mitmes_taht += 1
                    else:
                        (mangu_objekt.sona5_varv).pop(mitmes_taht)
                        (mangu_objekt.sona5_varv).insert(mitmes_taht, pole_varv)
                        mangu_objekt.save()
                        mitmes_taht += 1
            else:
                sona_pole = True
        else:
            print("MITMES ON KATKI - väärtus: "+str(mitmes))
        print(mangu_objekt)

        #teeb listid tahtede ja varvidega
        sona1 = mangu_objekt.sona1
        sona1.extend(mangu_objekt.sona1_varv)
        sona2 = mangu_objekt.sona2
        sona2.extend(mangu_objekt.sona2_varv)
        sona3 = mangu_objekt.sona3
        sona3.extend(mangu_objekt.sona3_varv)
        sona4 = mangu_objekt.sona4
        sona4.extend(mangu_objekt.sona4_varv)
        sona5 = mangu_objekt.sona5
        sona5.extend(mangu_objekt.sona5_varv)

        #kui sona pole anna märku ja kui on pane mitmendale juurde
        if sona_pole:
            sonum = "Sellist eestikeelset sõna meil pole, proovi mõnda teist!"
        else:
            mitmes += 1
            mangu_objekt.mitmes = mitmes
            mangu_objekt.save()   
            sonum = ""
        context = {
            "sona1": sona1,
            "sona2": sona2,
            "sona3": sona3,
            "sona4": sona4,
            "sona5": sona5,
            "sonum": sonum,
            "mitmes": mitmes,
            "mangu_id": mangu_id,
        }
        if sona == oige_sona:
            context.update({"sonum": "Arvasid ära!"})
            return render(request, "wordle/wordle.html", context)
        elif mitmes > 5:
            context.update({"sonum": ("Mäng läbi! Õige sõna oli "+oige_sona+" 🤦")})
            return render(request, "wordle/wordle.html", context)
        else:
            return render(request, "wordle/wordle.html", context)
    elif request.method=="GET":
        return HttpResponseRedirect(reverse("valik"))