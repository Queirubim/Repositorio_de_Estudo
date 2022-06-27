from tkinter import *
from tkinter import ttk
import sqlite3 as sq

tela = Tk()

class Funcs ():
    def limpa_tela(self):
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
        self.codigo_entry.delete(0, END)
    def conecta_bd(self):
        self.conn = sq.connect("Clientes.Bd")
        self.cursor = self.conn.cursor(); print("Conectando ao banco de dados")
    def desconecta_bd(self):
        self.conn.close(); print("Desconectando ao banco de dados")
    def monta_tabelas(self):
        self.conecta_bd()
        ###Cria Tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
            cod INTEGER PRIMARY KEY,
            nome_cliente CHAR(40) NOT NULL,
            telefone INTEGER(20),
            cidade CHAR(40)
            );
        """)
        self.conn.commit(); print("Banco de dados Criado")
        self.desconecta_bd()
    def add_cliente(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.cidade = self.cidade_entry.get()
        self.telefone = self.telefone_entry.get()
        self.conecta_bd()

        self.cursor.execute("""INSERT INTO clientes (nome_cliente, telefone, cidade)
        VALUES (?, ?, ?) """,(self.nome,self.telefone, self.cidade))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()
    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes ORDER BY nome_cliente ASC; """)
        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconecta_bd()

class Application(Funcs):
    def __init__ (self):
        self.raiz = tela
        self.config()
        self.frames()
        self.widgets_frame_1()
        self.lista_frame2()
        self.monta_tabelas()
        self.select_lista()
        tela.mainloop()
    def config(self):
        self.raiz.title("Aprendendo Tkinter")
        self.raiz.configure(background="gray")
        self.raiz.geometry("700x500+788+311")
        self.raiz.maxsize(width="900", height="700")
        self.raiz.minsize(width="500", height="300")
    def frames (self):
        self.frame_1 = Frame(self.raiz, bd=4, bg='lightgray',highlightbackground='#759fe6',highlightthickness=3 )
        self.frame_1.place(relx=0.1, rely=0.05, relwidth=0.8 ,relheight=0.4 )

        self.frame_2 = Frame(self.raiz, bd=4, bg='lightgray',highlightbackground='#759fe6',highlightthickness=3 )
        self.frame_2.place(relx=0.1, rely=0.5, relwidth=0.8 ,relheight=0.4 )
    def widgets_frame_1(self):
        #Cria botão limpar
        self.bt_limpar = Button(self.frame_1,text="Limpar",bd=2, bg='#107db2',fg='white', font=('verdana',8, 'bold'), command=self.limpa_tela)
        self.bt_limpar.place(relx=0.1,rely=0.1, relwidth=0.1, relheight=0.1)

        #Cria botão buscar
        self.bt_buscar = Button(self.frame_1,text="Buscar",bd=2, bg='#107db2',fg='white', font=('verdana',8, 'bold'))
        self.bt_buscar.place(relx=0.22,rely=0.1, relwidth=0.1, relheight=0.1)

        #Cria botão novo
        self.bt_Novo = Button(self.frame_1,text="Novo",bd=2, bg='#107db2',fg='white', font=('verdana',8, 'bold'), command=self.add_cliente)
        self.bt_Novo.place(relx=0.46,rely=0.1, relwidth=0.1, relheight=0.1)

        #Cria botão alterar
        self.bt_alterar = Button(self.frame_1,text="Alterar",bd=2, bg='#107db2',fg='white', font=('verdana',8, 'bold'))
        self.bt_alterar.place(relx=0.58,rely=0.1, relwidth=0.1, relheight=0.1)

        #Cria botão apagar 
        self.bt_apagar = Button(self.frame_1,text="Apagar",bd=2, bg='#107db2',fg='white', font=('verdana',8, 'bold'))
        self.bt_apagar.place(relx=0.70,rely=0.1, relwidth=0.1, relheight=0.1)
        
        #Label e entry do codigo
        self.lb_codigo = Label(self.frame_1,text="Código", bg='lightgray', fg='#107db2')
        self.lb_codigo.place(relx= 0.68, rely=0.3,relwidth=0.1, relheight=0.1)

        self.codigo_entry = Entry(self.frame_1, fg='#107db2')
        self.codigo_entry.place(relx=0.68,rely=0.4,relwidth=0.1,relheight=0.1)

        #Label e entry do nome
        self.lb_nome = Label(self.frame_1,text="Nome",bg='lightgray', fg='#107db2')
        self.lb_nome.place(relx= 0.05, rely=0.3,relwidth=0.1)

        self.nome_entry = Entry(self.frame_1, fg='#107db2')
        self.nome_entry.place(relx=0.05,rely=0.4,relwidth=0.6)

        #Label e entry do telefone
        self.lb_telefone = Label(self.frame_1,text="Telefone",bg='lightgray', fg='#107db2')
        self.lb_telefone.place(relx= 0.05, rely=0.6,relwidth=0.1)

        self.telefone_entry = Entry(self.frame_1, fg='#107db2')
        self.telefone_entry.place(relx=0.05,rely=0.7,relwidth=0.35)

        #Label e entry da cidade
        self.lb_cidade = Label(self.frame_1,text="Cidade",bg='lightgray', fg='#107db2')
        self.lb_cidade.place(relx= 0.5, rely=0.6,relwidth=0.1,)

        self.cidade_entry = Entry(self.frame_1, fg='#107db2')
        self.cidade_entry.place(relx=0.5,rely=0.7,relwidth=0.35)
    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=3, columns=("coll1","coll2","coll3","coll4"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Codigo")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Telefone")
        self.listaCli.heading("#4", text="Cidade")

        self.listaCli.column("#0", width ="1")
        self.listaCli.column("#1", width ="50")
        self.listaCli.column("#2", width ="200")
        self.listaCli.column("#3", width ="125")
        self.listaCli.column("#4", width ="125")

        self.listaCli.place(relx=0.01,rely=0.1,relwidth=0.95,relheight=0.85)

        self.scroll = Scrollbar(self.frame_2,orient='vertical')
        self.listaCli.configure(yscroll=self.scroll.set)
        self.scroll.place(relx=0.96,rely=0.1,relwidth=0.04,relheight=0.85)
Application()