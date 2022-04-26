from asyncio import events
from tkinter import *



cor1 = "#29ffd8" #esmeralda
cor2 = "#ff94ff" #rosa claro
cor3 = "#f7c8f7" #rosa claro +
cor4 = "#ffffff" #branco
cor5 = "#ff00ff" #rosa choque
cor6 = "#000000" #preto



janela = Tk()
janela.title("Calculadora")
janela.geometry("235x300")
janela.config(bg=cor2)
janela.resizable(width=FALSE, height=FALSE)


#frame
frame_tela= Frame(janela, width=235, height=50, bg=cor1)
frame_tela.grid(row = 0, column=0)

frame_corpo = Frame(janela, width=235, height=268, bg=cor3)
frame_corpo.grid(row=1, column=0)


#lógica

valores = ""
valor_string = StringVar()

#visor
def entra_valor(Event):
    
    global valores
    
    valores= valores + str(Event)
    
    valor_string.set(valores)

#calcular
def calcular():
    global valores
    
    resultado = eval(valores)
    
    valor_string.set(resultado)


#limpar visor
def limpar():
    
    global valores
    
    valores=""
    
    valor_string.set(valores)




#label

app_label=Label(frame_tela, textvariable=valor_string, width=16, height=2, padx=9, relief=FLAT, anchor="e", justify=RIGHT, font=("Ivy 18 "), bg=cor3)
app_label.place(x=0,y=0)




#botões
b1 = Button(frame_corpo, text="C", width=11, height=2, bg=cor2, fg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=limpar)
b1.place(x=0, y=0)
b2 = Button(frame_corpo, text="%", width=5,height=2, bg=cor2, fg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda:entra_valor("%"))
b2.place(x=118,y=0)
b3= Button(frame_corpo, text="/", width=5, height=2, bg=cor5, fg=cor6, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda:entra_valor("/"))
b3.place(x=177,y=0)

b4 = Button(frame_corpo, text="7", width=5,height=2, bg=cor2, fg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda:entra_valor("7"))
b4.place(x=0,y=52)
b5 = Button(frame_corpo, text="8", width=5,height=2, bg=cor2, fg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda:entra_valor("8"))
b5.place(x=59,y=52)
b6= Button(frame_corpo, text="9", width=5, height=2, bg=cor2, fg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda:entra_valor("9"))
b6.place(x=118,y=52)
b7 = Button(frame_corpo, text="*", width=5,height=2, bg=cor5, fg=cor6, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda:entra_valor("*"))
b7.place(x=177,y=52)

b8 = Button(frame_corpo, text="4", width=5,height=2, bg=cor2, fg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda:entra_valor("4"))
b8.place(x=0,y=104)
b9 = Button(frame_corpo, text="5", width=5,height=2, bg=cor2, fg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda:entra_valor("5"))
b9.place(x=59,y=104)
b10= Button(frame_corpo, text="6", width=5, height=2, bg=cor2, fg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda:entra_valor("6"))
b10.place(x=118,y=104)
b11 = Button(frame_corpo, text="-", width=5,height=2, bg=cor5, fg=cor6, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda:entra_valor("-"))
b11.place(x=177,y=104)

b12 = Button(frame_corpo, text="1", width=5,height=2, bg=cor2, fg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda:entra_valor("1"))
b12.place(x=0,y=156)
b13 = Button(frame_corpo, text="2", width=5,height=2, bg=cor2, fg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda:entra_valor("2"))
b13.place(x=59,y=156)
b14= Button(frame_corpo, text="3", width=5, height=2, bg=cor2, fg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda:entra_valor("3"))
b14.place(x=118,y=156)
b15 = Button(frame_corpo, text="+", width=5,height=2, bg=cor5, fg=cor6, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda:entra_valor("+"))
b15.place(x=177,y=156)

b16 = Button(frame_corpo, text="0", width=11, height=2, bg=cor2, fg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda:entra_valor("0"))
b16.place(x=0, y=200)
b17 = Button(frame_corpo, text=",", width=5,height=2, bg=cor2, fg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda:entra_valor("."))
b17.place(x=118,y=200)
b18= Button(frame_corpo, text="=", width=5, height=2, bg=cor5, fg=cor6, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=calcular)
b18.place(x=177,y=200)




janela.mainloop()
 