# structuri de date
import gc
from collections import deque

valori = []
valori = [1, 2, 3, 4, 5]
print(valori)
valori = list(range(1, 6))
print(valori)

valori.append(6)
print(valori)
valoare = valori.pop()
print(valoare)
print(valori)
valoare = valori[0]
print(valoare)
print(valori)
valori[0] = 10
print(valori)

# operatii cu liste
valoriSecundare = [20, 30, 40]
valoriCompuse = valori + valoriSecundare
print(valoriCompuse)
valoriSecundare = valori * 3
print(valoriSecundare)

valori = [1, 2, 3, 4]
valoriSecundare = [1, 2, 3, 4]
if valoriSecundare == valori:
    print("Au valori identice")
else:
    print("Au valori non identice")

# shallow copy
vector2 = [1, 2, 3, 4]
vector3 = vector2
print(vector3[0])
vector3[0] = 10
print(vector3)
print(vector2)

# deep copy
vector2 = [1, 2, 3, 4]
# 1st method
vector3 = vector2.copy()
# 2nd method
vector3 = vector2[:]
print(vector3[0])
vector3[0] = 10
print(vector3)
print(vector2)

# slice si unpacking
valoare1, valoare2, *valori_ramase = vector3
print(valori_ramase)

print(valori)
valori_ramase = [valoare * 2 for valoare in valori]
valori_pare = [valoare for valoare in valori if valoare % 2 == 0]
print(valori_ramase)
print(valori_pare)

# conversie lista la coada
coada = deque(valori)
print(coada)

coada.append(5)
print(coada)
coada.pop()
print(coada)
coada.popleft()
print(coada)

# tupluri
valori_constante = (1, 2, 3, 4, 5)
print(valori_constante)
# valori_constante[0] = 10
# print(valori_constante)

# seturi
valori_unice = {1, 2, 3, 4, 5}
print(valori_unice)
valori_unice_diferite = {4, 5, 6, 7}
valori_comune = valori_unice & valori_unice_diferite
print(valori_comune)
valori_unice_set1 = valori_unice - valori_unice_diferite
print(valori_unice_set1)
valori_diferite_ambele_seturi = valori_unice ^ valori_unice_diferite
print(valori_diferite_ambele_seturi)
valori_combinate = valori_unice | valori_unice_diferite
print(valori_combinate)

valori = [1, 2, 3, 4, 4, 4, 4, 5]
valori_unice = set(valori)
print(valori_unice)

# dictionare
angajati = {"john": "team lead", "alice": "dev", "bob": "tester"}
print(angajati)
pozitie = angajati["john"]
print(pozitie)
angajati["bob"] = "dev"
print(angajati)
angajati["Bob"] = "tester"
print(angajati)

print(angajati.keys())

# garbage collector
valori = list(range(1, 10000))
print(valori)
valori = [1, 2, 3]
# fortare apel gc
gc.collect()

# scenariu eveniment tech
participanti = [("John", 23, "Speaker"), ("Alice", 22,  "Participant"), ("Bob", 22, "Organizator")]
print(participanti)
nume_participanti = [p[0] for p in participanti]
participanti_cu_varsta_mare = [p[0] for p in participanti if p[1] > 22]
print(nume_participanti)
print(participanti_cu_varsta_mare)

workshops = []
main_events = []
workshops.append(participanti[0])
workshops.append(participanti[1])

main_events.append(participanti[1])
main_events.append(participanti[2])
print(workshops)
print(main_events)

all_events = workshops + main_events
print(all_events)
participanti_unici = set(all_events)
print(participanti_unici)

participanti_la_toate_evenimentele = set(main_events) & set(workshops)
print(participanti_la_toate_evenimentele)

numar_participari_persoane = {}

for nume in nume_participanti:
    numar_participari_persoane[nume] = len([p for p in all_events if p[0] == nume])

# numar_participari_persoane["John"] = len([p[0] for p in all_events if p[0] == 'John'])
# numar_participari_persoane["Alice"] = len([p[0] for p in all_events if p[0] == 'Alice'])
print(numar_participari_persoane)
