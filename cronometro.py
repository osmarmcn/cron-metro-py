from tkinter import*
from geral import *

janela = Tk()
janela.title('Cronômetro')
janela.geometry('450x300')
janela.config(bg='black')
janela.resizable(width=False, height=False)









#------------- label ------------------
app_nome = Label(janela, text='cronômetro', font=('Arial 10'), bg='black', fg='white')
app_nome.place(x=20, y=5)

label_tempo = Label(janela, text=tempo, font=('Times 50 bold'), bg='black', fg='lightblue')
label_tempo.place(x=100, y=45)


#------------ botões
iniciar_app = Button(janela, text='Iniciar', width=10, height=2 , bg='black', fg='white', font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
iniciar_app.place(x=95, y=180)

pausar_app = Button(janela, text='Pausar', width=10, height=2 , bg='black', fg='white', font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
pausar_app.place(x=180, y=180)

reiniciar_app = Button(janela, text='Reiniciar', width=10, height=2 , bg='black', fg='white', font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
reiniciar_app.place(x=265, y=180)

janela.mainloop()