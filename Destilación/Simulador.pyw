# -*- coding: utf-8 -*-
"""
 
"""

# Importación de librerías 
from tkinter import *
from tkinter import ttk
import pandas as pd
from tkinter import messagebox

import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

# Implementar los enlaces clave de Matplotlib por defecto.
from matplotlib.figure import Figure

import numpy as np
import matplotlib.pyplot as plt

######## Ventana de bienvenida #########
inicio = Tk()
inicio.title("Inicio")
inicio.geometry("1500x1200")

# Marco número i0
framei0 = LabelFrame(inicio, text="Simulador de destilación", 
                    bg="grey",fg="white", 
                    padx=10, pady=80,font=("Times new Roman", 25))
framei0.grid(row=0, column=0)
framei0.grid(row=0, column=0)


# # Imagen de columna de destilacion 
imagen = PhotoImage(file='columna.png')
lblfondo = Label(framei0, 
                 image=imagen)
lblfondo.grid(row=0, column=0)
framei0.config(width=480,height=320)

#Marco número i1
framei1= LabelFrame(inicio, text="Componentes de la mezcla", 
                    bg="white",fg="black", 
                    padx=55, pady=40,
                    font=("Times new Roman", 25))
framei1.grid(row=0, column=1)
framei1.config(width=80,height=20) 

## CONTENIDO MARCO COMPONENTES################################

###########ETIQUETAS
lbli11= Label(framei1,
              text="Define los componentes de la mezcla a analizar:", 
              font=("Times new Roman", 15))
lbli11.grid(pady=0,row=0,column=0)
lbli22= Label(framei1, text="Componente 1", font=("Times new Roman", 14))
lbli22.grid(pady=0,row=1,column=0)
lbli33= Label(framei1, text="Componente 2", font=("Times new Roman", 14))
lbli33.grid(pady=0,row=2,column=0)
lbli44= Label(framei1, text="¿Conoce la volatilidad relativa de la mezcla?", font=("Times new Roman", 14))
lbli44.grid(pady=0,row=3,column=0)

cajaComponente1=Entry(master=framei1, width=30,
                      font=("Times new Roman", 18))
cajaComponente2=Entry(master=framei1, width=30,
                      font=("Times new Roman", 18))
cajaConocelavolatilidadrelativadelamezcla=Entry(master=framei1, width=30,
                      font=("Times new Roman", 18))
cajaComponente1.grid(padx=1,pady=0, row=1, column=1)
cajaComponente2.grid(padx=1,pady=0, row=2, column=1)

#COMBOBOX
menupregunta=ttk.Combobox(framei1,
                    state="readonly",
                    values=['Sí', 'No'],
                    font=("Times new Roman", 12),
                    width=40
                    )
menupregunta.grid(padx=1,
                  pady=0,
                  row=3, 
                  column=1)


########## BOTONES
#Botton de ingresar datos

