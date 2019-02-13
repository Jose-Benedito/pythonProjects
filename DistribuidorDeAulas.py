from tkinter import*
import random
import time;

root = Tk()
root.geometry("1600x800+0+0")
root.title("Distribuidor de Aulas")
top = Frame(root, width=1600, height= 20 , relief=SUNKEN)
top.pack(side=TOP)

f1 = Frame(root,bd=8, bg="steel blue", relief=SUNKEN)
f1.pack(side=TOP)
f2 = Frame(root,bd=6, bg="white", relief=SUNKEN)
f2.pack(side=BOTTOM)
painel=Frame(f2, bg="powder blue",bd=5, relief=SUNKEN)
painel.grid(row=1, column=0)

#==============================================VARIÁVEIS=================================================
professor = StringVar()
disciplina = StringVar()
numeroAulas = StringVar()
turmas = StringVar()
chbSim = StringVar()
turma = StringVar()
segunda = StringVar()
terca = StringVar()
quarta = StringVar()
quinta = StringVar()
sexta = StringVar()
text_input = StringVar()

#==============================================funções=================================================

def checar():
    pass
def inserir():
    pass
 #   nome.set(professor.get())
  #  text_input.set(professor.get())
   # print(nomes)



def limpar():
    professor.set("")
    disciplina.set("")
    numeroAulas.set("")
    
    #chbNao()
    #chbSim.set(OFF)
    #chbTipo1(FALSE)
    #chbTipo2(FALSE)
def sair():
    root.destroy()


#===================================Time=================================================================
localTime = time.asctime(time.localtime(time.time()))
#=====================================INFO================================================================
lblInfo = Label(top,font=("arial", 30, 'bold'), text="Distribuidor de Aulas",bg="powder blue", fg="red", bd=10, anchor="w")
lblInfo.grid(row=0, column=0)
lblTime = Label(top, font=("arial", 14, 'bold'), text=localTime, fg="black",bg="powder blue", bd=10, anchor="w")
lblTime.grid(row=1, column=0)
lblTime = Label(top, font=("arial", 20, 'bold'), text="Aulas", fg="black", bd=10, anchor="w")
lblTime.grid(row=2, column=0)


#=======================================INFO professores====================================================
lblProfessor = Label(painel,font=("arial", 12, 'bold'),text="Professor",bg="powder blue", bd=16, anchor="w").grid(row=0, column=0)
txtProfessor = Entry(painel,font=('arial',12,'bold'), textvariable=professor,bd=10, width=10,
                    bg="white", justify="right").grid(row=0,column=1)
lblDisciplina = Label(painel, font=('arial', 12, 'bold'), text="Disciplina",bg="powder blue", bd=16, anchor='w').grid(row=0, column=2)
txtDisciplina = Entry(painel,font=('arial', 12, 'bold'),textvariable=disciplina,bd=10, insertwidth=4,width=10,
                      bg="white", justify="right").grid(row=0, column=3)
lblNumAulas = Label(painel,font=('arial', 12, 'bold'), text= "Qtde de Aulas", bg="powder blue",bd=16, anchor='w').grid(row=0,column=4)
txtNumAulas = Entry(painel, font=('arial',12,'bold'), textvariable=numeroAulas,bd=10, width=4,
                    bg="white", justify="right").grid(row=0, column=5)
lblTurmas = Label(painel, font=('arial', 12, 'bold'), text="Turmas",bg="powder blue", bd=16, anchor='w').grid(row=0, column=6)
txtTurmas = Entry(painel,font=('arial', 12, 'bold'),textvariable=turmas,bd=10, width=4,
                      bg="white", justify="right").grid(row=0, column=7)
