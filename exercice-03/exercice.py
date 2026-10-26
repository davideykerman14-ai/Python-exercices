temperatures = [12.5, 14, 9.5, 17, 21, 19.5, 11]

moyenne = sum(temperatures) / len(temperatures)
print(moyenne)

maximum = max(temperatures)
print(maximum)

minimum = min(temperatures)
print(minimum)

compteur = 0
for temperature in temperatures:
    if temperature > 15:
        compteur += 1
print(compteur)


Fahrenheit = []

for c in temperatures:
    f = c*9/5+32
    Fahrenheit.append(f)
print(Fahrenheit)

for jour, temp in enumerate(temperatures, start=1):
    print(f"jour{jour}: {temp} ° ")
    