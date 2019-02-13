from tkinter import*
import random
import time;

root = Tk()
root.geometry("1600x800+0+0")
root.title("RESTAURANTE SISTEMA DE GERENCIAMENTO ")
text_input = StringVar()
operador =""
tops = Frame(root,width= 1600, height= 50, bg="powder blue", relief=SUNKEN)
tops.pack(side=TOP)

f1 = Frame(root, width= 800, height= 700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width= 300, height= 700,  relief=SUNKEN)
f2.pack(side=RIGHT)
#====================================Time==========================================================================================
localtime =time.asctime(time.localtime(time.time()))
#===============================================Info===============================================================================
lblInfo = Label(tops, font=('arial',50,'bold'), text="Restaurante Sistema de Gerenciamento", fg="steel blue", bd=10, anchor="w")
lblInfo.grid(row=0,column=0)
lblInfo = Label(tops, font=('arial',20,'bold'), text=localtime, fg="steel blue", bd=10, anchor="w")
lblInfo.grid(row=1,column=0)
#================================================Calculadora=====================================================================
def btnClick(numeros):
    global operador
    operador = operador + str(numeros)
    text_input.set(operador)

def limparDisplay():
    global operador
    operador =""
    text_input.set("")

def equacao():
    global operador
    igual = str(eval(operador))
    text_input.set(igual)
    operador=""

def ref():
    x = random.randint(10908, 500876)
    randomRef = str(x)
    rand.set(randomRef)

def qExit():
    root.destroy()


def reset():
        rand.set("")
        empanado.set("")
        cafeExpres.set("")
        xBurger.set("")
        filePeixe.set("")
        torta.set("")
        pratoDia.set("")
        porcao.set("")
        refrigerante.set("")
        sobremesa.set("")
        subTotal.set("")
        drinks.set("")
        taxa.set("")
        servico.set("")
        custo.set("")
        desconto.set("")

#=====================================================================================================
txtDisplay = Entry(f2, font=('arial',20,'bold'),
                   textvariable= text_input, bd= 30,insertwidth= 4, bg="powder blue", justify='right')
txtDisplay.grid(columnspan=4)
#==============================================================================================
btn7 = Button(f2, padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
              text='7',bg="powder blue",command=lambda: btnClick(7)).grid(row=2,column=0)
btn8 = Button(f2, padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
              text='8',bg="powder blue",command=lambda: btnClick(8)).grid(row=2,column=1)
btn9 = Button(f2, padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
              text='9',bg="powder blue",command=lambda: btnClick(9)).grid(row=2,column=2)
Addition= Button(f2, padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
              text='+',bg="powder blue",command=lambda: btnClick("+")).grid(row=2,column=3)
#==========================================================================================
btn4 = Button(f2, padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
              text='4',bg="powder blue",command=lambda: btnClick(4)).grid(row=3,column=0)
btn5 = Button(f2, padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
              text='5',bg="powder blue",command=lambda: btnClick(5)).grid(row=3,column=1)
btn6 = Button(f2, padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
              text='6',bg="powder blue",command=lambda: btnClick(6)).grid(row=3,column=2)
Multiplica= Button(f2, padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
              text='*',bg="powder blue",command=lambda: btnClick("*")).grid(row=3,column=3)
#==========================================================================================
btn1 = Button(f2, padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
              text='1',bg="powder blue",command=lambda: btnClick(1)).grid(row=4,column=0)
btn2 = Button(f2, padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
              text='2',bg="powder blue",command=lambda: btnClick(2)).grid(row=4,column=1)
btn3 = Button(f2, padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
              text='3',bg="powder blue",command=lambda: btnClick(3)).grid(row=4,column=2)
Subtrai= Button(f2, padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
              text='-',bg="powder blue",command=lambda: btnClick("-")).grid(row=4,column=3)
#=============================================================================================
btn0 = Button(f2, padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
              text='0',bg="powder blue",command=lambda: btnClick(0)).grid(row=5,column=0)
btnLimpar = Button(f2, padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
              text='c',bg="powder blue", command=limparDisplay).grid(row=5,column=1)
btnIgual = Button(f2, padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
              text='=',bg="powder blue", command=equacao).grid(row=5,column=2)
Divisao= Button(f2, padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
              text='/',bg="powder blue",command=lambda: btnClick("/")).grid(row=5,column=3)
#==============================================variáveis====================================================
rand= StringVar()
empanado = StringVar()
cafeExpres = StringVar()
xBurger = StringVar()
filePeixe = StringVar()
torta = StringVar()
pratoDia = StringVar()
porcao =StringVar()
refrigerante = StringVar()
sobremesa = StringVar()
subTotal = StringVar()
drinks = StringVar()
taxa = StringVar()
servico = StringVar()
custo = StringVar()
desconto = StringVar()





#=====================================================Restaurante info 1===================================================
lblReferencia = Label(f1,font=('arial',16,'bold'),text="Referência",bd=16, anchor='w').grid(row=0,column=0)
txtreferencia =Entry(f1, font=('arial',16,'bold'),textvariable=rand, bd=10, insertwidth=4,
bg="powder blue", justify='right').grid(row=0,column=1)