lblAcumulo = Label(painel,font=('arial', 12, 'bold'), text="Acumula?",bg="powder blue", bd=16, anchor='w').grid(row=1,column=0)
chbSim = Checkbutton(painel,font=('arial',12,'bold'), text='Sim',bg="powder blue").grid(row=1,column=1)
chbNao = Checkbutton(painel,font=('arial',12,'bold'),text='Não',bg="powder blue").grid(row=1,column=2)
chbTipo1 = Checkbutton(painel,font=('arial',12,'bold'),text='Estado/prefeitura',bg="powder blue").grid(row=1,column=3)
chbTipo2 = Checkbutton(painel,font=('arial',12,'bold'),text='privado',bg="powder blue").grid(row=1,column=4)

campo = Text(f2,width=145, height= 15, bd=5).grid(row=0, column=0)

#===================================================Botões===========================================================
btnInserir = Button(painel,font=('arial',12,'bold'), text="Inserir", bd=8,width=5, bg="green",command=inserir).grid(row=0, column=8,)
btnLimpar = Button(painel,font=('arial', 12,'bold'), text="Limpar", bd=8, width=5, bg="yellow",command=limpar).grid(row=0, column=9)
btnExit = Button(painel, font=('arial', 12, 'bold'), text="Sair", bd=8, width=5, bg="red", command=sair).grid(row=0,column=10)
btnPrint = Button(painel, font=('arial', 12, 'bold'), text="Print", bd=8, width=5, bg="blue", command=sair).grid(row=0,column=11)

#==================================================QUADRO DE AULAS===========================================

secund = Label(f1, font=('arial',10,'bold'), text="Seg.", width=2,bd=5,bg="steel blue").grid(row=1, column=0)
terc = Label(f1, font=('arial',10,'bold'), text="Ter",width=2,bd=5,bg="steel blue").grid(row=2, column=0)
quart = Label(f1, font=('arial',10,'bold'), text="Qua",width=2,bd=5, bg="steel blue").grid(row=3, column=0)
quint = Label(f1, font=('arial',10,'bold'), text="Qui",width=2,bd=5,bg="steel blue").grid(row=4, column=0)
sex = Label(f1, font=('arial',10,'bold'), text="Sex",width=2,bd=5,bg="steel blue").grid(row=5, column=0)

turma = Label(f1, font=('arial',10,'bold'), text= "turma 1ºA",bd=5,bg="steel blue").grid(row=0, column=1)
secund = Entry(f1, font=('arial',10,'bold'), textvariable=segunda, width=8,bd=5,bg="white").grid(row=1, column=1)
terc = Entry(f1, font=('arial',10,'bold'), textvariable=terca, width=8,bd=5,bg="white").grid(row=2, column=1)
quart = Entry(f1, font=('arial',10,'bold'), textvariable=quarta,width=8,bd=5, bg="white").grid(row=3, column=1)
quint = Entry(f1, font=('arial',10,'bold'), textvariable=quinta,width=8,bd=5,bg="white").grid(row=4, column=1)
sex = Entry(f1, font=('arial',10,'bold'), textvariable=sexta, width=8,bd=5,bg="white").grid(row=5,column=1)

turma = Label(f1, font=('arial',10,'bold'), text= "turma 1ºB",bd=5,bg="steel blue").grid(row=0, column=2)
secund = Entry(f1, font=('arial',10,'bold'), textvariable=segunda, width=8,bd=5,bg="white").grid(row=1, column=2)
terc = Entry(f1, font=('arial',10,'bold'), textvariable=terca, width=8,bd=5,bg="white").grid(row=2, column=2)
quart = Entry(f1, font=('arial',10,'bold'), textvariable=quarta, width=8,bd=5, bg="white").grid(row=3, column=2)
quint = Entry(f1, font=('arial',10,'bold'), textvariable=quinta,width=8,bd=5,bg="white").grid(row=4, column=2)
sex = Entry(f1, font=('arial',10,'bold'), textvariable=sexta, width=8,bd=5,bg="white").grid(row=5,column=2)

