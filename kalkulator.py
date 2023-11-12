import math
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


#Stworzenie okna programu
root = tk.Tk()
root.title('Kalkulator')
root.geometry('800x800')

#Favicon
ico = Image.open('favicon.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)


#Stworzenie napisu
input_first_label = tk.Label(root, text='Write first number:', font=('Arial', 16))
input_first_label.pack()
#Stworzenie inputa
input_first = tk.Entry(root)
input_first.pack()

#Stworzenie napisu
input_second_label = tk.Label(root, text='Write second number', font=('Arial', 16))
input_second_label.pack()
#Stworzenie inputa
input_second = tk.Entry(root)
input_second.pack()

#Funkcja do przycisku minus
def minus_button():
    try:
        download_plus = int(input_second.get()) #Pobieranie wartosci z inputa jako int
        download_minus= int(input_first.get())
        result_output.config(text=f"Wynik to: {download_minus - download_plus}") #Wyswietlanie wyniku
    except:
        result_output.config(text='Error')

#Funkcja do przycisku dodaj
def plus_button():
    try:
        download_minus = int(input_first.get())#Pobieranie wartosci z inputa jako int
        download_plus = int(input_second.get())
        result_output.config(text=f"Wynik to: {download_plus + download_minus}")#Wyswietlanie wyniku
    except:
        result_output.config(text="Error")

#Funkcja do przycisku mnozenia
def mnozenie_button():
    try:
        download_plus = int(input_second.get())
        download_minus = int(input_first.get())
        result_output.config(text=f"Wynik to: {download_minus*download_plus}")
    except:
        result_output.config(text='Error')

#Funkcja do przycisku dzielenia
def dzielenie_button():
    try:
        download_plus = int(input_second.get())
        download_minus = int(input_first.get())
        result_output.config(text=f"Wynik to: {download_minus/download_plus}")
    except ZeroDivisionError as error:
        result_output.config(text=f"{error}")
        return None
    except:
        result_output.config(text="Error")
        
#Funkcja do przycisku potęgi
def potega_button():
    try:
        download_plus = int(input_second.get())
        download_minus = int(input_first.get())
        result_output.config(text=f"Wynik to: {download_minus**download_plus}")
    except:
        result_output.config("Error")
        
#Funkcja do przycisku pierwiastkowania
def pierwiastek_button():
    try:
        download_plus = int(input_first.get())
        download_minus = int(input_second.get())
        result_output.config(text=f"Wynik to: {math.pow(download_plus, 1/download_minus)}")
    except:
        result_output.config("Error")



#Przycisk minus
button_minus = tk.Button(root, text="subtraction", command=minus_button, width=15, height=2, bg='green')
button_minus.pack(side="left", padx=10, pady=10)

#Przycisk dodaj
button_dodac = tk.Button(root, text="Adding", command=plus_button, width=15, height=2, bg='green')
button_dodac.pack(side="left", padx=10, pady=10)

#Przycisk mnożenia
button_mnozenie = tk.Button(root, text='multiplication', command=mnozenie_button, width=15, height=2, bg='green')
button_mnozenie.pack(side="left", padx=10, pady=10)

#Przycisk dzielenia
button_dzielenie = tk.Button(root, text="division", command=dzielenie_button, width=15, height=2, bg='green')
button_dzielenie.pack(side="left", padx=10, pady=10)

#Przycisk potęgi
button_potega = tk.Button(root, text="exponentiation", command=potega_button, width=15, height=2, bg='green')
button_potega.pack(side="left", padx=10, pady=10)

#Przycisk pierwiastkowania
button_pierwiastek = tk.Button(root, text="elementalization", command=pierwiastek_button, width=15, height=2, bg='green')
button_pierwiastek.pack(side="left", padx=10, pady=10)


#Stworzenie outputa
result_output = tk.Label(root, font=('Arial', 24), fg='red', bg='blue')
result_output.place(x=350, y=600)

#Pętla programu
tk.mainloop()

