import tkinter as tk
import webbrowser

def abrirgoogle():
    webbrowser.open('google.com')

def digite():
    def abrir_site():
         site = campo_digitacao.get()
         webbrowser.open(site)

    janela = tk.Toplevel(tela)
    janela.title('Abrir outro site')
    janela.geometry('400x400')
    janela.config(bg='black')

    texto2 = tk.Label(janela, text='Por favor, digite abaixo o nome do site que deseja abrir.', bg='black', fg='white')
    texto2.pack()

    campo_digitacao = tk.Entry(janela)
    campo_digitacao.pack()

    botao_abrir = tk.Button(janela, text='Abrir Google', command=abrir_site)
    botao_abrir.pack(pady=10)

tela = tk.Tk()
tela.title('Abrido de site')
tela.geometry('400x400')
tela.config(bg='black')

texto1 = tk.Label(tela, text='Bem Vindo ao meu Abrido de site', bg='black', fg='white')
texto1.pack()

botao = tk.Button(tela, text='Abrir Google', command=abrirgoogle)
botao.pack(pady=10)

botao2 = tk.Button(tela, text='Acesse outro site.', command=digite)
botao2.pack(pady=20)

tela.mainloop()