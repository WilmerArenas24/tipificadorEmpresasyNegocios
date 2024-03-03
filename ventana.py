from tkinter import *

#Inicializar TKINTER
aplicacion = Tk()

#Tamaño de la ventana
aplicacion.geometry('1520x780+0+0')

#Eviatr maximizar ventana
aplicacion.resizable(0,0)

#Panel superior
panelSuperior = Frame(aplicacion, bd=0, relief=FLAT)
panelSuperior.pack(side=TOP)

#Etiqueta titulo
etiquetaTitulo = Label(panelSuperior, text='Tipificador Empresas & Negocios', fg='#4DF445',
                       font=('Dosis',25), bg='#2B595B',width=28)
etiquetaTitulo.grid(row=0,column=0)

#Panel izquierdo
panelIzquierdo = Frame(aplicacion, bd=1,relief=FLAT)
panelIzquierdo.pack(side=LEFT)

#Panel-UNO
panelUno=LabelFrame(panelIzquierdo, text='Datos de llamada', font=('Dosis',19,'bold'),bd=1,relief=FLAT,fg='#4DF445',bg='#2B595B')
panelUno.pack(side=LEFT)

#Panel-DOS
panelDos=LabelFrame(panelIzquierdo, text='DOS', font=('Dosis',19,'bold'),bd=1,relief=FLAT,fg='#4DF445')
panelDos.pack(side=LEFT)

#Panel-TRES
panelTres=LabelFrame(panelIzquierdo, text='TRES', font=('Dosis',19,'bold'),bd=1,relief=FLAT,fg='#4DF445')
panelTres.pack(side=LEFT)

#Panel derecha
panelDerecha = Frame(aplicacion, bd=1, relief=FLAT)
panelDerecha.pack(side=RIGHT)
#Titulo de la ventana
aplicacion.title('Tipificador E&M')


#Color de la ventana
aplicacion.config(bg='#2B595B')

datosLlamadas = ['Nombre del cliente','Cedula del cliente','Nit','Razon social','Cuenta','Cargo','Servicio afectado',
                 'Solicitud del cliente','Tel/Cel origen', 'Tel/Cel cliente', 'Estado CM', 'Equipo','Vecinos',
                 'Niveles', 'Aprovisionamiento','PQR','Marcación','Estado de solicitud']
contador = 0
for datos in datosLlamadas:
    datos = Label(panelUno, text=datos.title(), font=('Docis',16),bg='#2B595B',fg='#FFFFFF')
    datos.grid(row=contador, column = 0, sticky=W)
    contador += 1

#Evitar que la ventana se cierre
aplicacion.mainloop()