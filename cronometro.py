from os import times
from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
from tkinter import font


cor1 = "#ffffff" #Branca
cor2 = "#9c0000" #vermelho
cor3 = "#e8e6d5" #bege
cor4 = "#000000" #preto


janela = Tk()
janela.title('Cronômetro')
janela.geometry("600x360")
janela.configure(background=cor3)
janela.resizable(width=FALSE, height=FALSE)


global limit
global tempo
global rodar
global cont
tempo = "00:00:00"
rodar = False
cont = -5
limit = 59

def iniciar():
    global tempo
    global cont
    global limit
    
    if rodar:
        if cont <= -1:
            inicio= str(cont) 
            inicio1= inicio.replace("-" ," ")
            l_tempo["text"]  = "     " + inicio1
            
        else:
            temporaria = str(tempo)
            h,m,s = map(int,temporaria.split(":"))
            h = int(h)
            m = int(m)
            s = int(cont)
            
            if (s>=limit):
                cont = 0
                m +=1
                
                if (m>=limit):
                    m = 0
                    h += 1
             
            s = str(0)+str(s)
            m = str(0)+str(m) 
            h =  str(0)+str(h)
            
            temporaria = str(h[-2:])+":"+str(m[-2:]) +":" + str(s[-2:])
            l_tempo['text'] = temporaria
            tempo = temporaria
            
                   
        l_tempo.after(1000,iniciar)
        cont +=1
        
        
def start():
    global rodar
    rodar=True
    iniciar()

def pausar():
    global rodar
    rodar = False
    
def reiniciar ():
    global cont
    global tempo
    tempo = "00:00:00"
    l_tempo['text'] = tempo
    cont = 0


#label

l_app = Label(janela, text=("-=Cronômetro=-"), font=("Arial 23 italic"), bg = cor3, fg=cor4)
l_app.place(x= 195, y= 5 )

l_tempo = Label(janela, text=tempo, font= "Times 100 bold", bg=cor3, fg=cor2)
l_tempo.place(x=53, y=50 )

b_ini=Button(janela,command=start, text = "Iniciar", width=10, height= 2, bg=cor2, fg=cor3, font="Ivy 18 bold", relief="raised", overrelief="ridge")
b_ini.place(x=20, y=240) 

b_pausar=Button(janela,command=pausar, text = "Pausar", width=10, height= 2, bg=cor2, fg=cor3, font="Ivy 18 bold", relief="raised", overrelief="ridge", justify=None)
b_pausar.place(x=220, y=240) 

b_reini=Button(janela, command=reiniciar,text = "Reiniciar", width=10, height= 2, bg=cor2, fg=cor3, font="Ivy 18 bold", relief="raised", overrelief="ridge")
b_reini.place(x=420, y=240) 


janela.mainloop()
