
import tkinter as tk

#Stworzenie okna programu
root = tk.Tk()
root.title('Kalkulator')
root.geometry('500x500')

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
    download_plus = int(input_second.get()) #Pobieranie wartosci z inputa jako int
    download_minus= int(input_first.get())
    result_output.config(text=f"Wynik to: {download_minus - download_plus}") #Wyswietlanie wyniku

#Funkcja do przycisku dodaj
def plus_button():
    download_minus = int(input_first.get())#Pobieranie wartosci z inputa jako int
    download_plus = int(input_second.get())
    result_output.config(text=f"Wynik to: {download_plus + download_minus}")#Wyswietlanie wyniku

#Przycisk minus
button_minus = tk.Button(root, text="-", command=minus_button, width=10, height=2)
button_minus.place(x=250, y=350)
button_minus.pack()

#Przycisk dodaj
button_dodac = tk.Button(root, text="+", command=plus_button, width=10, height=2)
button_dodac.place(x=350, y=350)
button_dodac.pack()

#Stworzenie outputa
result_output = tk.Label(root)
result_output.pack()

#Pętla programu
tk.mainloop()
