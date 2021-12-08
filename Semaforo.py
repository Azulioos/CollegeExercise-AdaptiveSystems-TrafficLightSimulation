from tkinter import *
import time
import random
import threading
from collections import deque


SemaforoV=False
SemaforoH=False
congestionamiento1= False
congestionamiento2= False
congestionamiento3= False
congestionamiento4= False
trafico= 0
trafico2= 0
cola1=[]
cola2=[]
cola3=[]
cola4=[]
tiempo=time.time()



raiz=Tk()
raiz.title("Ventana de pruebas")
raiz.config(bg="#79DA6B")
raiz.resizable(False, False)
raiz.geometry("600x700")




miFrame=Frame(raiz)
miFrame.pack()
miFrame.pack(side="bottom", anchor="center")
miFrame.config(bg="#708D6B")
miFrame.config(width="100", height="600")

miFrame=Frame(raiz)
miFrame.pack()
miFrame.pack(side="right", anchor="center")
miFrame.place(x=0, y=350)

miFrame.config(bg="#708D6B")
miFrame.config(width="600", height="100")

miFrame=Frame(raiz)
miFrame.pack()
miFrame.pack(side="top", anchor="n")

miFrame.config(bg="#41CB71")
miFrame.config(width="600", height="100")

miFrame2=Frame(raiz)
miFrame2.pack()
miFrame2.place(x=170, y=220)
miFrame2.config(bg="black")
miFrame2.config(width="50", height="100")
Titulo = Label(raiz, text="Sur", font=("Helvetica",10), bg="#41CB71", fg="black").place(x=180, y=195)

miFrame2=Frame(raiz)
miFrame2.pack()
miFrame2.place(x=380, y=480)
miFrame2.config(bg="black")
miFrame2.config(width="50", height="100")
Titulo = Label(raiz, text="Norte", font=("Helvetica",10), bg="#41CB71", fg="black").place(x=385, y=455)

miFrame2=Frame()
miFrame2.pack()
miFrame2.place(x=380, y=270)
miFrame2.config(bg="black")
miFrame2.config(width="100", height="50")
Titulo = Label(raiz, text="Oeste", font=("Helvetica",10), bg="#41CB71", fg="black").place(x=410, y=240)

miFrame2=Frame(raiz)
miFrame2.pack()
miFrame2.place(x=300, y=100)
miFrame2.config(bg="yellow")
miFrame2.config(width="1", height="250")

miFrame2=Frame(raiz)
miFrame2.pack()
miFrame2.place(x=300, y=450)
miFrame2.config(bg="yellow")
miFrame2.config(width="1", height="250")

miFrame2=Frame(raiz)
miFrame2.pack()
miFrame2.place(x=1, y=400)
miFrame2.config(bg="yellow")
miFrame2.config(width="250", height="1")

miFrame2=Frame(raiz)
miFrame2.pack()
miFrame2.place(x=350, y=400)
miFrame2.config(bg="yellow")
miFrame2.config(width="250", height="1")

miFrame2=Frame(raiz)
miFrame2.pack()
miFrame2.place(x=348, y=400)
miFrame2.config(bg="black")
miFrame2.config(width="3", height="50")
miFrame2=Frame(raiz)
miFrame2.pack()
miFrame2.place(x=346, y=400)
miFrame2.config(bg="green")
miFrame2.config(width="2", height="5")
miFrame2=Frame(raiz)
miFrame2.pack()
miFrame2.place(x=346, y=407)
miFrame2.config(bg="yellow")
miFrame2.config(width="2", height="5")
miFrame2=Frame(raiz)
miFrame2.pack()
miFrame2.place(x=346, y=414)
miFrame2.config(bg="red")
miFrame2.config(width="2", height="5")

miFrame2=Frame(raiz)
miFrame2.pack()
miFrame2.place(x=252, y=350)
miFrame2.config(bg="black")
miFrame2.config(width="2", height="50")
miFrame2=Frame(raiz)
miFrame2.pack()
miFrame2.place(x=254, y=350)
miFrame2.config(bg="green")
miFrame2.config(width="2", height="5")
miFrame2=Frame(raiz)
miFrame2.pack()
miFrame2.place(x=254, y=357)
miFrame2.config(bg="yellow")
miFrame2.config(width="2", height="5")
miFrame2=Frame(raiz)
miFrame2.pack()
miFrame2.place(x=254, y=364)
miFrame2.config(bg="red")
miFrame2.config(width="2", height="5")

