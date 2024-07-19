flag= "2024-07-05T10:01:34-03:00"
ano=flag.replace("-","")[0:4]
mes = flag.replace("-","")[4:6]
dia = flag.replace("-","")[6:8]
print(ano, mes, dia)