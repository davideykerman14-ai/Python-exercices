temperature = -3

if temperature <= 0:
    print("gel")
elif temperature == 15:
    print("froid")
elif temperature < 25: 
    print("doux")
else:
    print("chaud") 

annee = 2000

if (annee % 4 == 0 and annee % 100 != 0):
    print("bissextile")
elif annee % 400 == 0:
    print("bissextile")
else:
    print ("non bissextile")
