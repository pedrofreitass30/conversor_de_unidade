from tkinter import *
from logica import calcular
def executar_calculo():
    valor_digitado = entrada1.get()      # pega da Entry
    resultado = calcular(valor_digitado) # chama função da lógica
    resultadotxt.config(text=resultado)

def chamar_janela():
    global entrada1, resultadotxt
    janela =  Tk()
    janela.title('Conversor de Unidades')
    janela.geometry('300x500')

    celsius = Label(janela, text='Digite a o valor em celsisus: ')
    celsius.pack()

    entrada1 = Entry(janela)
    entrada1.pack()

    fahrenheit = Label(janela, text='Valor em fahrenheit: ')
    fahrenheit.pack()

    resultadotxt = Label(janela, text='')
    resultadotxt.pack()

    botao = Button(janela, text='CALCULAR', command=executar_calculo)
    botao.pack()
    
    janela.mainloop()