miFrame2=Frame(raiz)
miFrame2.pack()
miFrame2.place(x=300, y=350)
miFrame2.config(bg="black")
miFrame2.config(width="50", height="2")
miFrame2=Frame(raiz)
miFrame2.pack()
miFrame2.place(x=300, y=352)
miFrame2.config(bg="red")
miFrame2.config(width="5", height="2")
miFrame2=Frame(raiz)
miFrame2.pack()
miFrame2.place(x=307, y=352)
miFrame2.config(bg="yellow")
miFrame2.config(width="5", height="2")
miFrame2=Frame(raiz)
miFrame2.pack()
miFrame2.place(x=314, y=352)
miFrame2.config(bg="green")
miFrame2.config(width="5", height="2")


miFrame2=Frame(raiz)
miFrame2.pack()
miFrame2.place(x=250, y=450)
miFrame2.config(bg="black")
miFrame2.config(width="50", height="2")
miFrame2=Frame(raiz)
miFrame2.pack()
miFrame2.place(x=250, y=448)
miFrame2.config(bg="red")
miFrame2.config(width="5", height="2")
miFrame2=Frame(raiz)
miFrame2.pack()
miFrame2.place(x=257, y=448)
miFrame2.config(bg="yellow")
miFrame2.config(width="5", height="2")
miFrame2=Frame(raiz)
miFrame2.pack()
miFrame2.place(x=264, y=448)
miFrame2.config(bg="green")
miFrame2.config(width="5", height="2")

miFrame2=Frame(raiz)
miFrame2.pack()
miFrame2.place(x=120, y=480)
miFrame2.config(bg="black")
miFrame2.config(width="100", height="50")
Titulo = Label(raiz, text="Este", font=("Helvetica",10), bg="#41CB71", fg="black").place(x=160, y=455)

miFrame2=Canvas(width=20,height=20,bg="red")
miFrame2.place(x=130, y=492)

miFrame2=Canvas(width=20,height=20,bg="#3D5144")
miFrame2.place(x=160, y=492)

miFrame2=Canvas(width=20,height=20,bg="#3D5144")
miFrame2.place(x=190, y=492)

miFrame2=Canvas(width=20,height=20,bg="red")
miFrame2.place(x=185, y=230)

miFrame2=Canvas(width=20,height=20,bg="#3D5144")
miFrame2.place(x=185, y=260)

miFrame2=Canvas(width=20,height=20,bg="#3D5144")
miFrame2.place(x=185, y=290)

miFrame2=Canvas(width=20,height=20,bg="#3D5144")
miFrame2.place(x=390, y=485)

miFrame2=Canvas(width=20,height=20,bg="#3D5144")
miFrame2.place(x=390, y=515)

miFrame2=Canvas(width=20,height=20,bg="red")
miFrame2.place(x=390, y=545)

#Este

miFrame2=Canvas(width=20,height=20,bg="#3D5144")
miFrame2.place(x=390, y=285)

miFrame2=Canvas(width=20,height=20,bg="#3D5144")
miFrame2.place(x=420, y=285)

miFrame2 =Canvas(width=20,height=20,bg="red")
miFrame2.place(x=450, y=285)

miFrame3=Frame(raiz)
miFrame3 =Canvas(width=400,height=1,bg="green")

#Semaforo 1 #-320,+450,-220,350+
#315,450,220,350
Altura = 320
for i in range(6):
	Auto3A=Frame(raiz)
	Auto3A.config(bg="#708D6B")
	Auto3A.config(width="20", height="30")
	Auto3A.place(x=265, y=Altura)
	Altura = Altura - 40

#Semaforo 2
Altura = 450
for i in range(6):
	Auto3A=Frame(raiz)
	Auto3A.config(bg="#708D6B")
	Auto3A.config(width="20", height="30")
	Auto3A.place(x=315, y=Altura)
	Altura = Altura + 40

#Semaforo 3
Ancho = 220
for i in range(6):
	Auto3A=Frame(raiz)
	Auto3A.config(bg="#708D6B")
	Auto3A.config(width="30", height="20")
	Auto3A.place(x=Ancho, y=420)
	Ancho = Ancho -40

