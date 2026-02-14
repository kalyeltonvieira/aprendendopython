import calendar

ano = int(input('DIGITE O ANO: '))
mes = int(input('DIGITE O MES: '))
print(calendar.isleap(ano))
print(calendar.month(ano, mes))