lblEmpanado = Label(f1,font=('arial',16,'bold'),text="Empanado",bd=16, anchor='w').grid(row=1,column=0)
txtEmpanado =Entry(f1, font=('arial',16,'bold'),textvariable=empanado, bd=10, insertwidth=4,
bg="powder blue", justify='right').grid(row=1,column=1)

lblTorta = Label(f1,font=('arial',16,'bold'),text="Torta",bd=16, anchor='w').grid(row=3,column=0)
txtTorta =Entry(f1, font=('arial',16,'bold'),textvariable=torta, bd=10, insertwidth=4,
bg="powder blue", justify='right').grid(row=3,column=1)

lblXburger = Label(f1,font=('arial',16,'bold'),text="X-Burger",bd=16, anchor='w').grid(row=4,column=0)
txtXburger =Entry(f1, font=('arial',16,'bold'),textvariable=xBurger, bd=10, insertwidth=4,
bg="powder blue", justify='right').grid(row=4,column=1)

lblFileP = Label(f1,font=('arial',16,'bold'),text="Filé de peixe",bd=16, anchor='w').grid(row=5,column=0)
txtFileP =Entry(f1, font=('arial',16,'bold'),textvariable=filePeixe, bd=10, insertwidth=4,
bg="powder blue", justify='right').grid(row=5,column=1)

lblPratoD = Label(f1,font=('arial',16,'bold'),text="Prato do dia",bd=16, anchor='w').grid(row=6,column=0)
txtPratoD =Entry(f1, font=('arial',16,'bold'),textvariable=pratoDia, bd=10, insertwidth=4,
bg="powder blue", justify='right').grid(row=6,column=1)

lblPorcao = Label(f1,font=('arial',16,'bold'),text="Porções",bd=16, anchor='w').grid(row=7,column=0)
txtPorcao =Entry(f1, font=('arial',16,'bold'),textvariable=porcao, bd=10, insertwidth=4,
bg="powder blue", justify='right').grid(row=7,column=1)


lblSobremesa = Label(f1,font=('arial',16,'bold'),text="Sobremesa",bd=16, anchor='w').grid(row=8,column=0)
txtSobremesa =Entry(f1, font=('arial',16,'bold'),textvariable=sobremesa, bd=10, insertwidth=4,
bg="powder blue", justify='right').grid(row=8,column=1)
#=================================================Restaurante info 2==============================================
lblDrinks = Label(f1,font=('arial',16,'bold'),text="Drinks",bd=16, anchor='w').grid(row=0,column=2)
txtDrinks =Entry(f1, font=('arial',16,'bold'),textvariable=drinks, bd=10, insertwidth=4,
bg="#ffffff", justify='right').grid(row=0,column=3)

lblCafe = Label(f1,font=('arial',16,'bold'),text="Café -Expresso",bd=16, anchor='w').grid(row=1,column=2)
txtCafe =Entry(f1, font=('arial',16,'bold'),textvariable=cafeExpres, bd=10, insertwidth=4,
bg="#ffffff", justify='right').grid(row=1,column=3)

lblRefrig = Label(f1,font=('arial',16,'bold'),text="Refrigerantes",bd=16, anchor='w').grid(row=3,column=2)
txtRefrig=Entry(f1, font=('arial',16,'bold'),textvariable=refrigerante, bd=10, insertwidth=4,
bg="#ffffff", justify='right').grid(row=3,column=3)

lblTaxa = Label(f1,font=('arial',16,'bold'),text="Taxa",bd=16, anchor='w').grid(row=4,column=2)
txtTaxa =Entry(f1, font=('arial',16,'bold'),textvariable=taxa, bd=10, insertwidth=4,
bg="#ffffff", justify='right').grid(row=4,column=3)

lblServ = Label(f1,font=('arial',16,'bold'),text="Serviço",bd=16, anchor='w').grid(row=5,column=2)
txtServ =Entry(f1, font=('arial',16,'bold'),textvariable=servico, bd=10, insertwidth=4,
bg="#ffffff", justify='right').grid(row=5,column=3)

lblSubT = Label(f1,font=('arial',16,'bold'),text="Sub-Total",bd=16, anchor='w').grid(row=6,column=2)
txtSubT =Entry(f1, font=('arial',16,'bold'),textvariable=subTotal, bd=10, insertwidth=4,
bg="#ffffff", justify='right').grid(row=6,column=3)

lblCusto = Label(f1,font=('arial',16,'bold'),text="Custo",bd=16, anchor='w').grid(row=7,column=2)
txtCusto =Entry(f1, font=('arial',16,'bold'),textvariable=custo, bd=10, insertwidth=4,
bg="#ffffff", justify='right').grid(row=7,column=3)

lblDesconto = Label(f1,font=('arial',16,'bold'),text="Desconto",bd=16, anchor='w').grid(row=8,column=2)
txtDesconyo=Entry(f1, font=('arial',16,'bold'),textvariable=desconto, bd=10, insertwidth=4,
bg="#ffffff", justify='right').grid(row=8,column=3)

btnTotal = Button(f1,font=('arial',16,'bold'), text="Total", bd=8, width= 8,bg="yellow", command=ref).grid(row=9, column=1)
btnReset = Button(f1, font=('arial',16,'bold'), text="Resetar",bd=8, width= 8, bg="green", command=reset).grid(row=9,column=2)
btnSair = Button(f1,font=('arial',16,'bold'), text="Sair", bd=8, width=8, bg="red",command=qExit).grid(row=9,column=3)
root.mainloop()