#Semaforo 4
Ancho = 350
for i in range(6):
	Auto3A=Frame(raiz)
	Auto3A.config(bg="#708D6B")
	Auto3A.config(width="30", height="20")
	Auto3A.place(x=Ancho, y=360)
	Ancho = Ancho + 40


Auto=Frame()
Auto.pack()

Titulo = Label(raiz, text="Practica No.1", font=("Helvetica",20), bg="#41CB71", fg="#C8FFBF").place(x=250, y=10)
Titulo = Label(raiz, text="Nombre: Luis Daniel García Leal     Lab:Sist adaptativos", font=("Helvetica",12), bg="#41CB71", fg="#C8FFBF").place(x=200, y=50)
Titulo = Label(raiz, text="Semestre: 5to  Carrera: ITS  20/10/2020", font=("Helvetica",12), bg="#41CB71", fg="#C8FFBF").place(x=200, y=70)




def evento1():
	global congestionamiento1,congestionamiento2,congestionamiento3,congestionamiento4
	congestionamiento1=False
	congestionamiento2=False
	congestionamiento3=False
	congestionamiento4=False
	variable=1
	print("Evento: Trafico normal.")
	return(variable)

def evento2():
	global congestionamiento1,congestionamiento2,congestionamiento3,congestionamiento4
	congestionamiento1=True
	congestionamiento2=True
	congestionamiento3=False
	congestionamiento4=False
	variable=2
	print("Evento: Trafico congestionado en los carriles norte y sur.")
	return(variable)


def evento3():
	global congestionamiento1,congestionamiento2,congestionamiento3,congestionamiento4
	congestionamiento1=False
	congestionamiento2=False
	congestionamiento3=True
	congestionamiento4=True
	variable=3
	print("Evento: Trafico congestionado en los carriles este y oeste.")
	return(variable)




def tiempos():
	    global congestionamiento1,congestionamiento2,congestionamiento3,congestionamiento4
	    congestionamiento1= False
	    congestionamiento2= False
	    congestionamiento3= False
	    congestionamiento4= False
	    variable=evento1()
	    variable=evento2()
	    variable=evento3()
	    boton1=Button(raiz, text="(Trafico normal)", bg="#C8FFBF",command=evento1).place(x=10,y=10)
       		
	    boton2=Button(raiz, text="(Congestionamiento norte y sur)", bg="#C8FFBF",command=evento2).place(x=10,y=40)

	    boton3=Button(raiz, text="(Congestionamiento este y oeste)", bg="#C8FFBF",command=evento3).place(x=10,y=70)

	    Orden=True
	    while (True):

       		queue1 = len(cola1)
       		queue2 = len(cola2)
       		queue3 = len(cola3)
       		queue4 = len(cola4)

       		if congestionamiento1==True:
        		numazar1=random.randint(2,3)

       		else:
       			numazar1=random.randint(0,2)

       		Parametro_c1=queue1-6 
       		Parametro_c1= Parametro_c1 * (1-2)
        	for i in range(numazar1):
        		if queue1 <= 6:
        			cola1.append("Coche")

       			Altura = 320
       			for i in cola1:
       				Auto3A=Frame(raiz)
       				Auto3A.config(bg="red")
       				Auto3A.config(width="20", height="30")
       				Auto3A.place(x=265, y=Altura)

       				Altura = Altura - 40



        	if congestionamiento2==True:
        		numazar2=random.randint(2,3)
        	else:
        		numazar2=random.randint(0,2)

        	for i in range(numazar2):
        		if queue2 <= 6:
        			cola2.append("Coche")

       			Altura = 450
       			for i in cola2:
       				Auto3A=Frame(raiz)
       				Auto3A.config(bg="red")
       				Auto3A.config(width="20", height="30")
       				Auto3A.place(x=315, y=Altura)
       				Altura = Altura + 40


        	if congestionamiento3 == True:
        		numazar3=random.randint(2,3)
        	else:
        		numazar3=random.randint(0,2)
        	for i in range(numazar3):
        		if queue3 <= 6:
        			cola3.append("Coche")

        		Ancho=220
       			for i in cola3:
       				Auto3A=Frame(raiz)
       				Auto3A.config(bg="red")
       				Auto3A.config(width="30", height="20")
       				Auto3A.place(x=Ancho, y=420)
       				Ancho = Ancho - 40



        	if congestionamiento4 == True:
        		numazar4=random.randint(2,3)
        	else:
        		numazar4=random.randint(0,2)
        	for i in range(numazar4):
        		if queue1 <= 6:
        			cola4.append("Coche")

        		Ancho = 350
        		for i in cola4:
       				Auto3A=Frame(raiz)
       				Auto3A.config(bg="red")
       				Auto3A.config(width="30", height="20")
       				Auto3A.place(x=Ancho, y=360)
       				Ancho = Ancho + 40



        	print("Norte: ", queue1)
       		print("Sur: ", queue2)
       		print("Este: ", queue3)
       		print("Oeste: ", queue4)
       		print(" ------------ ")
       		time.sleep(1)

       		if(SemaforoV==0 and SemaforoH==0):


       			trafico = queue1 + queue2
       			trafico2 = queue3 + queue4

       			if Orden==True:

       				t2= threading.Thread(name="Hilo_2", target=semaforos(queue1,queue2))
       				t2.start()
       				

       				Orden=False
       				     				

       			else:

       				t3= threading.Thread(name="Hilo_3", target=semaforos2(queue3,queue4))
       				t3.start()
       				

       				Orden=True
       				

         

