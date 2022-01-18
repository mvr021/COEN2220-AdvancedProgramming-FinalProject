# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 11:53:01 2021

@author: yeya
"""


import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

window = tk.Tk()
window.title("illustreya")
window.rowconfigure(1, minsize=1, weight=1)
window.columnconfigure(1, minsize=1, weight=1)

class menu():
    
    def __init__(self,master):
        
        #frame
        fr_menu = tk.Frame(master)
        fr_menu.grid(row=0,rowspan=3, column=0, sticky="ns")
        
        #label
        self.lbl_menu = tk.Label(fr_menu,text="Menú principal",font='bold')
      
        self.lbl_menu.grid(row=0, column=0, sticky = "ew",padx=5, pady=5)
        
        #logo
        self.photo = ImageTk.PhotoImage(Image.open("photo.png"))
        self.lbl_photo = Label(fr_menu,image=self.photo)
        self.lbl_photo.grid(row=1, column=0, sticky = "ew",padx=5, pady=5)
        
       # buttons
        self.btn_galeria = tk.Button(fr_menu, text="Galería", command=self.galeria)
        self.btn_com = tk.Button(fr_menu, text="Información", command=self.com)
        self.btn_tos = tk.Button(fr_menu, text="Términos y condiciones", command=self.tos)
        self.btn_estimados = tk.Button(fr_menu, text="Estimados", command=self.estimados)

        self.btn_galeria.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        self.btn_com.grid(row=3, column=0, sticky="ew", padx=5)
        self.btn_tos.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
        self.btn_estimados.grid(row=5, column=0, sticky="ew", padx=5)
        
           
    def galeria(self):
        # #Hide all frames except the one for galeria
        fr_inicio.grid_forget()
        fr_cominfo.grid_forget()
        fr_tosinfo.grid_forget()
        fr_estimadosinfo.grid_forget()
        fr_bocetoinfo.grid_forget()
        fr_pinturainfo.grid_forget()
        fr_galeria.grid(row=0,column=1,sticky="ns")
        
    def com(self):
        #Hide all frames except the one for comisiones
        fr_inicio.grid_forget()
        fr_galeria.grid_forget()
        fr_tosinfo.grid_forget()
        fr_estimadosinfo.grid_forget()
        fr_bocetoinfo.grid_forget()
        fr_pinturainfo.grid_forget()
        fr_cominfo.grid(row=0,rowspan=5,column=1,sticky="ns")

    def tos(self):
        #Hide all frames except the one for terminos y condiciones
        fr_inicio.grid_forget()
        fr_galeria.grid_forget()
        fr_cominfo.grid_forget()
        fr_estimadosinfo.grid_forget()
        fr_bocetoinfo.grid_forget()
        fr_pinturainfo.grid_forget()
        fr_tosinfo.grid(row=0,column=1,sticky="ns")
    
    def estimados(self):
        #hide all frames except the ones for estimados
        fr_inicio.grid_forget()
        fr_galeria.grid_forget()
        fr_cominfo.grid_forget()
        fr_tosinfo.grid_forget()
        fr_estimadosinfo.grid(row=0,column=1,sticky="ns")
        fr_bocetoinfo.grid(row=1,column=1,sticky="ns")
        fr_pinturainfo.grid(row=1,column=2,sticky="ns")

class inicioinfo():
    
    def __init__(self,master):
        
        #frame
        global fr_inicio, photo1
        fr_inicio =tk.Frame(master)
        fr_inicio.grid(row=0,column=1,sticky="ns")
        
        #label
        self.label = tk.Label(fr_inicio,text="Inicio",font='bold')
        self.label.grid(row=0, column=1, sticky="n",padx=5, pady=5)
        
        #contents
        self.text1 = tk.Text(fr_inicio,height=25,width=60)
        self.text1.grid(row=1,column=1,sticky="n")       
        self.text1.tag_configure("center", justify='center')
        photo1 = tk.PhotoImage(file='photo1.png')
        self.text1.image_create(tk.END, image=photo1)
        self.text1.insert(tk.END, '\n\n                         ¡Bienvenido!')

        self.text1.config(state='disabled')

class galeriainfo():
    
    def __init__(self,master):
        
        #frame
        global fr_galeria, photo2, photo3, photo4, photo5, photo6, photo7, photo8, photo9, photo10, photo11
        fr_galeria =tk.Frame(master)
        
        #label
        self.label = tk.Label(fr_galeria,text="Galería",font='bold')
        self.label.grid(row=0, column=1, sticky="n",padx=5, pady=5)
        
        #contents
        self.text1 = tk.Text(fr_galeria,height=25,width=60)
        self.text1.tag_configure("center", justify='center')
        
        photo2 = tk.PhotoImage(file='photo2.png')
        self.text1.image_create(tk.END, image=photo2)
        
        photo3 = tk.PhotoImage(file='photo3.png')
        self.text1.insert(tk.END, '\n\n')
        self.text1.image_create(tk.END, image=photo3)

        photo4 = tk.PhotoImage(file='photo4.png')
        self.text1.insert(tk.END, '\n\n')
        self.text1.image_create(tk.END, image=photo4)
        
        photo5 = tk.PhotoImage(file='photo5.png')
        self.text1.insert(tk.END, '\n\n')
        self.text1.image_create(tk.END, image=photo5)
        
        photo6 = tk.PhotoImage(file='photo6.png')
        self.text1.insert(tk.END, '\n\n')
        self.text1.image_create(tk.END, image=photo6)
        
        photo7 = tk.PhotoImage(file='photo7.png')
        self.text1.insert(tk.END, '\n\n')
        self.text1.image_create(tk.END, image=photo7)
        
        photo8 = tk.PhotoImage(file='photo8.png')
        self.text1.insert(tk.END, '\n\n')
        self.text1.image_create(tk.END, image=photo8)
        
        photo9 = tk.PhotoImage(file='photo9.png')
        self.text1.insert(tk.END, '\n\n')
        self.text1.image_create(tk.END, image=photo9)
        
        photo10 = tk.PhotoImage(file='photo10.png')
        self.text1.insert(tk.END, '\n\n')
        self.text1.image_create(tk.END, image=photo10)
        
        photo11 = tk.PhotoImage(file='photo11.png')
        self.text1.insert(tk.END, '\n\n')
        self.text1.image_create(tk.END, image=photo11)
        
        self.text1.config(state='disabled')
        self.text1.grid(row=1,column=1,sticky="n")    
    
        self.scroll = tk.Scrollbar(fr_galeria, command=self.text1.yview)
        self.scroll.grid(row=1,column=2,sticky="nse")
   
class cominfo():  
 
    def __init__(self,master):
       
        #frame
        global fr_cominfo
        fr_cominfo =tk.Frame(master)
        
        #label
        self.label = tk.Label(fr_cominfo,text="Información de comisiones",font='bold')
        self.label.grid(row=0, column=1, sticky="n",padx=5, pady=5)
        
        #contents
        __quote = """
    Precios:
        
    Boceto:
    rostro............................. $ 5 USD
    busto ............................. $ 10 USD
    cintura ........................... $ 15 USD
    cuerpo entero ..................... $ 20 USD

    Pintura digital:
    busto.............................. $ 30 USD
    cintura............................ $ 50 USD
    cuerpo entero...................... $ 70 USD 
    
    Adiciones:
        
    fondo:
    transparente.......................$ 0 USD
    sencillo...........................$ 10 USD
    complejo...........................$ 20 USD
    
    personajes adicionales............ x cantidad
    
    
    
