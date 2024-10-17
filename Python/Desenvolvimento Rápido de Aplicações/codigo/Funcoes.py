import sqlite3
from tkinter import *
from tkinter import messagebox
from aspose.pdf.text import FontStyles, TextFragment
from aspose.pdf import Document, PageInfo

class Funcs:
    def ConectarBD(self):
        self.conectar = sqlite3.connect("clientes.bd")
        self.cursor = self.conectar.cursor()

    def DesconectarBD(self):
        self.conectar.close()

    def MontarTabelas(self):
        self.ConectarBD(); print("Conectando banco de dados")
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_nome CHAR(40) NOT NULL,
                user_telefone INTEGER(20),
                user_cidade CHAR(40)
            );
        """)

        self.conectar.commit(); print("Banco de dados conectado!")
        self.DesconectarBD(); print("Desconectando do banco de dados!")

    def Variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.cidade = self.cidade_entry.get()

    def Limpar(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.cidade_entry.delete(0, END)

    def Adicionar(self):
        self.Variaveis()
        self.ConectarBD()
        self.msg = messagebox.askyesno(title="", message="Deseja criar novo cliente?")

        if self.msg == NO:
            self.msg = exit
        elif self.nome == "":
            messagebox.showwarning(title="", message="O cadastro do cliente deve conter informações.")
        elif self.msg == YES:
            self.cursor.execute("""
                INSERT INTO clientes (user_nome, user_telefone, user_cidade)
                VALUES (?, ?, ?) """, (self.nome, self.telefone, self.cidade))
            messagebox.showinfo(title="", message="Cliente cadastado com sucesso!")

        self.conectar.commit()
        self.DesconectarBD()
        self.SelectLista()
        self.Limpar()

    def SelectLista(self):
        self.listbox.delete(*self.listbox.get_children())
        self.ConectarBD()
        lista = self.cursor.execute(""" 
            SELECT user_id, user_nome, user_telefone, user_cidade FROM clientes
            ORDER BY user_id, user_nome ASC; """)
        for i in lista:
            self.listbox.insert("", END, values=i)
        self.DesconectarBD()

    def DuploClique(self, event):
        self.Limpar()
        self.listbox.selection()
        for n in self.listbox.selection():
            col1, col2, col3, col4 = self.listbox.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.telefone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)
            print(self.nome_entry.get())

    def Alterar(self):
        self.Variaveis()
        self.ConectarBD()
        self.msg = messagebox.askyesno(title="", message="Deseja alterar o Cliente?")

        if self.msg == NO:
            self.msg = exit
        elif self.nome == "":
            messagebox.showwarning(title="", message="É necessário informações para alterar o cliente.")
        else:
            self.cursor.execute("""
                UPDATE clientes SET user_nome = ?, user_telefone = ?, user_cidade = ? 
                WHERE user_id = ?; """, (self.nome, self.telefone, self.cidade, self.codigo,))

        self.conectar.commit()
        self.DesconectarBD()
        self.Limpar()
        self.SelectLista()

    def Apagar(self):
        self.Variaveis()
        self.ConectarBD()
        self.msg = messagebox.askyesno(title="", message="Deseja apagar o Cliente?")

        if self.msg == NO:
            self.msg = exit
        elif self.nome == "":
            messagebox.showwarning(title="", message="É necessário informações para apagar o cliente.")
        else:
            self.cursor.execute(""" DELETE FROM clientes WHERE user_id = ?; """, (self.codigo,))

        self.conectar.commit()
        self.DesconectarBD()
        self.Limpar()
        self.SelectLista()

    def Buscar(self):
        self.ConectarBD()
        self.listbox.delete(*self.listbox.get_children())
        self.nome_entry.insert(END, '%')
        nome = self.nome_entry.get()
        self.cursor.execute("""
            SELECT user_id, user_nome, user_telefone, user_cidade FROM clientes 
            WHERE user_nome LIKE '%s' ORDER BY user_id ,user_nome ASC """ % nome)
        buscar = self.cursor.fetchall()
        for i in buscar:
            self.listbox.insert("", END, values=i)
        self.Limpar()
        self.DesconectarBD()


    def write_all_file_PDF(self):
        self.ConectarBD()
        self.cursor.execute('SELECT user_id, user_nome, user_telefone, user_cidade FROM clientes')
        all_users_array = self.cursor.fetchall()

        document = Document()

        page = document.pages.add()

        margin_left_right = 36
        margin_bottom_top = 56

        page_info = PageInfo()
        page_info.margin.left = margin_left_right
        page_info.margin.right = margin_left_right
        page_info.margin.top = margin_bottom_top
        page_info.margin.bottom = margin_bottom_top
        page.page_info = page_info

        title_text_str = 'Ficha dos usuários:\n\n'
        title_text_fragment = TextFragment(title_text_str)
        title_text_fragment.text_state.font_size = 18
        title_text_fragment.text_state.font_style = FontStyles.BOLD
        page.paragraphs.add(title_text_fragment)

        i = 0
        for user in all_users_array:
            content_text_str = (f'ID: {user[0]}\n'
                        f'Nome: {user[1]}\n'
                        f'Telefone: {user[2]}\n'
                        f'Cidade: {user[3]}\n\n')
            content_text_fragment = TextFragment(content_text_str)
            content_text_fragment.text_state.font_size = 14

            if i >= 7:
                page = document.pages.add()

                page_info = PageInfo()
                page_info.margin.left = margin_left_right
                page_info.margin.right = margin_left_right
                page_info.margin.top = margin_bottom_top
                page_info.margin.bottom = margin_bottom_top

                page.page_info = page_info

                page.paragraphs.add(content_text_fragment)
                i = 0
            else:
                page.paragraphs.add(content_text_fragment)
            i += 1

        document.save('./pdf/registros.pdf')
        messagebox.showinfo(title='Salvo com sucesso!', message='Arquivo PDF foi salvo e está localizado em '
                                                                './pdf/registros.pdf')


    def write_one_file_PDF(self):
        if not self.codigo_entry.get().strip():
            return messagebox.showwarning(title='Opção inválida!', message='Clique duas vezes em um cliente para '
                                                                            'poder imprimir seus dados')

        document = Document()

        page = document.pages.add()

        margin_left_right = 36  # 0,5 polegadas
        margin_bottom_top = 56  # 1 polegada

        page_info = PageInfo()
        page_info.margin.left = margin_left_right
        page_info.margin.right = margin_left_right
        page_info.margin.top = margin_bottom_top
        page_info.margin.bottom = margin_bottom_top
        page.page_info = page_info

        title_text_str = 'Ficha do Usuário:\n\n'
        title_text_fragment = TextFragment(title_text_str)
        title_text_fragment.text_state.font_size = 18
        title_text_fragment.text_state.font_style = FontStyles.BOLD
        page.paragraphs.add(title_text_fragment)

        content_text_str = (f'ID: {self.codigo_entry.get()}\n'
                        f'Nome: {self.nome_entry.get()}\n'
                        f'Telefone: {self.telefone_entry.get()}\n'
                        f'Cidade: {self.cidade_entry.get()}')

        content_text_fragment = TextFragment(content_text_str)
        content_text_fragment.text_state.font_size = 14
        page.paragraphs.add(content_text_fragment)

        document.save('./pdf/' + self.nome_entry.get().replace(' ', '_') + '.pdf')

        messagebox.showinfo(title='Salvo com sucesso!',
                            message='Arquivo PDF foi salvo, localizado em ./pdf/' + self.nome_entry.get().replace(' ', '_') + '.pdf')