def semaforos(queue1, queue2):
	SemaforoV=True
	SemaforoH=False
	miFrame2=Canvas(width=20,height=20,bg="#3D5144")
	miFrame2.place(x=185, y=230)

	miFrame2=Canvas(width=20,height=20,bg="#3D5144")
	miFrame2.place(x=185, y=260)

	miFrame2=Canvas(width=20,height=20,bg="green")
	miFrame2.place(x=185, y=290)

	miFrame2=Canvas(width=20,height=20,bg="green")
	miFrame2.place(x=390, y=485)

	miFrame2=Canvas(width=20,height=20,bg="#3D5144")
	miFrame2.place(x=390, y=515)

	miFrame2=Canvas(width=20,height=20,bg="#3D5144")
	miFrame2.place(x=390, y=545)

	parametro_e=time.time()
	parametro_s=parametro_e + queue1 + queue2 + 2
	extension=0
	while time.time() < parametro_s:
		if queue1 > 0:
			Altura = 320


			for i in cola1:
				Auto3A=Frame(raiz)
				Auto3A.config(bg="#708D6B")
				Auto3A.config(width="20", height="30")
				Auto3A.place(x=265, y=Altura)
				Altura = Altura - 40
				time.sleep(0.5)

			for i in cola1:
				cola1.pop(0)

		if queue2 > 0:
			Altura = 450


			for i in cola2:
				Auto3A=Frame(raiz)
				Auto3A.config(bg="#708D6B")
				Auto3A.config(width="20", height="30")
				Auto3A.place(x=315, y=Altura)
				time.sleep(0.5)
				Altura = Altura + 40

			for i in cola2:
				cola2.pop(0)

		queue1 = len(cola1)
		queue2 = len(cola2)
		if queue2 !=0 and queue1 !=0 and extension<3:
			parametro_s + 5
			extension = extension + 1

		time.sleep(1)

	print("El semaforo norte y sur esta en verde")
	SemaforoV=False
	SemaforoH=False

	miFrame2=Canvas(width=20,height=20,bg="#3D5144")
	miFrame2.place(x=185, y=230)

	miFrame2=Canvas(width=20,height=20,bg="yellow")
	miFrame2.place(x=185, y=260)

	miFrame2=Canvas(width=20,height=20,bg="#3D5144")
	miFrame2.place(x=185, y=290)

	miFrame2=Canvas(width=20,height=20,bg="#3D5144")
	miFrame2.place(x=390, y=485)

	miFrame2=Canvas(width=20,height=20,bg="yellow")
	miFrame2.place(x=390, y=515)

	miFrame2=Canvas(width=20,height=20,bg="#3D5144")
	miFrame2.place(x=390, y=545)

	time.sleep(2)




	miFrame2=Canvas(width=20,height=20,bg="red")
	miFrame2.place(x=185, y=230)

	miFrame2=Canvas(width=20,height=20,bg="#3D5144")
	miFrame2.place(x=185, y=260)

	miFrame2=Canvas(width=20,height=20,bg="#3D5144")
	miFrame2.place(x=185, y=290)

	miFrame2=Canvas(width=20,height=20,bg="#3D5144")
	miFrame2.place(x=390, y=485)

	miFrame2=Canvas(width=20,height=20,bg="#3D5144")
	miFrame2.place(x=390, y=515)

	miFrame2=Canvas(width=20,height=20,bg="red")
	miFrame2.place(x=390, y=545)

	return

