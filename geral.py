import cronometro

global tempo
global rodar
global contador
global limitdaor 



tempo = "00:00:00"
rodar = False
contador = -5
limitador = 59

def horas():
    global tempo
    global contador
    global limitador
    temporaria = str(tempo)
    h,m,s = map(int,temporaria.split(":"))
    h = int(h)
    m = int(m)
    s = int(contador)

    if s >= limitador:
        contador = 0
        m += 1

    s = f'{str(0)}{str(s)}'
    m = f'{str(0)}{str(m)}'
    h = f'{str(0)}{str(h)}'

    #atualizar valores
    temporaria = f'{str(h[-2:])}:{str(m[-2:])}:{str(s[-2:])}'
    cronometro.label_tempo['text'] = temporaria
    tempo = temporaria

    
def iniciar():
    import cronometro
    global tempo
    global contador 

    if rodar:
        if contador <= -1:
            inicio = f'Começando  em: {contador}'
            cronometro.label_tempo['text'] = inicio
            cronometro.label_tempo['font'] = 'Arial 10'

        else:
            cronometro.label_tempo['font'] = 'Times 50 bold'
            horas()
        
        cronometro.label_tempo.after(1000, iniciar)
        contador += 1    



def start():
    global rodar
    rodar = True
    iniciar()


def pausar():
    global rodar
    rodar = False

def reiniciar():
    import cronometro

    global tempo
    global contador
    
    tempo = "00:00:00"
    contador = 0
    cronometro.label_tempo['text'] = tempo


