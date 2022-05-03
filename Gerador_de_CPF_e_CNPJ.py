from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
from random import randint
import pyperclip as pc

cor1 = "#ffffff" #Branca
cor2 = "#85b1ff" #azul escuro
cor3 = "#9cf1f7" #azul claro
cor4 = "#000000" #preto

#janela
janela = Tk()
janela.title('Gerador de CPF e CNPJ')
janela.geometry("500x300")
janela.configure(background=cor3)
janela.resizable(width=FALSE, height=FALSE)


#frame de cima, de baixo e o visor
frame_cima = Frame(janela, width=500, height=100, bg=cor3, relief='flat')
frame_cima.grid(row=0, column=0,pady=1,padx=0,sticky=NSEW)


frame_visor = Frame(janela, width=400, height=70, bg=cor1, relief='solid',borderwidth=2)
frame_visor.grid(row=1, column=0,pady=1,padx=0,)


frame_baixo = Frame(janela, width=500, height=130, bg=cor3, relief='flat')
frame_baixo.grid(row=2, column=0,pady=1,padx=0,sticky=NSEW)



#código

valor= ""
visor= StringVar()


def gerar_cpf():
    global valor
    numero= str(randint(100000000, 999999999))
    novo_cpf = numero
    reverso = 10
    total= 0

    for numero in range(19):
        if numero > 8:
            numero -= 9
    
        total += int(novo_cpf[numero]) * reverso
        reverso -=1 

    
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total=0
            novo_cpf += str(d)
            valor=novo_cpf
            visor.set(valor)
            pc.copy(valor)

            

        
def gerar_cnpj():
    global valor
    cnpj=str(randint(10000000, 99999999))   

    novo_cnpj=cnpj[:8] + "0001"
                 
    total= 0
    multiplicador = 5
    multiplicador2 = 9

    for numero in range(12):                                    
        if multiplicador > 1 and multiplicador <= 5:           
            total += int(novo_cnpj[numero]) * multiplicador 
            multiplicador = multiplicador - 1               
        else:                                                  
            total += int(novo_cnpj[numero]) * multiplicador2 
            multiplicador2 = multiplicador2 - 1             

    d = 11 - (total % 11)                                      
    if d > 9:
        d=0

    multiplicador = 6                                          
    total2 = 0
    multiplicador2 = 9
    novo_cnpj = novo_cnpj + str(d)

    for numero in range(13):
        if multiplicador > 1 and multiplicador <= 6:
            total2 += int(novo_cnpj[numero]) * multiplicador
            multiplicador = multiplicador - 1
        else:
            total2 +=int(novo_cnpj[numero])*multiplicador2
            multiplicador2 = multiplicador2 - 1
    d2= 11 - (total2 % 11)
    if d2 > 9:
        d2=0                  
    novo_cnpj = novo_cnpj + str(d2)
    valor = novo_cnpj
    visor.set(valor)
    pc.copy(valor)
    

 

#trabalhando no frame de cima

l_nome = Label(frame_cima, text="-=- Gerador de CPF e CNPJ -=-", anchor=NE, font=("Helvetica 20  italic"), bg=cor3, fg=cor4)
l_nome.place(x=55,y=30)

l_linha = Label(frame_cima, text="", anchor=NW, font=("Helvetica 1"), bg=cor2, fg=cor4, width=550)
l_linha.place(x=3,y=70)

#trabalhando os botões

b1 = Button(frame_baixo, text="GERAR CPF", width=17, height=2, bg=cor2, fg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=gerar_cpf)
b1.place(x=30, y=9)

b2 = Button(frame_baixo, text="GERAR CNPJ", width=17, height=2, bg=cor2, fg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=gerar_cnpj)
b2.place(x=290, y=9)

#visor

app_label=Label(frame_visor, textvariable=visor, width=26, height=2, padx=9, relief=FLAT, anchor="e", justify=RIGHT, font=("Ivy 18 "), bg=cor1)
app_label.place(x=0,y=0)

janela.mainloop()
 