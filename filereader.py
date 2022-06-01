
from tkinter import *
import glob
import subprocess
root = Tk()
root.title("File Reader ")
root.geometry("800x800")
plikiczytacz = [x for x in glob.glob("*.txt")]

try:
    pliki = StringVar()
    pliki.set(plikiczytacz[0])
    opcje = OptionMenu(root, pliki, *plikiczytacz)
    opcje.pack()
except IndexError:
    pliki = StringVar()
    pliki.set("")
    print("Tworzenie pliku...")
    f = open("plik.txt", "w")
    f.write("Plik testowy")
    


    
    
    
def wczytaj():
    print("Tekst:" + pliki.get())
    f = open(pliki.get(), "r")
    TekstPlik.delete(1.0, END)
    TekstPlik.insert(END, f.read())

def okienkoTworzenie():
    Tworzenie = Toplevel(root)
    Tworzenie.title("Stwórz plik!")
    Tworzenie.geometry("800x800")
    LabelStwórz = Label(Tworzenie, text = "Wpisz nazwę pliku:").pack()
    e = Entry(Tworzenie)
    e.pack()
    if e.get == "":
        print("Wpisz nazwę pliku!")
    TekstPlikTworzenie = Text(Tworzenie, width = 50, height = 10)
    TekstPlikTworzenie.pack()
    TekstPlikTworzenie.insert(END, "Wpisz tekst")
    def TworzeniePliku():
        f = open(str(e.get())+".txt", "w")
        f.write(TekstPlikTworzenie.get(1.0, END))
    ButtonStwórz = Button(Tworzenie, text = "Stwórz", command =TworzeniePliku)
    ButtonStwórz.pack()
    

    
def EdytujPlik():
    Edytuj = Toplevel(root)
    Edytuj.title("Edytuj plik!")
    Edytuj.geometry("800x800")
    LabelEdytuj = Label(Edytuj, text = "Edytuj plik:").pack()
    plikiczytacz = [x for x in glob.glob("*.txt")]
    pliki = StringVar()
    pliki.set(plikiczytacz[0])
    opcje = OptionMenu(Edytuj, pliki, *plikiczytacz)
    opcje.pack()
    def UruchomPlik():
        subprocess.call(["notepad.exe", pliki.get()])
        Edytuj.destroy()
    
    przyciskWczytaj = Button(Edytuj, text="Wczytaj", command=UruchomPlik)
    przyciskWczytaj.pack()
    
przycisk = Button(root, text="Wczytaj", command=wczytaj)
przycisk.pack()     
przyciskTworzenie = Button(root, text = "Stwórz plik", command =okienkoTworzenie)
przyciskTworzenie.pack()
przyciskedytuj = Button(root, text = "Edytuj plik", command = EdytujPlik).pack()
TekstPlik = Text(root, width=500, height=500)
TekstPlik.pack()


    








mainloop()