def leermezcla():
    global comp1, comp2, volatilidadrelativadelamezcla
    comp1=cajaComponente1.get()
    comp2=cajaComponente2.get()
    volatilidadrelativadelamezcla=cajaConocelavolatilidadrelativadelamezcla.get()
    framei1.configure(text=f"Componentes de la mezcla: {comp1}+{comp2}")
    resp=menupregunta.get()
    
    if resp=='Sí':
        
        ########## Ventana del método de McCabe-Thiele ########## 
        """
        Ejemplo 1
        xF = 0.35        # Fracción molar del componente ligero en la alimentación, -
        xD = 0.975       # Fracción molar del componente ligero en el destilado, -
        xW = 0.025       # Fracción molar del componente ligero en el rehervidor, -
        R = 1.5          # Relación de reflujo (L/D),-
        a = 2.5          # Factor de separación
        q = 1.5          #  Condición de la alimentación

        """

        # Crea la interfaz
        root = tkinter.Tk()
        root.title("SIMULADOR DE DESTILACIÓN")
        root.geometry("1400x690")

        #Panel para pestañas
        nb= ttk.Notebook(root)
        nb.pack()  

        #Agregamos pestanas
        p1=ttk.Frame(nb)
        p2=ttk.Frame(nb)

        #Nombre de pestañas
        nb.add(p1,text='Datos de destilación')
        nb.add(p2,text='Gráfica')

        # Marco número 1
        frame1 = LabelFrame(p1, text="Entradas", 
                            bg="gray",fg="white", 
                            padx=100, pady=80,font=("Times new Roman", 40))
        frame1.grid(row=0, column=0)
        #Marco número 2
        frame2 = LabelFrame(p1, text="Resultados", 
                            bg="white",fg="black", 
                            padx=100, pady=150,
                            font=("Times new Roman", 40))
        frame2.grid(row=0, column=1)

        #Pestaña del gráfico
        frame3 = LabelFrame(master=p2, 
                            text="Gráfico Generado", 
                            bg="gray",
                            fg="white", 
                            padx=2, 
                            pady=2,
                            font=("Times new Roman", 15))
        frame3.grid(row=0, column=1)


        # Marco de barra de herramientas
        frame4 = LabelFrame(master=p2,
                            bg="gray",
                            fg="white", 
                            padx=2, 
                            pady=2,
                            font=("Times new Roman", 12))
        frame4.grid(row=2, column=1)

        #Contenido del GUI
        #Casillas de ingreso de texto frame 1 
        lbl1= Label(frame1, text="Ingresa las variables de tu mezcla", font=("Times new Roman", 15))
        lbl1.grid(pady=5,row=1,column=1)

        lbl2= Label(frame1, text="xF", font=("Times new Roman", 13))
        lbl2.grid(pady=5,row=2,column=0)
        lbl3= Label(frame1, text="xD", font=("Times new Roman", 13))
        lbl3.grid(pady=5,row=3,column=0)
        lbl4= Label(frame1, text="xW", font=("Times new Roman", 13))
        lbl4.grid(pady=5,row=4,column=0)
        lbl5= Label(frame1, text="R", font=("Times new Roman", 13))
        lbl5.grid(pady=5,row=5,column=0)
        lbl6= Label(frame1, text="a", font=("Times new Roman", 13))
        lbl6.grid(pady=5,row=6,column=0)
        lbl7= Label(frame1, text="q", font=("Times new Roman", 13))
        lbl7.grid(pady=5,row=7,column=0)

        #Texto de entrada
        cajaxf=Entry(master=frame1, width=40)
        cajaxd=Entry(master=frame1, width=40)
        cajaxw=Entry(master=frame1, width=40)
        cajar=Entry(master=frame1, width=40)
        cajaa=Entry(master=frame1, width=40)
        cajaq=Entry(master=frame1, width=40)

        cajaxf.grid(padx=5, row=2, column=1)
        cajaxd.grid(padx=5, row=3, column=1)
        cajaxw.grid(padx=5, row=4, column=1)
        cajar.grid(padx=5, row=5, column=1)
        cajaa.grid(padx=5, row=6, column=1)
        cajaq.grid(padx=5, row=7, column=1)
        #Se define una funcion para el clickeo del botton


        def calcular():    
            global fig, canvas
            xF = float(cajaxf.get())        # Fracción molar del componente ligero en la alimentación, -
            xD = float(cajaxd.get())       # Fracción molar del componente ligero en el destilado, -
            xW = float(cajaxw.get())       # Fracción molar del componente ligero en el rehervidor, -
            R = float(cajar.get())          # Relación de reflujo (L/D), -
            a = float(cajaa.get())          # Factor de separación
            q = float(cajaq.get())          # Condición de la alimentación
            
            ######## Curva de equilibrio ########
            
            lbl1.configure(text="Los datos han sido ingresados")
            def eq_curve(a):
                x_eq = np.linspace(0,1,51)
                y_eq = a*x_eq/(1+(a-1)*x_eq)
                return y_eq, x_eq
            y_eq, x_eq = eq_curve(a)

            ######## Línea de alimentación ########
            def fed(xF,q,a):    
                c1 = (q*(a-1))
                c2 = q + xF*(1-a) - a*(q-1)
                c3 = -xF
                coeff = [c1, c2, c3]
                r = np.sort(np.roots(coeff))
                
                if r[0]>0:
                    xiE = r[0]
                else:
                    xiE = r[1]
               
                yiE = a*xiE/(1+ xiE*(a-1))
                if q == 1:
                    x_fed = [xF, xF]
                    y_fed = [xF, yiE]
                else:
                    x_fed = np.linspace(xF, xiE, 51)
                    y_fed = q/(q-1)*x_fed - xF/(q-1)
                
                return xiE, yiE, y_fed, x_fed
            xiE, yiE, y_fed, x_fed = fed(xF,q,a)

            ######## R_min & R (nuevo) ########
            R_min = (xD-yiE)/(yiE-xiE)
            R = R*R_min
            ########Punto de alimentación ########
            xiF = (xF/(q-1)+xD/(R+1))/(q/(q-1)-R/(R+1))
            yiF = R/(R+1)*xiF + xD/(R+1)
            ######## Sección de rectificación ########
            def rect(R,xD,xiF):
                x_rect = np.linspace(xiF-0.025,xD,51)    
                y_rect = R/(R+1)*x_rect + xD/(R+1)
                return y_rect,x_rect
            y_rect, x_rect = rect(R, xD,xiF)
            ######## Sección de agotamiento ########
            def stp(xiF,yiF,xW):
                x_stp = np.linspace(xW,xiF+0.025,51)    
                y_stp = ((yiF-xW)/(xiF-xW))*(x_stp-xW) + xW
                return y_stp,x_stp
            y_stp, x_stp = stp(xiF,yiF,xW)
            
            ######## Construcción de etapas ########
            s = np.zeros((1000,5)) # Matriz vacía (s) para calcular las coordenadas de las etapas
            for i in range(1,1000):
                # (s[i,0],s[i,1]) = (x1,y1) --> Primer punto
                # (s[i,2],s[i,3]) = (x2,y2) --> Segundo punto
                # La unión de (x1,y1) y (x2,y2) dará lugar a etapas
                
                s[0,0] = xD
                s[0,1] = xD
                s[0,2] = s[0,1]/(a-s[0,1]*(a-1))
                s[0,3] = s[0,1]
                s[0,4] = 0
            # x1
                s[i,0] = s[i-1,2]
                
                # Paso de ruptura una vez (x1,y1) < (xW,xW)
                if s[i,0] < xW:
                    s[i,1] = s[i,0] 
                    s[i,2] = s[i,0]
                    s[i,3] = s[i,0]
                    s[i,4] = i
                   
                    break  
                # y1
                if s[i,0] > xiF:
                    s[i,1] = R/(R+1)*s[i,0] + xD/(R+1)
                elif s[i,0] < xiF:
                    s[i,1] = ((yiF-xW)/(xiF-xW))*(s[i,0]-xW) + xW
                else:
                    s[i,1] = s[i-1,3]
                
                # x2
                if s[i,0] > xW:
                    s[i,2] = s[i,1]/(a-s[i,1]*(a-1))
                else:
                    s[i,2] = s[i,0]
                
                # y2
                s[i,3] = s[i,1]
                
                # Número de etapas 
                if s[i,0] < xiF:
                    s[i,4] = i
                else:
                    s[i,4] = 0
            s = s[~np.all(s == 0, axis=1)] # Borrado de filas con contenido cero
            s_rows = np.size(s,0)  
            #print(s)
            S = np.zeros((s_rows*2,2)) # Matriz vacía para reagrupar la matriz 's' para el trazado
            for i in range(0,s_rows):
                S[i*2,0] = s[i,0]
                S[i*2,1] = s[i,1]
                S[i*2+1,0] = s[i,2]
                S[i*2+1,1] = s[i,3]
            ######## Numeración de las etapas ########
            # (x2,y2) de la matriz 's' como (x_s,y_s) utilizada para la numeración de etapas
            
            x_s = s[:,2:3]
            y_s = s[:,3:4]
            stage = np.char.mod('%d', np.linspace(1,s_rows-1,s_rows-1))
            s_f = s_rows-np.count_nonzero(s[:,4:5], axis=0)
            print(s_f)
            
            ##########################################
            #           SALIDA DE DATOS
            ##########################################
            cajaRmin.configure(text=str(R_min))
            cajaR.configure(text=str(R))
            cajaEtapas.configure(text=str(s_rows-1))
            cajaplatof.configure(text=str(s_f))
            
            ########################################
            # Gráfico:
            ########################################    
            fig = plt.figure(num=None, figsize=(10, 4.2), dpi=130)
            # Parity line
            plt.plot([0,1],[0,1],"k-")
            # Equilibrium curve
            plt.plot(x_eq,y_eq,"r-", label="Curva de equilibrio")
            # Rectifying section line
            plt.plot(x_rect,y_rect,'k--', label="Sección de rectificación " )
            # Stripping section line
            plt.plot(x_stp,y_stp,'k-.', label="Sección de agotamiento")
            # Feed line
            plt.plot(x_fed,y_fed,'k:', label="Plato de alimentación")
            # Stages
            plt.plot(S[:,0],S[:,1],'b-', label="Etapas")
            plt.plot([xF,xF],[0,xF], 
                     color="lawngreen") # Alimentación
            plt.plot([xW,xW],[0,xW], 
                     color="indigo") # fondos
            plt.plot([xD,xD],[0,xD], 
                     color="deepskyblue") # Alimentación
            # Stage numbers
            for label, x, y in zip(stage, x_s, y_s):
                plt.annotate(label,
                             xy=(x, y),
                             xytext=(0,5),
                             textcoords='offset points', 
                             ha='right')
            
            # Puntos de alimentación, destilación y fondos
            plt.plot(xF,xF,'go',xD,xD,'go',xW,xW,'go',markersize=5)   
            plt.text(xF+0.05,xF-0.03,'($x_{F}, x_{F}$)',horizontalalignment='center')
            plt.text(xD+0.05,xD-0.03,'($x_{D}, x_{D}$)',horizontalalignment='center')
            plt.text(xW+0.05,xW-0.03,'($x_{W}, x_{W}$)',horizontalalignment='center')
            # Intersección:Puntos de alimentación, rectificación y agotamiento
            plt.plot(xiF,yiF,'go',markersize=5)
            plt.text(xiF+0.05,yiF-0.05,'($x_{iF}, y_{iF}$)',horizontalalignment='center')
            # Creación de las cajas de salida
            textstr1 = '\n'.join((
                r'$Entradas:$',
                r'$\alpha=%.1f$' % (a, ),
                r'$q=%.2f$' % (q, ),
                r'$x_F=%.2f$' % (xF, ),
                r'$x_D=%.2f$' % (xD, ),
                r'$x_W=%.2f$' % (xW, )))
            
            
            textstr2 = '\n'.join((
                r'$Salidas:$',
                r'$R_{min}=%.2f$' % (R_min, ),
                r'$R=%.2f$' % (R, ),
                r'$Etapas=%.0f$' % (s_rows-1, ),
                r'$Plato\: de \:alimentación=%.0f$' % (s_f, )))
            # colocar un cuadro de texto en la parte superior izquierda en las coordenadas de los ejes
            props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
            plt.text(0.65, 0.33, textstr1, fontsize=8, verticalalignment='bottom', bbox=props)
            plt.text(0.65, 0.0, textstr2, fontsize=8, verticalalignment='bottom', bbox=props)
            #  Configuración general del grafico
            plt.grid(True, which='major',linestyle=':',alpha=0.6)
            plt.grid(True, which='minor',linestyle=':',alpha=0.3)
            plt.minorticks_on()
            plt.legend(loc='upper left',
                       shadow=True)
            plt.xlabel("Composición en la fase L, x")
            plt.ylabel("Composición en la fase V, y")
            plt.savefig('McCabe - Thiele Method.png', dpi=140)
            plt.title("Destilación Binaria : Método de McCabe - Thiele")
            plt.show()

        ############### Fin del gráfico

            # Mostrar el gráfico
            # Lienzo del gráfico   
            # fig = Figure(figsize=(5,4),dpi=100)
            
            canvas = FigureCanvasTkAgg(fig, master=frame3)   #frame3
            canvas.draw()
            canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
            toolbar = NavigationToolbar2Tk(canvas, frame4) #barra de iconos
            toolbar.update()
            canvas.get_tk_widget().pack(side=BOTTOM, fill=x, expand=0)


        #Botton de ingresar datos
        Button(frame1, 
               command=calcular,
               text="Registrar los datos",  font=("Times new Roman", 13),
               width=15).grid(padx=2, pady=2, row=9, column=1, columnspan=2)

        # Botón para limpiar datos
        def limpiar():
            #Texto de entrada
            cajaxf.delete(0,END)
            cajaxd.delete(0,END)
            cajaxw.delete(0,END)
            cajar.delete(0,END)
            cajaa.delete(0,END)
            cajaq.delete(0,END)
            
            cajaRmin.configure(text="")
            cajaR.configure(text="")
            cajaEtapas.configure(text="")
            cajaplatof.configure(text="")
            canvas.get_tk_widget().destroy()
            toolbar.destroy()
            plt.figure().clear()
            canvas.delete("all")

        botonlimpiar=Button(frame1, 
               command=limpiar,
               text="Limpiar Datos", 
               font=("Times new Roman", 13),
               width=15)

        botonlimpiar.grid(padx=2, 
                          pady=2, 
                          row=10, 
                          column=1, 
                          columnspan=2)

        botonlimpiar.grid(padx=2, 
                          pady=2, 
                          row=11, 
                          column=1, 
                          columnspan=2)
        botonlimpiar.grid(padx=2, 
                          pady=2, 
                          row=10, 
                          column=1, 
                          columnspan=2)


        # Botón para salir del programa
        def salir():
            root.destroy()
        botonsalir = Button(frame1, 
               command=salir,
               text="Salir", 
               font=("Times new Roman", 13),
               width=15)
        botonsalir.grid(padx=2, 
                          pady=2, 
                          row=11, 
                          column=1, 
                          columnspan=2)


        #Casillas de salida de texto frame 2 

        lbl2= Label(frame2, text="Rmin", font=("Times new Roman", 13))
        lbl2.grid(pady=5,row=2,column=0)
        lbl3= Label(frame2, text="R   ", font=("Times new Roman", 13))
        lbl3.grid(pady=5,row=3,column=0)
        lbl4= Label(frame2, text="Etapas", font=("Times new Roman", 13))
        lbl4.grid(pady=5,row=4,column=0)
        lbl5= Label(frame2, text="Plato de alimentacion", font=("Times new Roman", 13))
        lbl5.grid(pady=5,row=5,column=0)

        cajaRmin=Label(frame2, width=40,font=("Times new Roman", 12))
        cajaR=Label(frame2, width=40,font=("Times new Roman", 12))
        cajaEtapas=Label(frame2, width=40,font=("Times new Roman", 12))
        cajaplatof=Label(frame2, width=40,font=("Times new Roman", 12))

        cajaRmin.grid(padx=5, row=2, column=1)
        cajaR.grid(padx=5, row=3, column=1)
        cajaEtapas.grid(padx=5, row=4, column=1)
        cajaplatof.grid(padx=5, row=5, column=1)

        #root.resizable(0,0)
        root.mainloop() 

    if resp=='No':
        ######Ventana de cálculo de volatilidad#####
      tablaAntoine = pd.read_csv("Tabla Antoine.csv", index_col="SUSTANCIA")
      tablaAntoine = tablaAntoine.drop(['No.'], axis=1)

      elementos=[]
      for i in range(len(tablaAntoine)):
          elementos.append([tablaAntoine.iloc[i]["FORMULA"],
                            tablaAntoine.index[i]])
      #tablaAntoine.iloc[i]["FORMULA"],
      # Aislar indice de tabla por elemento
      ## tablaAntoine.index[tablaAntoine['SUSTANCIA']=="carbon-tetrachloride"].tolist()

      # Ventana inicio
      volatilidad = Tk()
      volatilidad.title("Volatilidad Relativa de la Mezcla")
      volatilidad.geometry("800x800")
      volatilidad.rowconfigure(0, weight=1)
      volatilidad.columnconfigure(0, weight=1)

      # Marco número i0
      framev0 = LabelFrame(volatilidad, text="Componente 1:", 
                          bg="grey",fg="white", 
                          padx=35, pady=50,
                          font=("Times new Roman", 20))
      framev0.grid(row=0, column=0, sticky="news")

      #Marco número i1
      framev1= LabelFrame(volatilidad, text="Componente 2:", 
                          bg="white",fg="black", 
                          padx=35, pady=50,
                          font=("Times new Roman", 20))
      framev1.grid(row=0, column=1, sticky="news")

      # Marco Volatilidad
      framev2= LabelFrame(volatilidad, text="Cálculo de Volatilidad:", 
                          bg="white",fg="black", 
                          padx=35, pady=100,
                          font=("Times new Roman", 18))
      framev2.grid(row=1, column=0, columnspan=2, sticky="news")


      ## CONTENIDO MARCO COMPONENTE 1################################
      ###########ETIQUETAS framev0
      lblvc1= Label(framev0,
                    text="Selecciona el componente 1:", 
                    font=("Times new Roman", 13))
      lblvc1.grid(pady=5,row=0,column=0)
      #COMBOBOX 1
      menucomp1=ttk.Combobox(framev0,
                          state="readonly",
                          values=elementos,
                          width=50
                          )
      menucomp1.grid(pady=5,row=1,column=0)
      antoinec1= Label(framev0,
                    text="Constantes de Antoine:\nA=\nB=\nC=", 
                    font=("Times new Roman", 11))
      antoinec1.grid(pady=5,row=2,column=0)
      ####### MARCO COMP 2 frame v1
      lblvc2= Label(framev1,
                    text="Selecciona el componente 2:", 
                    font=("Times new Roman", 13))
      lblvc2.grid(pady=5,row=0,column=0)
      ##COMBOBOX 2
      menucomp2=ttk.Combobox(framev1,
                          state="readonly",
                          values=elementos,
                          width=50
                          )
      menucomp2.grid(pady=5,row=1,column=0)
      antoinec2= Label(framev1,
                    text="Constantes de Antoine:\nA=\nB=\nC=", 
                    font=("Times new Roman", 11))
      antoinec2.grid(pady=5,row=2,column=0)

      ##### MARCO VOLATILIDAD framev2
      lbvol0= Label(framev2,
                    text="Escribe las condiciones de la mezcla:", 
                    font=("Times new Roman", 13))
      lbvol0.grid(pady=5,row=0,column=0)
      lblvol1= Label(framev2, text="Temperatura (°C)", 
                     font=("Times new Roman", 13))
      lblvol1.grid(pady=5,row=1,column=0)
      lblT=Label(framev2, width=25,
                 font=("Times new Roman", 13),
                 text='Temperatura (°C)')
      lblT.grid(padx=5, row=1, column=0)
      cajaT=Entry(framev2, width=25,font=("Times new Roman", 13))
      cajaT.grid(padx=5, row=1, column=1)

      lblP1= Label(framev2, text="Psat 1=",
                   width=25,
                     font=("Times new Roman", 12))
      lblP1.grid(pady=5,row=2,column=0)
      lblP1dato= Label(framev2, text="", width=25, 
                     font=("Times new Roman", 12))
      lblP1dato.grid(pady=5,row=2,column=1)

      lblP2=Label(framev2, width=25,
                  font=("Times new Roman", 12),
                 text='Psat 2 =')
      lblP2.grid(padx=5, row=3, column=0)
      lblP2dato= Label(framev2, width=25,
                     font=("Times new Roman", 12))
      lblP2dato.grid(pady=5,row=3,column=1)


      lblvolf= Label(framev2, 
                     width=25,
                     text="Volatilidad Calculada:", 
                     font=("Times new Roman", 13))
      lblvolf.grid(pady=5,row=4,column=0)
      lblvoldato=Label(framev2, width=25,
                       text='',
                       font=("Times new Roman", 12))
      lblvoldato.grid(padx=5, row=4, column=1)

     

      ########## BOTONES
      #Botton de ingresar datos
      def calcvol():
          global ctes1, ctes2, compv1, compv2
          try:
              T=float(cajaT.get())
              compv1=menucomp1.get().split()
              compv2=menucomp2.get().split()
              ctes1 = tablaAntoine.loc[compv1[1]] 
              ctes2 = tablaAntoine.loc[compv2[1]]
              antoinec1.configure(text=ctes1)
              antoinec2.configure(text=ctes2)
              
              #Definir constantes de antoine
              #COMP1
              A1=ctes1[1]
              B1=ctes1[2]
              C1=ctes1[3]
              #COMP2
              A2=ctes2[1]
              B2=ctes2[2]
              C2=ctes2[3]
              
              Psat1=10**(A1-B1/(T+C1))
              Psat2=10**(A2-B2/(T+C2))
              valoralfa = Psat1/Psat2
              lblvoldato.configure(text=f"{round(valoralfa,6)}")
              lblP1dato.configure(text=f"{round(Psat1,6)} mmHg")
              lblP2dato.configure(text=f"{round(Psat2,6)} mmHg")
              
          except KeyError:
              # No existe el compuesto
              messagebox.showinfo("Información","Verifique los compuestos introducidos")
          except TypeError:
               messagebox.showinfo("Información","La temperatura debe ser un número")
          except ValueError:
               messagebox.showinfo("Información","Revisa el valor de temperatura introducido")
          except IndexError:
              messagebox.showinfo("Información","Ingresa ambos componentes")
          except NameError:
              messagebox.showinfo("Información","Ingresa ambos componentes")
              
      #Botón Calcular
      botonvol=Button(framev2,
            command=calcvol,
            text="Calcular Volatilidad", 
            font=("Times new Roman", 13),
            width=15)
      botonvol.grid(padx=2, pady=2, row=1, column=2)
         
      # Botón para limpiar datos
      def limpiarv():
          #Texto de entrada
          cajaT.delete(0,END)
          menucomp1.delete(0,END)
          menucomp2.delete(0,END)
          antoinec1.configure(text="Constantes de Antoine:\nA=\nB=\nC")
          antoinec2.configure(text="Constantes de Antoine:\nA=\nB=\nC=")
          lblvoldato.configure(text="")
          lblP1dato.configure(text="")
          lblP2dato.configure(text="")
          menucomp1.set('')
          menucomp2.set('')

      botonlimpiarv=Button(framev2, 
             command=limpiarv,
             text="Limpiar Datos",
             font=("Times new Roman", 13),
             width=15)
      botonlimpiarv.grid(padx=2, 
                        pady=2, 
                        row=2, 
                        column=2, 
                        )

      # Botón para cerrar
      def salirv():
          volatilidad.destroy()
      botonsalirv = Button(framev2, 
             command=salirv,
             text="Cerrar Ventana", 
             font=("Times new Roman", 13),
             width=15)
      botonsalirv.grid(padx=2, 
                       pady=2, 
                       row=3, 
                       column=2)
      
      volatilidad.mainloop()
          
bleeri=Button(framei1,
      command=leermezcla,
      text="Registrar los datos", 
      width=15, font=("Times new Roman", 13))
bleeri.grid(padx=2, pady=2, row=9, column=1, columnspan=2)


    
# Botón para limpiar datos
def limpiari():
    #Texto de entrada
    cajaComponente1.delete(0,END)
    cajaComponente2.delete(0,END)
    menupregunta.delete(0,END)
    menupregunta.set('')
    
botonlimpiar=Button(framei1, 
       command=limpiari,
       text="Limpiar Datos", 
       width=15,font=("Times new Roman", 13))
botonlimpiar.grid(padx=2, 
                  pady=2, 
                  row=10, 
                  column=1, 
                  columnspan=2)

# Botón para cerrar
def saliri():
    inicio.destroy()
botonsaliri = Button(framei1, 
       command=saliri,
       text="Salir", 
       width=15,font=("Times new Roman", 13))
botonsaliri.grid(padx=2, 
                 pady=2, 
                 row=11, 
                 column=1, 
                 columnspan=3)

inicio.mainloop()
    