¡Para realizar un encargo, envíeme su pedido por correo 
electrónico! illustreya@gmail.com

*Cuando me contrata, acepta haber leído y aceptado los 
Términos y condiciones.
    
    """
        self.text1 = tk.Text(fr_cominfo, height=25, width=60)
    
        self.text1.insert(tk.END, __quote)
        self.text1.config(state='disabled') 
        self.text1.grid(row=1,column=1,sticky="n")
    
        self.scroll = tk.Scrollbar(fr_cominfo, command=self.text1.yview)
        self.scroll.grid(row=1,column=1,sticky="nse")
    

class tosinfo():
    
    def __init__(self,master):
        
    
        #frame
        global fr_tosinfo
        fr_tosinfo =tk.Frame(master)
        
        #label
        self.label = tk.Label(fr_tosinfo,text="Términos y condiciones",font='bold')
        self.label.grid(row=0, column=1, sticky="n",padx=5, pady=5)
        
        __quote = """
                        Introducción:
 
Lea atentamente estos Términos de servicio ("Términos"). Al comprar mis servicios de arte, automáticamente acepta estar sujeto a los siguientes términos y condiciones.
 
** DESCARGO DE RESPONSABILIDAD ** ¡Todos los proyectos son solo DIGITALES y NO se enviarán físicamente a menos que se indique lo contrario! Por lo tanto, recuerde seleccionar "NO SE REQUIERE ENVÍO" o "NO SE NECESITA DIRECCIÓN" durante el pago.
 
