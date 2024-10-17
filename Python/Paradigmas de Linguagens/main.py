from tkinter import *

class CalculadoraIMC:
    def __init__(self):
        super().__init__()

    class CalcularIMC:
        def Calculo(self, peso, altura):
            return peso / (altura ** 2)

    class GetClassificacao(CalcularIMC):
        def ClassificacaoIMC(self, imc):

            if imc < 18.5:
                return "Abaixo do Peso."
            elif imc >= 18.50 and imc <= 24.90:
                return "Peso Normal."
            elif imc >= 25.00 and imc <= 29.90:
                return "Excesso de Peso."
            elif imc >= 30.00 and imc <= 34.90:
                return "Obesidade Classe I."
            elif imc >= 35.00 and imc <= 39.90:
                return "Obesidade Classe II."
            else:
                return "Obesidade Classe III."

    class ResultadoIMC(GetClassificacao):
        def __init__(self):
            altura = float(input_altura.get())
            peso = float(input_peso.get())

            imc = self.Calculo(peso, altura)
            classificacao = self.ClassificacaoIMC(imc)

            texto_resultado.config(text=f"{imc:.2f} - {classificacao}")

janela = Tk()
janela.geometry("300x300")
janela.grid_rowconfigure(0, weight=0)
janela.grid_columnconfigure(0, weight=1)
janela.title("Calculadora IMC")

texto_altura = Label(janela, text="Informe sua altura:")
texto_altura.grid(column=0, row=0, padx=5, pady=10)

input_altura = Entry(janela)
input_altura.grid(column=0, row=1, padx=5, pady=10)

texto_peso = Label(janela, text="Informe seu peso:")
texto_peso.grid(column=0, row=2, padx=5, pady=10)

input_peso = Entry(janela)
input_peso.grid(column=0, row=3, padx=5, pady=10)

botao = Button(janela, text="Enviar", command=CalculadoraIMC.ResultadoIMC)
botao.grid(column=0, row=4, padx=5, pady=10)

texto_resultado = Label(janela, text="")
texto_resultado.grid(column=0, row=5, padx=5, pady=10)

janela.mainloop()
