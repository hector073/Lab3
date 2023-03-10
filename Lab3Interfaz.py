#########################################Links#########################################################
#video sobre como leer datos de arduino en py: https://www.youtube.com/watch?v=AHr94RtMj1A

#########################################IMPORTS######################################################

from tkinter import * #el * va a importar todo de la libreria de tkinter

import serial.tools.list_ports #para importar esta libreria es necesario instalar la libreria. Para ello 
# se escribe pip install pyserial en el comand prompt y se oprime enter

def comArduinoAPython():   
    #########################################Definicion de variables y arrays##############################

    ports = serial.tools.list_ports.comports() # enlista los puertos com utilizados
    serialInst = serial.Serial()  

    portsList = [] #array en el que se guardaran los puertos com para luego ser desplegados

    #####################################COM PORTS##########################################################

    for onePort in ports:#este ciclo for despliega en pantalla los puertos com disponibles
        portsList.append(str(onePort))
        print(str(onePort)) 

    val = input("Seleccione Puerto: COM") #el usuario puede seleccionar el puerto due que quiera
    #recibir datos

    #ahora queremos toma el numero seleccionado por el usuario y unirlo a un string que pueda identificar 
    # nuestro dispositivo serial
    for x in range(0,len(portsList)):
        if portsList[x].startswith("COM" + str(val)):
            portVar = "COM" + str(val)
            print(portVar)



    #---------------------------Seteando nuestro dispositivo serial para poder abrirlo--------------
    serialInst.baudrate = 9600
    serialInst.port = portVar
    serialInst.open()

    while True:#se crea un loop para recibir datos constantemente
        if serialInst.in_waiting:            
            packet = serialInst.readline()
            print(packet.decode('utf').rstrip('\n'))
"""
####################################CREACION DE LA INTERFAZ###############################################
#def Interfaz():
root = Tk() #Toplevel widget of Tk which represents mostly the main window of an application. 
#It has an associated Tcl interpreter.
root.title("Monitoreo de sensores") #cambia el titulo de la ventana
root.iconbitmap(r"C:\Users\CarlosFernando\.vscode\SensorIcon.ico") #cambia el icono de la ventana por cualquiera que se le asigne
#Colocando r antes de las comas y luego pegando la direccion del icono se elimina el posible error que da si
#unicamente se escribe SensorIcon.ico ADVERTENCIA!!! El icono debe guardarse en el archivo .vscode, ubicado usualmente en la carpeta
#del usuario

root.geometry("600x300")#Tamano de la ventana. La x debe ser minuscula


#####################FUNCIONES########################################################################

def funct1Min():
    tiempo1 = Label(root, text = "1")
    tiempo1.grid(row = 5 , column = 1)# la posicion del texto que despliega la funcion se
    #debe colocar dentro de la funcion, de lo contraro no reconoce la variable tiempo1

def funct5Min():
    tiempo5 = Label(root, text = "5")
    tiempo5.grid(row = 6 , column = 1)

def funct10Min():
    tiempo10 = Label(root, text = "10")
    tiempo10.grid(row = 7 , column = 1)



################################TEXTO EN PANTALLA#################################
#texto = Label(root, text = 'Hi' ).pack() # Inserta un texto en la ventana. 
#El .pack() evita que se cree una ventana mucho mas grande que el texto.

texto1 = Label(root, text = "hola! Bienvenido!") #root indica que el texto se mostrara en la ventana principal llamada root
textfMuestreo = Label (root, text = " Seleccione la frecuencia de muesreo deseada: ")


#######################################BOTONES############################################

#command indica cual de las funciones definidas arriba se lleva a cabo al presionar el boton
boton1min = Button(root, text = "1 minuto", command = funct1Min, fg = "#4D33FF", bg = "#33FFED", padx = 30, pady = 15) #fg = frontground color, bg = background color
boton5min = Button(root, text = "5 minutos", command = funct5Min, fg = "#4D33FF", bg = "#33FFED", padx = 29, pady = 15)#padx = tama;o del boton en x
boton10min = Button(root, text = "10 minutos", command = funct10Min, fg = "#4D33FF", bg = "#33FFED", padx = 28, pady = 15)#pady = tama;o del boton en y

#----------------------organizacion de la ventana-----------------------------------------
#el siguiente pedazo de codigo es una alternativa para .pack(). grid posiciona el texto en filas y columnas, 
#de esta forma es mas intuitivo ordentar los textos
texto1.grid(row = 2 , column = 0)
textfMuestreo.grid(row = 4 , column = 0)
boton1min.grid(row = 5 , column = 0)
boton5min.grid(row = 6, column = 0)
boton10min.grid(row = 7, column = 0)




#Interfaz()   
#comArduinoAPython()



root.after(0, comArduinoAPython) #https://pythonguides.com/python-tkinter-mainloop/   
root.mainloop() #crea el loop 
"""

comArduinoAPython()