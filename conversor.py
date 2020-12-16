def tempo(valor, conv):
    if conv == 1:
        return f""" A conversão será de segundos para minutos.
               {valor} segundo(s) correspondem a {valor/60} minuto(s)."""

    elif conv == 2:
        return f""" A conversão será de segundos para horas.
        {valor} segundo(s) correspondem a {valor/3600} hora(s)."""

    elif conv == 3:
        return f""" A conversão será de minutos para segundos.
        {valor} minuto(s) correspondem a {valor*60} segundo(s)."""
    
    elif conv == 4:
        return f""" A conversão será de minutos para horas.
        {valor} minuto(s) correspondem a {valor/60} hora(s)."""
    
    elif conv == 5:
        return f""" A conversão será de horas para segundos.
        {valor} hora(s) correspondem a {valor*3600} segundo(s)."""
    
    elif conv == 6:
        return f""" A conversão será de horas para minutos.
        {valor} em horas correspondem a {valor*60} minutos."""


def velocidade(valor, conv):
    if conv == 1:
        return f""" A conversão será de km/h para m/s.
        {valor} km/h correspondem a {valor/3.6} m/s."""

    elif conv == 2:
        return f""" A conversão será de km/h para cm/min.
        {valor} km/h correspondem a {valor*1667} cm/min."""

    elif conv == 3:
        return f""" A conversão será de m/s para km/h.
        {valor} m/s correspondem a {valor*3.6} km/h."""
    
    elif conv == 4:
        return f""" A conversão será de m/s para cm/min.
        {valor} m/s correspondem a {valor*6000} cm/min."""
    
    elif conv == 5:
        return f""" A conversão será de cm/min para m/s.
        {valor} cm/min correspondem a {valor/6000} m/s."""
    
    elif conv == 6:
        return f""" A conversão será cm/min para km/h.
        {valor} cm/min correspondem a {valor/1667} km/h."""

def menu():
    print("""
    --------------------------------------------------------------
                        Conversor de Medidas
    --------------------------------------------------------------
    """)
    while True:
        try:
            num = float(input('           Qual valor númerico você quer converter?'))
        except:
            print('           Inválido, pelo visto você não sabe ler.')
        else:
            return num
            break
    


def menuUm():
    ops = [1, 2, 3, 4]
    print(f"""
    --------------------------------------------------------------
                            Conversor de Medidas
        1 - Tempo ( Horas, minutos e segundos. )
        2 - Velocidade ( km/h, m/s, cm/min. )
        3 - Conversão aleatória.
 
    --------------------------------------------------------------
    """)
    while True:
        try:
            op = int(input('     Escolha uma opção. '))
        except:
            print('     Não é um inteiro.')
        else:
            if op not in ops:
                print('     Não é uma opção válida.')
            else:
                return op
                break
    
def menuDois():
    ops = [1, 2, 3, 4, 5, 6]
    print("""
    ---------------------------------------------------------------------
                        Conversor de Medidas
        TEMPO -> 
        1 - De segundos para minutos.
        2 - De segundos para horas.
        3 - De minutos para segundos.
        4 - De minutos para horas.
        5 - De horas para segundos.
        6 - De horas para minutos.
    ----------------------------------------------------------------------
     """)
    while True:
        try:
            op = int(input('     Escolha uma opção. '))
        except:
            print('     Não é um inteiro.')
        else:
            if op not in ops:
                print('     Não é uma opção válida.')
            else:
                return op
                break

def menuTres():
    ops = [1, 2, 3, 4, 5, 6]
    print("""
    ---------------------------------------------------------------------
                        Conversor de Medidas
        VELOCIDADE -> 
        1 - De km/h para m/s.
        2 - De km/h para cm/min.
        3 - De m/s para km/h.
        4 - De m/s para cm/min.
        5 - De cm/min para m/s.
        6 - De cm/min para km/h
    ---------------------------------------------------------------------
     """)
    while True:
        try:
            op = int(input('     Escolha uma opção. '))
        except:
            print('     Não é um inteiro.')
        else:
            if op not in ops:
                print('     Não é uma opção válida.')
            else:
                return op
                break





    