turma = Label(f1, font=('arial',10,'bold'), text= "turma 1ºC",bd=5,bg="steel blue").grid(row=0, column=3)
secund = Entry(f1, font=('arial',10,'bold'), textvariable=segunda, width=8,bd=5,bg="white").grid(row=1, column=3)
terc = Entry(f1, font=('arial',10,'bold'), textvariable=terca, width=8,bd=5,bg="white").grid(row=2, column=3)
quart = Entry(f1, font=('arial',10,'bold'), textvariable=quarta, width=8,bd=5, bg="white").grid(row=3, column=3)
quint = Entry(f1, font=('arial',10,'bold'), textvariable=quinta,width=8,bd=5,bg="white").grid(row=4, column=3)
sex = Entry(f1, font=('arial',10,'bold'), textvariable=sexta, width=8,bd=5,bg="white").grid(row=5,column=3)

turma = Label(f1, font=('arial',10,'bold'), text= "turma 1ºD",bd=5,bg="steel blue").grid(row=0, column=4)
secund = Entry(f1, font=('arial',10,'bold'), textvariable=segunda, width=8,bd=5,bg="white").grid(row=1, column=4)
terc = Entry(f1, font=('arial',10,'bold'), textvariable=terca, width=8,bd=5,bg="white").grid(row=2, column=4)
quart = Entry(f1, font=('arial',10,'bold'), textvariable=quarta, width=8,bd=5, bg="white").grid(row=3, column=4)
quint = Entry(f1, font=('arial',10,'bold'), textvariable=quinta, width=8,bd=5,bg="white").grid(row=4, column=4)
sex = Entry(f1, font=('arial',10,'bold'), textvariable=sexta, width=8,bd=5,bg="white").grid(row=5,column=4)

turma = Label(f1, font=('arial',10,'bold'), text= "turma 1ºE",bd=5,bg="steel blue").grid(row=0, column=5)
secund = Entry(f1, font=('arial',10,'bold'), textvariable=segunda, width=8,bd=5,bg="white").grid(row=1, column=5)
terc = Entry(f1, font=('arial',10,'bold'), textvariable=terca, width=8,bd=5,bg="white").grid(row=2, column=5)
quart = Entry(f1, font=('arial',10,'bold'), textvariable=quarta, width=8,bd=5, bg="white").grid(row=3, column=5)
quint = Entry(f1, font=('arial',10,'bold'), textvariable=quinta, width=8,bd=5,bg="white").grid(row=4, column=5)
sex = Entry(f1, font=('arial',10,'bold'), textvariable=sexta, width=8,bd=5,bg="white").grid(row=5,column=5)

turma = Label(f1, font=('arial',10,'bold'), text= "turma 1ºF",bd=5,bg="steel blue").grid(row=0, column=6)
secund = Entry(f1, font=('arial',10,'bold'), textvariable=segunda, width=8,bd=5,bg="white").grid(row=1, column=6)
terc = Entry(f1, font=('arial',10,'bold'), textvariable=terca, width=8,bd=5,bg="white").grid(row=2, column=6)
quart = Entry(f1, font=('arial',10,'bold'), textvariable=quarta, width=8,bd=5, bg="white").grid(row=3, column=6)
quint = Entry(f1, font=('arial',10,'bold'), textvariable=quinta, width=8,bd=5,bg="white").grid(row=4, column=6)
sex = Entry(f1, font=('arial',10,'bold'), textvariable=sexta, width=8,bd=5,bg="white").grid(row=5,column=6)


turma = Label(f1, font=('arial',10,'bold'), text= "turma 1ºG",bd=5,bg="steel blue").grid(row=0, column=7)
secund = Entry(f1, font=('arial',10,'bold'), textvariable=segunda, width=8,bd=5,bg="white").grid(row=1, column=7)
terc = Entry(f1, font=('arial',10,'bold'), textvariable=terca, width=8,bd=5,bg="white").grid(row=2, column=7)
quart = Entry(f1, font=('arial',10,'bold'), textvariable=quarta, width=8,bd=5, bg="white").grid(row=3, column=7)
quint = Entry(f1, font=('arial',10,'bold'), textvariable=quinta, width=8,bd=5,bg="white").grid(row=4, column=7)
sex = Entry(f1, font=('arial',10,'bold'), textvariable=sexta, width=8,bd=5,bg="white").grid(row=5,column=7)

