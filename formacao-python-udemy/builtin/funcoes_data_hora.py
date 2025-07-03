import datetime

data_completa = datetime.datetime.now() # Pegando data e hora no agora

data = data_completa.date() # Pegando apenas data
hora = data_completa.time() # Pegando apenas hora

print("Dia", data_completa.day)
print("Mês", data_completa.month)
print("Ano", data_completa.year)
print("Hora", data_completa.hour)
print("Minuto", data_completa.minute)
print("Segundo", data_completa.second)

data = datetime.date(2000,9,30) # Passando ano, mês e dia
print(data)

hora = datetime.time(10,30,20) # Passando hora, minuto, segundo
print(hora)

current_time = data_completa.strftime("%y/%m/%d %H:%M:%S") # Formatando texto com data e hora
print(current_time)

print(data_completa.strftime("%A - %a")) # Dia da semana e dia da semana abrevi.
print(data_completa.strftime("%B - %b")) # Mês e mês abrevi.
print(data_completa.strftime("%H - %I")) # Hora em 24hrs e hora em 12 horas
print(data_completa.strftime("%I - %p")) #Formatação com 12hrs com AM ou PM