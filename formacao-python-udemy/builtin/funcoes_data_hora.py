from datetime import datetime,timedelta

data_completa = datetime.now() # Pegando data e hora no agora

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

data1 = datetime.datetime(2020,10,20)
data2 = datetime.datetime(2020,11,20)
diferenca = data2 - data1
print(diferenca) # Calculando diferença com data

data_atual = datetime.now()
datafutura1 = data_atual + timedelta(weeks=4) # acrescentando 4 semanas à data atual
datafutura1 = data_atual + timedelta(days= 30) # acrescentando 30 dias à data atual
datafutura1 = data_atual + timedelta(hours=12) # acrescentando 12 horas à data atual
datafutura1 = data_atual + timedelta(minutes=60) # acrescentando 60 minutos à data atual

data_txt = input("Digite a data no formato dia/mês/ano: ")
data = datetime.strptime(data_txt,"%d/%m/Y")
print(data)