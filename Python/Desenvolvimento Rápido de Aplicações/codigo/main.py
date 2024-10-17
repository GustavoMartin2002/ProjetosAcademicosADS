import tkinter as tk
from tkinter import ttk
from Funcoes import Funcs


class CadastroClientes(Funcs):
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Clientes")
        self.root.geometry("700x500")
        self.root.configure(bg="#181818")
        self.root.maxsize(width=800, height=600)
        self.root.minsize(width=700, height=500)
        self.Menu()
        self.Frame1()
        self.Frame2()
        self.MontarTabelas()
        self.SelectLista()


    def imgApp(self):
        root.iconphoto(False, tk.PhotoImage(file='ico/cliente.png'))

    def Menu(self):
        #MENU
        self.menubar = tk.Menu(self.root, )
        self.root.config(menu=self.menubar)
        self.filemenu1 = tk.Menu(self.menubar, background='black', fg='white')

        self.menubar.add_cascade(label="Opções", menu=self.filemenu1)
        self.filemenu1.add_command(label="Imprimir fichas", command=self.write_all_file_PDF)
        self.filemenu1.add_command(label="Sair", command=self.root.destroy)

    def Frame1(self):
        #LABELS/ENTRYS
        self.frame_cadastro = tk.Frame(self.root)
        self.frame_cadastro = tk.Frame(highlightcolor="grey", highlightthickness=2.5, background="#FFFFFF")
        self.frame_cadastro.pack(side="top", pady=25)
        self.frame_cadastro.place(relx=0.025, rely=0.05, relheight=0.41, relwidth=0.95)

        self.label_codigo = tk.Label(self.frame_cadastro, text="Codigo:", background="#FFFFFF", font=('verdana', 8, 'bold'))
        self.label_codigo.place(relx=0.06, rely=0.08)

        self.codigo_entry = tk.Entry(self.frame_cadastro, bd=1.50, highlightcolor="#000000", highlightthickness=2)
        self.codigo_entry["width"] = 6
        self.codigo_entry.place(relx=0.06, rely=0.18)

        self.label_nome = tk.Label(self.frame_cadastro, text="Nome:", background="#FFFFFF", font=('verdana', 8, 'bold'))
        self.label_nome.place(relx=0.06, rely=0.38)
        self.nome_entry = tk.Entry(self.frame_cadastro, bd=1.50, highlightcolor="#000000", highlightthickness=2)
        self.nome_entry.place(relx=0.06, rely=0.48)
        self.nome_entry["width"] = 60


        self.label_telefone = tk.Label(self.frame_cadastro, text="Telefone:", background="#FFFFFF", font=('verdana', 8, 'bold'))
        self.label_telefone.place(relx=0.06, rely=0.70)
        self.telefone_entry = tk.Entry(self.frame_cadastro, bd=1.50, highlightcolor="#000000", highlightthickness=2)
        self.telefone_entry["width"] = 25
        self.telefone_entry.place(relx=0.06, rely=0.80)

        self.label_cidade = tk.Label(self.frame_cadastro, text="Cidade:", background="#FFFFFF", font=('verdana', 8, 'bold'))
        self.label_cidade.place(relx=0.62, rely=0.70)
        self.cidade_entry = tk.Entry(self.frame_cadastro, bd=1.50, highlightcolor="#000000", highlightthickness=2)
        self.cidade_entry["width"] = 34
        self.cidade_entry.place(relx=0.62, rely=0.80)

        #BUTTONS
        self.button_limpar = tk.Button(self.frame_cadastro, text="Limpar", bg='#181818', fg='white', borderwidth=2.50, font=('verdana', 9, 'bold'), command=self.Limpar)
        self.button_limpar.place(relx=0.235, rely=0.11)

        self.button_buscar = tk.Button(self.frame_cadastro, text="Buscar", bg='#181818', fg='white', borderwidth=2.50, font=('verdana', 9, 'bold'), command=self.Buscar)
        self.button_buscar.place(relx=0.331, rely=0.11)

        self.button_novo = tk.Button(self.frame_cadastro, text="Novo", bg='#181818', fg='white', borderwidth=2.50, font=('verdana', 9, 'bold'), command=self.Adicionar)
        self.button_novo.place(relx=0.65, rely=0.11)

        self.button_imprimir = tk.Button(self.frame_cadastro, text="Imprimir", bg='#181818', fg='white', borderwidth=2.50, font=('verdana', 9, 'bold'), command=self.write_one_file_PDF)
        self.button_imprimir.place(relx=0.535, rely=0.11)

        self.button_alterar = tk.Button(self.frame_cadastro, text="Alterar", bg='#181818', fg='white', borderwidth=2.50, font=('verdana', 9, 'bold'), command=self.Alterar)
        self.button_alterar.place(relx=0.727, rely=0.11)

        self.button_apagar = tk.Button(self.frame_cadastro, text="Apagar", bg='#181818', fg='white', borderwidth=2.50, font=('verdana', 9, 'bold'), command=self.Apagar)
        self.button_apagar.place(relx=0.823, rely=0.11)

    def Frame2(self):
        #LISTBOX
        self.frame_listbox = tk.Frame(self.root, highlightcolor="grey", highlightthickness=2.5)
        self.frame_listbox.place(relx=0.095, rely=0.5, relheight=0.45, relwidth=0.80)

        self.listbox = ttk.Treeview(self.frame_listbox, height=3, columns=("col1", "col2", "col3", "col4"))

        self.listbox.heading("#1", text="Codigo", anchor='w')
        self.listbox.heading("#2", text="Nome", anchor='w')
        self.listbox.heading("#3", text="Telefone", anchor='w')
        self.listbox.heading("#4", text="Cidade", anchor='w')

        self.listbox.column("#0", width=1)
        self.listbox.column("#1", width=50)
        self.listbox.column("#2", width=200)
        self.listbox.column("#3", width=125)
        self.listbox.column("#4", width=125)

        self.listbox.place(relx=0.01, rely=0.070, relwidth=0.95, relheight=0.86)

        self.scrollbar = ttk.Scrollbar(self.frame_listbox, orient="vertical", command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.listbox.bind("<Double-1>", self.DuploClique)

        self.scrollbar.place(relx=0.962, rely=0, relwidth=0.04, relheight=1.0)

if __name__ == '__main__':
    root = tk.Tk()
    janela = CadastroClientes(root)
    root.mainloop()
