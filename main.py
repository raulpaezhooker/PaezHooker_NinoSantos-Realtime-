from Tkinter import *
from Tkinter import Tk
from tkFileDialog import askopenfilename
import threading
from play import Play

def main():

    #Creacion de la ventana

    ventana = Tk()
    ventana.title('REAL TIME SOUND ADDITION')
    ventana.geometry("400x200")
    imageL=PhotoImage(file="realtime.gif")
    lblImagen=Label(ventana,image=imageL).place(x=0,y=0)
    #Cargar achivo1
    def archivo():

        global Audio1
        Audio1= askopenfilename()

    #Cargar archivo2
    def archivo2():

        global Audio2
        Audio2= askopenfilename()

    #Cargar archivo3
    def archivo3():

        global Audio3
        Audio3= askopenfilename()

    def archivo4():

        global Audio4
        Audio4= askopenfilename()

    def reproducir():

        global audio, audio2, audio3, audio4

        s=threading.Thread(target=suma, args=(audio,))
        t=threading.Thread(target=suma, args=(audio2,))
        u=threading.Thread(target=suma, args=(audio3,))
        v=threading.Thread(target=suma, args=(audio4,))
        s.start()
        t.start()
        u.start()
        v.start()


    def suma(nombre):

        sonido=Play(1024)
        Datos=sonido.open(nombre)
        sonido.start(Datos[0],Datos[1],Datos[2])
        sonido.play(Datos[3])
        sonido.closed()



    b1 = Button(ventana,text="FILE #1",command = archivo ,font=("Arial Black", 14),width=10).place(x=80,y=50)
    b2 = Button(ventana,text="FILE #2",command = archivo2,font=("Arial Black", 14),width=10).place(x=200,y=50)
    b3 = Button(ventana,text="FILE #3",command = archivo3,font=("Arial Black", 14),width=10).place(x=80,y=80)
    b4 = Button(ventana,text="FILE #4",command = archivo4,font=("Arial Black", 14),width=10).place(x=200,y=80)
    b5 = Button(ventana,text="ADDITION",command =reproducir,font=("Arial Black", 14),width=10).place(x=140,y=110)

    ventana.mainloop()

if __name__=="__main__":
    main()