turma = Label(f1, font=('arial',10,'bold'), text= "turma 1H",bd=5,bg="steel blue").grid(row=0, column=8)
secund = Entry(f1, font=('arial',10,'bold'), textvariable=segunda, width=8,bd=5,bg="white").grid(row=1, column=8)
terc = Entry(f1, font=('arial',10,'bold'), textvariable=terca, width=8,bd=5,bg="white").grid(row=2, column=8)
quart = Entry(f1, font=('arial',10,'bold'), textvariable=quarta, width=8,bd=5, bg="white").grid(row=3, column=8)
quint = Entry(f1, font=('arial',10,'bold'), textvariable=quinta, width=8,bd=5,bg="white").grid(row=4, column=8)
sex = Entry(f1, font=('arial',10,'bold'), textvariable=sexta, width=8,bd=5,bg="white").grid(row=5,column=8)

turma = Label(f1, font=('arial',10,'bold'), text= "turma A",bd=5,bg="steel blue").grid(row=0, column=9)
secund = Entry(f1, font=('arial',10,'bold'), textvariable=segunda, width=8,bd=5,bg="white").grid(row=1, column=9)
terc = Entry(f1, font=('arial',10,'bold'), textvariable=terca, width=8,bd=5,bg="white").grid(row=2, column=9)
quart = Entry(f1, font=('arial',10,'bold'), textvariable=quarta, width=8,bd=5, bg="white").grid(row=3, column=9)
quint = Entry(f1, font=('arial',10,'bold'), textvariable=quinta, width=8,bd=5,bg="white").grid(row=4, column=9)
sex = Entry(f1, font=('arial',10,'bold'), textvariable=sexta, width=8,bd=5,bg="white").grid(row=5,column=9)

turma = Label(f1, font=('arial',10,'bold'), text= "turma B",bd=5,bg="steel blue").grid(row=0, column=10)
secund = Entry(f1, font=('arial',10,'bold'), textvariable=segunda, width=8,bd=5,bg="white").grid(row=1, column=10)
terc = Entry(f1, font=('arial',10,'bold'), textvariable=terca, width=8,bd=5,bg="white").grid(row=2, column=10)
quart = Entry(f1, font=('arial',10,'bold'), textvariable=quarta, width=8,bd=5, bg="white").grid(row=3, column=10)
quint = Entry(f1, font=('arial',10,'bold'), textvariable=quinta, width=8,bd=5,bg="white").grid(row=4, column=10)
sex = Entry(f1, font=('arial',10,'bold'), textvariable=sexta, width=8,bd=5,bg="white").grid(row=5,column=10)

turma = Label(f1, font=('arial',10,'bold'), text= "turma C",bd=5,bg="steel blue").grid(row=0, column=11)
secund = Entry(f1, font=('arial',10,'bold'), textvariable=segunda, width=8,bd=5,bg="white").grid(row=1, column=11)
terc = Entry(f1, font=('arial',10,'bold'), textvariable=terca, width=8,bd=5,bg="white").grid(row=2, column=11)
quart = Entry(f1, font=('arial',10,'bold'), textvariable=quarta, width=8,bd=5, bg="white").grid(row=3, column=11)
quint = Entry(f1, font=('arial',10,'bold'), textvariable=quinta, width=8,bd=5,bg="white").grid(row=4, column=11)
sex = Entry(f1, font=('arial',10,'bold'), textvariable=sexta, width=8,bd=5,bg="white").grid(row=5,column=11)

