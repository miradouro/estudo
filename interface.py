""""https://www.youtube.com/watch?v=e2SKXBALAws&list=PLXik_5Br-zO_m8NaaEix1pyQOsCZM7t1h&index=2"""
from tkinter import *

app = Tk()
app.title("Eh noix!!!")

largura = 600
altura = 400
largura_tela = app.winfo_screenwidth()
altura_tela = app.winfo_screenheight()
print(largura_tela, altura_tela)
posx = largura_tela / 2 - largura / 2
posy = altura_tela / 2 - altura / 2
app.geometry("%dx%d+%d+%d" % (largura,altura, posx, posy))

#app.geometry("600x300+400+200")
app.resizable(0, 0)

#app.maxsize(600, 600)
#app.minsize(200, 200)
#app.state("zoomed")
#app.state("iconic")

app.iconbitmap("images/icon.ico")

app.configure(background="#008")

txt1 = Label(app, text="Curso interface", background="yellow", foreground="#000")
txt1.place(x=10, y=10, width=300, height=30)


def cmd():
    print("Ola mundo!")


def cmd2(msg):
    print(msg)


btn = Button(app, text="executar", command=cmd)
btn.place(x=490, y=260, width=100, height=30)
btn2 = Button(app, text="botao 2", command=lambda: cmd2("mensagem"))
btn2.place(x=490, y=220, width=100, height=30)


app.mainloop()