Si tiene alguna pregunta o inquietud, comuníquese conmigo en: illustreya@gmail.com ¡Gracias!


    
                            Pago:

USD a través de PayPal únicamente.
Los pagos se deben realizar por adelantado para cualquier comisión.


 
                    Obras en curso y cambios:

¡Es su responsabilidad proporcionarme los detalles que necesitaré para hacer un trabajo exitoso antes del pago! Sea lo más completo posible y proporcione referencias si están disponibles. No habrá cambios para la obra de arte terminada.
En el caso de piezas completamente coloreadas, puede solicitar un trabajo en progreso ("wip") justo antes de que empiece a colorear. ¡Los cambios significativos solo se pueden aplicar en este momento!


 
                            Artista:

Al contratarme, solo compra mi trabajo artístico. Conservo todos los derechos de autor sobre mi trabajo, que incluyen, entre otros: el derecho a distribuir, reproducir o usar la imagen como muestra para ventas / autopromoción, a menos que se acuerde lo contrario.
La propiedad intelectual de los personajes retratados permanece en sus respectivos dueños.
La obra de arte puede tardar entre 1 y 21 días en completarse. Si tiene una fecha límite / límite de tiempo, infórmeme antes del pago. Si tarda más, me pondré en contacto contigo de inmediato.
Tengo derecho a rechazar pedidos.
Enviaré su copia de la obra de arte por correo electrónico o mensajería directa.
 


                            Cliente:

Las piezas encargadas son solo para uso personal / privado, lo que significa que no se pueden utilizar con fines comerciales o de lucro (no deben aparecer en ningún producto que se venda).
Dé el crédito adecuado cuando vuelva a publicarlo / usarlo para otro propósito.
No puede reclamar que la obra de arte es suya, editarla o configurarla para su redistribución. Tampoco debe utilizarlo para proyectos externos a menos que se acuerde.
 


                    Política de reembolsos:

Solo se pueden solicitar reembolsos si aún no he comenzado a trabajar en la comisión. Una vez iniciado no habrá reembolsos.
 
Al contratarme, significa que ha leído y aceptado todos los términos descritos anteriormente.
Te adherirás a la política de usar el arte para fines personales, sin fines de lucro y me proporcionarás todos los créditos de imagen, illustreya.
 
Este documento puede y será editado en cualquier momento sin necesidad de previo aviso.


