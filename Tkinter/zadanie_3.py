import tkinter
from tkinter import messagebox

root = tkinter.Tk()

root.columnconfigure(1, weight=1)  # ograniczenie przesuwania kolumn podczas przesuwania rozszezania okna


def koszt():
    try:
        dys = float(dystans.get())
        spal = float(spalanie.get())
        cena = float(cena_paliwa.get())
        wynik = (dys / 100) * spal * cena
        wynik_label.configure(text=f'Wynik: {wynik}')
    except:
        messagebox.showerror("Błędne dane", "Dane powinny być liczbami")


dystans_label = tkinter.Label(master=root, text='Podaj dystans do przejechania')
dystans_label.grid(row=0, column=0)

dystans = tkinter.Entry(master=root)
dystans.grid(row=0, column=1)

spalanie_label = tkinter.Label(master=root, text='Podaj spalanie')
spalanie_label.grid(row=1, column=0)

spalanie = tkinter.Entry(master=root)
spalanie.grid(row=1, column=1)

cena_paliwa_label = tkinter.Label(master=root, text='Podaj cene paliwa')
cena_paliwa_label.grid(row=2, column=0)

cena_paliwa = tkinter.Entry(master=root)
cena_paliwa.grid(row=2, column=1)

button = tkinter.Button(master=root, text="Koszt przejazdu", command=koszt)
button.grid(row=3, column=1)

wynik_label = tkinter.Label(master=root, text='-')
wynik_label.grid(row=4, column=1)

root.mainloop()
