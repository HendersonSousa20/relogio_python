import tkinter as tk
from tkinter import *
import os 
from time import strftime

root = tk.Tk()
root.title("Seu relogio")
root.geometry("600x320")
root.maxsize(600, 320)
root.minsize(600, 320)
root.configure (background="#ffff33")

def get_saudacao():
   nome_usuario = os.getlogin()
   saudacao.config ( text= "ola,  " + nome_usuario)
def get_data():
   data_atual = strftime (' %a, %d %b %y')
   data.config( text= data_atual)

def get_horas():
   hora_atual = strftime('%H:%M:%S')
   horas.config(text=hora_atual)
   horas.after(1000, get_horas)

tela = tk.Canvas(root, width=600, height=60 , bg="#ffff33" , bd=0, highlightthickness=0, relief='ridge' )
tela.pack()  

saudacao = Label(root, bg="#ffff33" , fg='#000000', font=('montserrat', 16))
saudacao.pack()

data= Label(root, bg="#ffff33" , fg='#000000', font=('montserrat', 14))
data.pack(pady=2)

horas = Label(root, bg="#ffff33" , fg= '#000000', font=('montserrat', 64  , 'bold'))
horas.pack(pady=2)
get_saudacao()
get_data()
get_horas()

root.mainloop()