Última actualización: 8/2/2021

    """
        self.text1 = tk.Text(fr_tosinfo,height=25, width=60)
        self.text1.grid(row=1,column=1,sticky="n")
        self.text1.insert(tk.END, __quote)
        self.text1.config(state='disabled')

        
        self.scroll = tk.Scrollbar(fr_tosinfo, command=self.text1.yview)
        self.scroll.grid(row=1,column=1,sticky="nse")

 
      

class estimadosinfo():
   
    def __init__(self,master):
        
        #frame
        global fr_estimadosinfo
        fr_estimadosinfo =tk.Frame(master)

        
    def selection(self):
        pass
    def selection1(self):
        pass
    def selection2(self):
        pass
    def precioTotal(self):
        pass
    def tiempoTotal(self):
        pass
    
class boceto(estimadosinfo):
    
    def __init__(self,master):
        
        #frame
        super().__init__(fr_estimadosinfo)

        global fr_bocetoinfo
        fr_bocetoinfo =Label(master)
        
        #contents
        self.frame1 = Label(fr_bocetoinfo)
        self.frame1.pack()
                
        Label(self.frame1, text="Boceto:").grid(row=0,column=4,sticky="ew")
        self.frame2 = LabelFrame(self.frame1, text='Tamaño', padx=30, pady=5)
        self.frame3 = LabelFrame(self.frame1, text='Fondo', padx=30, pady=5)
        self.frame4 = LabelFrame(self.frame1, text='Personajes',padx=30,pady=5)
        
        global var, var1, var2
        var = IntVar()
        var1 = IntVar()

        Radiobutton(self.frame2, text='rostro', variable=var, value=1,command=self.selection).pack()
        Radiobutton(self.frame2, text='busto', variable=var, value=2,command=self.selection).pack()
        Radiobutton(self.frame2, text='cintura', variable=var, value=3,command=self.selection).pack()
        Radiobutton(self.frame2, text='cuerpo completo', variable=var, value=4,command=self.selection).pack()

        Radiobutton(self.frame3, text='transparente', variable=var1, value=1,command=self.selection1).pack()
        Radiobutton(self.frame3, text='sencillo', variable=var1, value=2,command=self.selection1).pack()
        Radiobutton(self.frame3, text='complejo', variable=var1, value=3,command=self.selection1).pack()

        Label(self.frame4, text="Cantidad").grid(row=0,column=1)

        
        var2 = Entry(self.frame4, width = 5)
        var2.grid(row=1, column=1, columnspan=30)

        self.frame2.grid(row=4, column=4,padx=30)
        self.frame3.grid(row=5, column=4,padx=30)
        self.frame4.grid(row=6, column=4,padx=30)
        
        self.submit_btn = Button(self.frame1, text="Submit", command=self.submit, padx=50, pady=5)
        self.submit_btn.grid(row=7, column=4, pady=2)

    
    def selection(self):
        choice = var.get()
        
        if choice == 1:
            m = 'rostro'
        elif choice == 2:
            m = 'busto'
        elif choice == 3:
            m = 'cintura'
        elif choice == 4:
            m = 'cuerpo completo'
        else:
            pass
        return m

    def selection1(self):
        choice1 = var1.get()
        
        if choice1 == 1:
            n = 'transparente'
        elif choice1 == 2:
            n = 'sencillo'
        elif choice1 == 3:
            n = 'complejo'
        else:
            pass
        return n
  
    def selection2(self):
        choice2 = var2.get()
        c = choice2
        return c
    
    def precioTotal(self):
        choice = var.get()
        choice1 = var1.get()
        choice2 = var2.get()
        
        if ((choice == 1) and (choice1 == 1)):
            p = 5
        elif ((choice == 1) and (choice1 == 2)):
            p = 15
        elif ((choice == 1) and (choice1 == 3)):
            p = 25
       
        elif ((choice == 2) and (choice1 == 1)):
            p = 10
        elif ((choice == 2) and (choice1 == 2)):
            p = 20
        elif ((choice == 2) and (choice1 == 3)):
            p = 30  
        
        elif ((choice == 3) and (choice1 == 1)):
            p = 15
        elif ((choice == 3) and (choice1 == 2)):
            p = 25
        elif ((choice == 3) and (choice1 == 3)):
            p = 35  
       
        elif ((choice == 4) and (choice1 == 1)):
            p = 20
        elif ((choice == 4) and (choice1 == 2)):
            p = 30
        elif ((choice == 4) and (choice1 == 3)):
            p = 40    
        else:
            pass
        p = (p * (int(choice2)))
        return p
    
        
    def tiempoTotal(self):
        choice = var.get()
        choice1 = var1.get()
        choice2 = var2.get()
        
        if ((choice == 1) and (choice1 == 1)):
            t = 1
        elif ((choice == 1) and (choice1 == 2)):
            t = 2
        elif ((choice == 1) and (choice1 == 3)):
            t = 3
       
        elif ((choice == 2) and (choice1 == 1)):
            t = 4
        elif ((choice == 2) and (choice1 == 2)):
            t = 5
        elif ((choice == 2) and (choice1 == 3)):
            t = 6  
        
        elif ((choice == 3) and (choice1 == 1)):
            t = 7
        elif ((choice == 3) and (choice1 == 2)):
            t = 8
        elif ((choice == 3) and (choice1 == 3)):
            t = 9  
       
        elif ((choice == 4) and (choice1 == 1)):
            t = 11
        elif ((choice == 4) and (choice1 == 2)):
            t = 12
        elif ((choice == 4) and (choice1 == 3)):
            t = 13      
        else:
            pass
        
        t = (t * (int(choice2)))
        
        return t
    
    
    def submit(self):
        m = self.selection()
        n = self.selection1()
        c = self.selection2()
        p = self.precioTotal()
        t = self.tiempoTotal()
        
        return messagebox.showinfo('Resultados', f'Pedido de boceto: \n \n Tamaño: {m} \n Fondo: {n} \n Personajes: {c} \n\n Precio total: $ {p} USD \n Tiempo total: {t} días')


    
class pintura(estimadosinfo):
    
    def __init__(self,master):
        
        #frame
        global fr_estimadosinfo  , fr_pinturainfo
        super().__init__(fr_estimadosinfo)
        fr_estimadosinfo =tk.Frame(master)
        fr_pinturainfo =Label(master)
       
        #label
        self.label = tk.Label(fr_estimadosinfo,text="Estimados",font='bold')
        self.label.grid(row=0, column=1, sticky="n",padx=5, pady=5)
        
        #contents
        self.frame1 = Label(fr_pinturainfo)
        self.frame1.pack()
        Label(self.frame1, text="Pintura:").grid(row=0,column=4,sticky="ew")
        self.frame2 = LabelFrame(self.frame1, text='Tamaño', padx=30, pady=5)
        self.frame3 = LabelFrame(self.frame1, text='Fondo', padx=30, pady=5)
        self.frame4 = LabelFrame(self.frame1, text='Personajes',padx=30,pady=5)
        global var3, var4, var5
        var3 = IntVar()
        var4 = IntVar()
    
        Radiobutton(self.frame2, text='rostro', variable=var3, value=1,command=self.selection).pack()
        Radiobutton(self.frame2, text='busto', variable=var3, value=2,command=self.selection).pack()
        Radiobutton(self.frame2, text='cintura', variable=var3, value=3,command=self.selection).pack()
        Radiobutton(self.frame2, text='cuerpo completo', variable=var3, value=4,command=self.selection).pack()
    
        Radiobutton(self.frame3, text='transparente', variable=var4, value=1,command=self.selection1).pack()
        Radiobutton(self.frame3, text='sencillo', variable=var4, value=2,command=self.selection1).pack()
        Radiobutton(self.frame3, text='complejo', variable=var4, value=3,command=self.selection1).pack()

        Label(self.frame4, text="Cantidad:").grid(row=0,column=1)

    
        var5 = Entry(self.frame4, width = 5)
        var5.grid(row=1, column=1, columnspan=30)

        self.frame2.grid(row=4, column=4,padx=30)
        self.frame3.grid(row=5, column=4,padx=30)
        self.frame4.grid(row=6, column=4,padx=30)
        
        self.submit_btn = Button(self.frame1, text="Submit", command=self.submit, padx=50, pady=5)
        self.submit_btn.grid(row=7, column=4, pady=2)

    

    def selection(self):
        choice3 = var3.get()
        
        if choice3 == 1:
            m1 = 'rostro'
        elif choice3 == 2:
            m1 = 'busto'
        elif choice3 == 3:
            m1 = 'cintura'
        elif choice3 == 4:
            m1 = 'cuerpo completo'
        else:
            pass
        return m1

    def selection1(self):
        choice4 = var4.get()
        
        if choice4 == 1:
            n1 = 'transparente'
        elif choice4 == 2:
            n1 = 'sencillo'
        elif choice4 == 3:
            n1 = 'complejo'
        else:
            pass
        return n1
  
    def selection2(self):
        choice5 = var5.get()
        c1 = choice5
        return c1
    
    def precioTotal(self):
        choice3 = var3.get()
        choice4 = var4.get()
        choice5 = var5.get()
        
        if ((choice3 == 1) and (choice4 == 1)):
            p1 = 30
        elif ((choice3 == 1) and (choice4 == 2)):
            p1 = 40
        elif ((choice3 == 1) and (choice4 == 3)):
            p1 = 50
       
        elif ((choice3 == 2) and (choice4 == 1)):
            p1 = 45
        elif ((choice3 == 2) and (choice4 == 2)):
            p1 = 55
        elif ((choice3 == 2) and (choice4 == 3)):
            p1 = 65  
        
        elif ((choice3 == 3) and (choice4 == 1)):
            p1 = 50
        elif ((choice3 == 3) and (choice4 == 2)):
            p1 = 60
        elif ((choice3 == 3) and (choice4 == 3)):
            p1 = 70  
       
        elif ((choice3 == 4) and (choice4 == 1)):
            p1 = 70
        elif ((choice3 == 4) and (choice4 == 2)):
            p1 = 80
        elif ((choice3 == 4) and (choice4 == 3)):
            p1 = 90    
        else:
            pass
        p1 = (p1 * (int(choice5)))
        return p1
    
        
    def tiempoTotal(self):
        choice3 = var3.get()
        choice4 = var4.get()
        choice5 = var5.get()
        
        if ((choice3 == 1) and (choice4 == 1)):
            t1 = 5
        elif ((choice3 == 1) and (choice4 == 2)):
            t1 = 6
        elif ((choice3 == 1) and (choice4 == 3)):
            t1 = 7
       
        elif ((choice3 == 2) and (choice4 == 1)):
            t1 = 8
        elif ((choice3 == 2) and (choice4 == 2)):
            t1 = 9
        elif ((choice3 == 2) and (choice4 == 3)):
            t1 = 10  
        
        elif ((choice3 == 3) and (choice4 == 1)):
            t1 = 11
        elif ((choice3 == 3) and (choice4 == 2)):
            t1 = 12
        elif ((choice3 == 3) and (choice4 == 3)):
            t1 = 13  
       
        elif ((choice3 == 4) and (choice4 == 1)):
            t1 = 14
        elif ((choice3 == 4) and (choice4 == 2)):
            t1 = 15
        elif ((choice3 == 4) and (choice4 == 3)):
            t1 = 16      
            
        else:
            pass
        
        t1 = (t1 * (int(choice5)))
        
        return t1
    
    
    def submit(self):
        m1 = self.selection()
        n1 = self.selection1()
        c1 = self.selection2()
        p1 = self.precioTotal()
        t1 = self.tiempoTotal()
        
        return messagebox.showinfo('Resultados', f'Pedido de pintura: \n \n Tamaño: {m1} \n Fondo: {n1} \n Personajes: {c1} \n\n Precio total: $ {p1} USD \n Tiempo total: {t1} días')
    
    
        
    
        

       
obj = menu(window) 
obj1 = inicioinfo(window)
obj2 = galeriainfo(window)
obj3 = cominfo(window)
obj4 = tosinfo(window)
obj5 = estimadosinfo(window)
obj6 = boceto(window)
obj7 = pintura(window)

window.geometry("710x470")
window.mainloop()
    
    
#%%

  