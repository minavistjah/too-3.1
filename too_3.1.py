while True:
    print("Vali ülesanne 1-4, 0-väljumiseks:")
    valik= input("Sisesta valik: ")
    if valik=="1":
        print("Ülesanne 1")
        #1
        # Sisestatakse 15 arvu.
        #Määrata, mitu neist on täisarvud.
        #for kasutades
        for i in range(15):
            try:
                arv = float(input(f"Sisesta {i+1}. arv: "))
                if arv.is_integer():
                    print(f"{arv} on täisarv.")
                else:
                    print(f"{arv} ei ole täisarv.")
            except ValueError:
                print("Sisestatud väärtus ei ole arv.")
    elif valik=="2":
        #2
        #Küsi kasutajalt arv A ja leia kõigi naturaalarvude summa vahemikus 1 kuni A.
        summa=0
        try:
            A = int(input("Sisesta arv A: "))
            if A < 1:
                print("A peab olema naturaalarv (1 või suurem).")
            else:
                for i in range(1, A + 1):  #i=1,2,3, ..., A
                    summa += i             #1+2+3+...+A
                print(f"Naturaalarvude summa vahemikus 1 kuni {A} on: {summa}")
        except ValueError:
            print("Sisestatud väärtus ei ole täisarv.")
    elif valik=="3":
        #3
        # Sisestatakse 8 arvu.Leida nende korrutis (ainult positiivsete arvude puhul).
        korrutis=1
        for i in range(8):   #0,1,2,3,4,5,6,7 , samm=0 range(0,8,1)
            try:
                arv = float(input(f"Sisesta {i+1}. arv: "))
                if arv > 0:
                    korrutis *= arv
            except ValueError:
                print("Sisestatud väärtus ei ole arv.")
    elif valik=="4":
          #4
          #Koosta programm, mis väljastab ekraanile arvude ruudud vahemikus 10 kuni 20
        for i in range(10, 21):  #i=10,11,12,...,20
            print(f"{i} ruut on {i**2}")
    elif valik=="0":
        #5
        summa = 0
        try:
            N = int(input("Sisesta arv N: "))
            for i in range(N):
                arv = float(input(f"Sisesta {i+1}. arv: "))
                if arv < 0:
                    summa+= arv
             print(f"Negatiivsete arvude summa on: {summa}")
         except ValueError:
             print("Sisestatud väärtus ei ole arv.")
    elif valik=="0":
        print("Väljun programmist.")
        break
    #6
            try:
                N = int(input("Sisesta arv N: "))
                for i in range(N):
                    arv = float(input(f"Sisesta {i+1}. arv: "))
                    if arv < 0:
                        negatiivsed += 1
                    elif arv > 0:
                        positiivsed += 1
                    else:
                        nullid += 1
                print(f"Negatiivsete arvude arv: {negatiivsed}")
                print(f"Positiivsete arvude arv: {positiivsed}")
                print(f"Nullide arv: {nullid}")
            except ValueError:
                elif valik=="7":
        #7
        try:
            A = int(input("Sisesta arv A:"))
            B = int(input("Sisesta arv B:"))
            K = int(input("Sisesta arv K:"))
            if A > B:
                print("A peab olema väiksem või võrdne B-ga.")
                A, B = B, A
            print(f"Arvud vahemikus [{A}, {B}], mis on {K}-ga jaguvad:")
            for i in range (A, B + 1):
                if i % K == 0:
                    print(i)
        except ValueError:
            print("Sisestatud väärtus ei ole täisarv.")
    elif valik=="0":
        print("Väljun programmist.")
        break
#31
K = int(input("Sisesta kotlettide arv (K): "))
M = int(input("Sisesta panni mahutavus (M): "))

tais_pannid = 0
jääk = K

while jääk >= M:
    jääk -= M
    täis_pannid += 1

print(f"Täis pannitäisi: {täis_pannid}")
print(f"Viimasele pannile jääb: {jääk}")
#22
summa = 0
for arv in range(100, 201):
    if arv % 17 == 0:
        summa += arv

print("Summa (for):", summa)
#10
for i in range(1, 11):
  a = float(input(f"{i}. paar – sisesta esimene arv: "))
  b = float(input(f"{i}. paar – sisesta teine arv: "))

  if a > b:
    print(f"Suurem arv: {a}")
  elif b > a:
    print(f"Suurem arv: {b}")
  else:
    print("Arvud on võrdsed.")
#25
N = int(input("Sisesta naturaalarv N: "))
loendur = 0
i = 1

while i <= N:
  if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
    loendur += 1
  i += 1

print(f"Selliseid arve on: {loendur}")
#26
for a in range(10, 100):
    for b in range(10, 100):
        neljakohaline = a * 100 + b
        if neljakohaline % (a * b) == 0:
            print(f"Arvud: {a} ja {b} -> {neljakohaline}")