def semaforos2(queue3, queue4):
	SemaforoV=False
	SemaforoH=True

	miFrame2=Canvas(width=20,height=20,bg="#3D5144")
	miFrame2.place(x=130, y=492)

	miFrame2=Canvas(width=20,height=20,bg="#3D5144")
	miFrame2.place(x=160, y=492)

	miFrame2=Canvas(width=20,height=20,bg="green")
	miFrame2.place(x=190, y=492)

	miFrame2=Canvas(width=20,height=20,bg="green")
	miFrame2.place(x=390, y=285)

	miFrame2=Canvas(width=20,height=20,bg="#3D5144")
	miFrame2.place(x=420, y=285)

	miFrame2 =Canvas(width=20,height=20,bg="#3D5144")
	miFrame2.place(x=450, y=285)


	parametro_e=time.time()
	parametro_s=parametro_e + queue3 + queue4 + 2
	extension=0
	while time.time() < parametro_s:
		if queue3 > 0:
			Ancho = 220
#-320,+450,-220,350+
			for i in cola3:
				Auto3A=Frame(raiz)
				Auto3A.config(bg="#708D6B")
				Auto3A.config(width="30", height="20")
				Auto3A.place(x=Ancho, y=420)
				Ancho = Ancho -40
				time.sleep(0.5)
			for i in cola3:
				cola3.pop(0)

		if queue4 > 0:
			Ancho = 350

			for i in cola4:
				Auto4A=Frame(raiz)
				Auto4A.config(bg="#708D6B")
				Auto4A.config(width="30", height="20")
				Auto4A.place(x=Ancho, y=360)
				Ancho = Ancho + 40
				time.sleep(0.5)
			for i in cola4:
				cola4.pop(0)

		queue3 = len(cola3)
		queue4 = len(cola4)
		if queue3 !=0 and queue4 !=0 and extension<3:
			parametro_s + 5
			extension = extension + 1

	time.sleep(1)

	print("El semaforo este y oeste esta en verde")
	SemaforoV=False
	SemaforoH=False

	miFrame2=Canvas(width=20,height=20,bg="#3D5144")
	miFrame2.place(x=130, y=492)

	miFrame2=Canvas(width=20,height=20,bg="yellow")
	miFrame2.place(x=160, y=492)

	miFrame2=Canvas(width=20,height=20,bg="#3D5144")
	miFrame2.place(x=190, y=492)

	miFrame2=Canvas(width=20,height=20,bg="#3D5144")
	miFrame2.place(x=390, y=285)

	miFrame2=Canvas(width=20,height=20,bg="yellow")
	miFrame2.place(x=420, y=285)

	miFrame2 =Canvas(width=20,height=20,bg="#3D5144")
	miFrame2.place(x=450, y=285)

	time.sleep(2)





	miFrame2=Canvas(width=20,height=20,bg="red")
	miFrame2.place(x=130, y=492)

	miFrame2=Canvas(width=20,height=20,bg="#3D5144")
	miFrame2.place(x=160, y=492)

	miFrame2=Canvas(width=20,height=20,bg="#3D5144")
	miFrame2.place(x=190, y=492)

	miFrame2=Canvas(width=20,height=20,bg="#3D5144")
	miFrame2.place(x=390, y=285)

	miFrame2=Canvas(width=20,height=20,bg="#3D5144")
	miFrame2.place(x=420, y=285)

	miFrame2 =Canvas(width=20,height=20,bg="red")
	miFrame2.place(x=450, y=285)


	return


t1= threading.Thread(name="Hilo_1", target=tiempos)
t1.start()


raiz.mainloop()