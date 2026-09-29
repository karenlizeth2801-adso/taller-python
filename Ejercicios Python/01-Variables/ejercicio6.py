segundos = int(input("Segundos: "))

horas = segundos // 3600
resto = segundos % 3600

minutos = resto // 60
segundos_restantes = resto % 60

print(segundos, "segundos equivalen a:")
print(horas, "hora(s)")
print(minutos, "minuto(s)")
print(segundos_restantes, "segundo(s)")
