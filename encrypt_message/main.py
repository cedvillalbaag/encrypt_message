from tkinter import *
import pybase64
from tkinter import messagebox

root = Tk()
root.title('Encrypt / decrypt Message')
root.geometry('550x500')
root.iconbitmap('prueba.ico')
root.config(bg= "#9BA4B5")


colorbg = "#9BA4B5"


#Funciones
def decrypt():
    #Get text
    secret = text1.get(1.0, END)
    
    #Logic for passwd
    if e1.get() == "lima123":
        #Clear box
        text1.delete(1.0, END)

        #convert to bytes
        secret = secret.encode("ascii")

        #Convert to base64
        secret = pybase64.b64decode(secret)

        #Convert it back to ascii
        secret = secret.decode("ascii")

        text1.insert(END, secret)
    else:
        messagebox.showwarning("Incorrect!!!", "Incorrect Password, Try again")

def encrypt():
    #Get text
    secret = text1.get(1.0, END)
    
    #Logic for passwd
    if e1.get() == "lima123":
        #Clear box
        text1.delete(1.0, END)

        #convert to bytes
        secret = secret.encode("ascii")

        #Convert to base64
        secret = pybase64.b64encode(secret)

        #Convert it back to ascii
        secret = secret.decode("ascii")

        text1.insert(END, secret)
    else:
        messagebox.showwarning("Incorrect!!!", "Incorrect Password, Try again")


def clean():
    #Clean boxes
    text1.delete(1.0,END)
    e1.delete(0,END)
    text1.focus_set()

# GUI
frame1 = Frame(root)
frame1.pack()


label1 = Label(root, text="Encriptar Mensajes:", font=("Courier", 20), fg="Blue", bg=colorbg)
label1.pack(pady= 20)

label2= Label(root, text="Ingrese su contraseña asignada: ", font=("Courier"), fg="Blue", bg=colorbg)
label2.pack()

e1 = Entry(root, width= 35, show="*")
e1.pack()

e1.focus_set()

labelframe2 = LabelFrame(root, text= "Write your message", font= ("Courier", 12), bg= colorbg)
labelframe2.pack(padx=10)

text1 = Text(labelframe2, width= 57, height= 10, font=("Courier", 16), fg="#212A3E")
text1.pack(pady= 20, padx=10)

labelfr1 = LabelFrame(root, text="Opciones", font="Courier", fg="Blue", bg= colorbg)
labelfr1.pack()

btn1 = Button(labelfr1, text= "Encrypt", font=("Courier"), bg= colorbg, command= encrypt)
btn1.grid(row= 0, column= 0)

btn2 = Button(labelfr1, text="Decrypt", bg= colorbg, font=("Courier"), command= decrypt)
btn2.grid(row= 0, column= 1)

btn3 = Button(labelfr1, text="Clean", bg= colorbg, font=("Courier"), command= clean)
btn3.grid(row= 0, column= 2)


root.mainloop()