turma = Label(f1, font=('arial',10,'bold'), text= "turma D",bd=5,bg="steel blue").grid(row=0, column=12)
secund = Entry(f1, font=('arial',10,'bold'), textvariable=segunda, width=8,bd=5,bg="white").grid(row=1, column=12)
terc = Entry(f1, font=('arial',10,'bold'), textvariable=terca, width=8,bd=5,bg="white").grid(row=2, column=12)
quart = Entry(f1, font=('arial',10,'bold'), textvariable=quarta, width=8,bd=5, bg="white").grid(row=3, column=12)
quint = Entry(f1, font=('arial',10,'bold'), textvariable=quinta, width=8,bd=5,bg="white").grid(row=4, column=12)
sex = Entry(f1, font=('arial',10,'bold'), textvariable=sexta, width=8,bd=5,bg="white").grid(row=5,column=12)

turma = Label(f1, font=('arial',10,'bold'), text= "turma E",bd=5,bg="steel blue").grid(row=0, column=13)
secund = Entry(f1, font=('arial',10,'bold'), textvariable=segunda, width=8,bd=5,bg="white").grid(row=1, column=13)
terc = Entry(f1, font=('arial',10,'bold'), textvariable=terca, width=8,bd=5,bg="white").grid(row=2, column=13)
quart = Entry(f1, font=('arial',10,'bold'), textvariable=quarta, width=8,bd=5, bg="white").grid(row=3, column=13)
quint = Entry(f1, font=('arial',10,'bold'), textvariable=quinta, width=8,bd=5,bg="white").grid(row=4, column=13)
sex = Entry(f1, font=('arial',10,'bold'), textvariable=sexta,  width=8,bd=5,bg="white").grid(row=5,column=13)

turma = Label(f1, font=('arial',10,'bold'), text= "turma F",bd=5,bg="steel blue").grid(row=0, column=14)
secund = Entry(f1, font=('arial',10,'bold'), textvariable=segunda, width=8,bd=5,bg="white").grid(row=1, column=14)
terc = Entry(f1, font=('arial',10,'bold'), textvariable=terca, width=8,bd=5,bg="white").grid(row=2, column=14)
quart = Entry(f1, font=('arial',10,'bold'), textvariable=quarta, width=8,bd=5, bg="white").grid(row=3, column=14)
quint = Entry(f1, font=('arial',10,'bold'), textvariable=quinta, width=8,bd=5,bg="white").grid(row=4, column=14)
sex = Entry(f1, font=('arial',10,'bold'), textvariable=sexta, width=8,bd=5,bg="white").grid(row=5,column=14)

turma = Label(f1, font=('arial',10,'bold'), text= "turma G",bd=5,bg="steel blue").grid(row=0, column=15)
secund = Entry(f1, font=('arial',10,'bold'), textvariable=segunda, width=8,bd=5,bg="white").grid(row=1, column=15)
terc = Entry(f1, font=('arial',10,'bold'), textvariable=terca, width=8,bd=5,bg="white").grid(row=2, column=15)
quart = Entry(f1, font=('arial',10,'bold'), textvariable=quarta, width=8,bd=5, bg="white").grid(row=3, column=15)
quint = Entry(f1, font=('arial',10,'bold'), textvariable=quinta, width=8,bd=5,bg="white").grid(row=4, column=15)
sex = Entry(f1, font=('arial',10,'bold'), textvariable=sexta, width=8,bd=5,bg="white").grid(row=5,column=15)

turma = Label(f1, font=('arial',10,'bold'), text= "turma H",bd=5,bg="steel blue").grid(row=0, column=16)
secund = Entry(f1, font=('arial',10,'bold'), textvariable=segunda, width=8,bd=5,bg="white").grid(row=1, column=16)
terc = Entry(f1, font=('arial',10,'bold'), textvariable=terca, width=8,bd=5,bg="white").grid(row=2, column=16)
quart = Entry(f1, font=('arial',10,'bold'), textvariable=quarta, width=8,bd=5, bg="white").grid(row=3, column=16)
quint = Entry(f1, font=('arial',10,'bold'), textvariable=quinta, width=8,bd=5,bg="white").grid(row=4, column=16)
sex = Entry(f1, font=('arial',10,'bold'), textvariable=sexta, width=8,bd=5, bg="white").grid(row=5, column=16)


root.mainloop()