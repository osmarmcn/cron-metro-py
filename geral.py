import cronometro

global tempo
global rodar
global contador



tempo = "00:00:00"
rodar = False
contador = 5





def inicar():
    import cronometro
    global tempo
    global rodar
    global contador 

    rodar = True
    if rodar:
        contador = 5
        while contador >= 1:
            inicio = f'começando: {contador}'
            cronometro.label_tempo['text'] = inicio
            cronometro.label_tempo['font'] = 'Arial 10'
           
           

