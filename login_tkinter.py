from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

#cores
cor1 = "#ffffff" #Branca
cor2 = "#3c804e" #verde escuro
cor3 = "#e8d4a2" #bege
cor4 = "#000000" #preto

#código
acesso = ['douglas', '123456789']

def logado():
    l_nome = Label(frame_cima, text="Usuário : " + acesso[0], anchor=NE, font=("Helvetica 20  italic"), bg=cor3, fg=cor4)
    l_nome.place(x=28,y=30)

    l_linha = Label(frame_cima, text="", anchor=NW, font=("Helvetica 1"), bg=cor2, fg=cor4, width=550)
    l_linha.place(x=28,y=90)
    
    l_nome = Label(frame_baixo, text="Seja bem vindo, " + acesso[0], anchor=NE, font=("Helvetica 20 "), bg=cor3, fg=cor4)
    l_nome.place(x=5,y=105)

def verificador_acesso():
    nome = e_nome.get()
    senha = e_senha.get()
    
    if nome =='admin' and senha == 'admin':
        messagebox.showinfo('Login', 'Seja bem vindo admin')
    elif acesso[0] == nome and acesso[1] == senha:
        messagebox.showinfo('Login', 'Seja bem vindo outra vez! ' + acesso[0])
        
        for Widget in frame_baixo.winfo_children():
            Widget.destroy()
        for Widget in frame_cima.winfo_children():
            Widget.destroy()
            
        logado()
        
    else:
        messagebox.showwarning('Erro', 'Nome ou senha incorretos')
        


#janela
janela = Tk()
janela.title('Login')
janela.geometry("620x600")
janela.configure(background=cor3)
janela.resizable(width=FALSE, height=FALSE)

#divisões
frame_cima = Frame(janela, width=620, height=100, bg=cor3, relief='flat')
frame_cima.grid(row=0, column=0,pady=1,padx=0,sticky=NSEW)

frame_baixo = Frame(janela, width=620, height=501, bg=cor3, relief='flat')
frame_baixo.grid(row=1, column=0,pady=1,padx=0,sticky=NSEW)

#criando o frame de cima

l_nome = Label(frame_cima, text="LOGIN", anchor=NE, font=("Helvetica 40  italic"), bg=cor3, fg=cor4)
l_nome.place(x=230,y=30)

l_linha = Label(frame_cima, text="", anchor=NW, font=("Helvetica 1"), bg=cor2, fg=cor4, width=550)
l_linha.place(x=28,y=90)

#criando o framde de baixo

l_nome =Label(frame_baixo, text="Nome ", anchor=NW, font=("Helvetica 20"), bg=cor3, fg=cor4)
l_nome.place(x=20, y=40)
e_nome = Entry(frame_baixo, width=45, justify="left", font=("", 15), highlightthickness=1, relief="solid")
e_nome.place(x=25,y=100)


l_senha =Label(frame_baixo, text="Senha ", anchor=NW, font=("Helvetica 20"), bg=cor3, fg=cor4)
l_senha.place(x=20, y=200)
e_senha = Entry(frame_baixo, width=45, justify="left",show='*', font=("", 15), highlightthickness=1, relief="solid")
e_senha.place(x=25,y=260)


b_entrar =Button(frame_baixo, command=verificador_acesso ,text="Entrar", width=30, height=4, font=("Helvetica 16 bold"), bg=cor2, fg=cor1, relief=RAISED, overrelief=RIDGE)
b_entrar.place(x=100, y=360)


            


janela.mainloop()
 
