f1 = open("sonad.txt", "r", encoding="utf-8")
f2 = open("valmis_sonad.py", "w", encoding="utf-8")
tekst = f1.readlines()
sonade_list = []
tähestik = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r",]
for rida in tekst:
    rida = rida.strip().lower()
    if len(rida) == 5 and rida.isalpha() and rida not in sonade_list:
        sonade_list.append(rida)
f2.write("sonade_list = "+str(sonade_list))
f1.close()
f2.close()
