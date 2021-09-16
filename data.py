from datetime import datetime

#Operações realizadas pela API 


def count(start, end):
    # Data final
    date_end = datetime.strptime(end, '%d/%m/%Y')

    # Data inicial
    date_start = datetime.strptime(start, '%d/%m/%Y')

    # Realizamos o calculo da quantidade de dias
    quantidade_dias = abs((date_end - date_start).days)
    return (quantidade_dias+1)

def calc(value, debt):
    total = value + (value*debt/100)
    return total