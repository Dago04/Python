from tkinter import *

# iniciar tkinter
aplicacion = Tk()

# tamaño de la ventana

aplicacion.geometry('1060x560+0+0')

# evitar maximizar ventana
aplicacion.resizable(False, False)

# titulo de la venta
aplicacion.title('Restaurante - Sistema de facturación')

# color de fondo de la ventana
aplicacion.config(bg='burlywood')

# panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

# etiqueta titulo
etiqueta_titulo = Label(
    panel_superior, text='Sistema de Facturación', fg='azure4',
    font=('Dosis', 58), bg='burlywood', width=27)

etiqueta_titulo.grid(row=0, column=0)

# panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4', padx=80)
panel_costos.pack(side=BOTTOM)

# panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold '),
                           bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)
# panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold  '),
                           bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)
# panel postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold  '),
                           bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)


# panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)


# panel calculadora
panel_calculadora = Frame(panel_comidas, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack()

# panel reciibo
panel_reciibo = Frame(panel_comidas, bd=1, relief=FLAT, bg='burlywood')
panel_reciibo.pack()

# panel botones
panel_botones = Frame(panel_comidas, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()


# lista productos
lista_comidas = ['pollo', 'cordero', 'salmon',
                 'merluza', 'kebab', 'pizza', 'hamburguesa', 'pizza2']

lista_bebidas = ['agua', 'soda', 'jugo',
                 'vino1', 'vino2', 'cerveza1', 'cerveza2', 'té']

lista_postres = ['helado', 'fruta', 'brownies',
                 'flan', 'mousse', 'pastel1', 'pastel2', 'coco']

# Crea un Frame para los elementos de comida, bebida ypostres
frame_comidas = Frame(panel_comidas)
frame_comidas.pack()

frame_bebidas = Frame(panel_bebidas)
frame_bebidas.pack()

frame_postres = Frame(panel_postres)
frame_postres.pack()

# generar items comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:
    # crear checkbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(frame_comidas,
                         text=comida.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador])
    comida.grid(row=contador,
                column=0,
                sticky=W)

    # crear cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set(0)
    cuadros_comida[contador] = Entry(frame_comidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,
                                  column=1)
    contador += 1


variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebidas:
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(frame_bebidas,
                         text=bebida.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebida[contador])
    bebida.grid(row=contador, column=0, sticky=W)

    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set(0)
    cuadros_bebida[contador] = Entry(frame_bebidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador,
                                  column=1)

    contador += 1


variables_postres = []
cuadros_postre = []
texto_postre = []
contador = 0
for postre in lista_postres:
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postre = Checkbutton(frame_postres,
                         text=postre.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_postres[contador])

    postre.grid(row=contador,
                column=0,
                sticky=W)

    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set(0)
    cuadros_postre[contador] = Entry(frame_postres,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_postre[contador])
    cuadros_postre[contador].grid(row=contador,
                                  column=1)

    contador += 1


# variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

# etiquetas de costo y campos de entrada

etiqueta_costo_comida = Label(panel_costos,
                              text='Costo Comida',
                              fon=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos,
                           font=("Dosis", 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)

texto_costo_comida.grid(row=0, column=1, padx=41)


etiqueta_costo_bebida = Label(panel_costos,
                              text='Costo Bebida',
                              fon=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costos,
                           font=("Dosis", 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida)

texto_costo_bebida.grid(row=1, column=1, padx=41)


etiqueta_costo_postre = Label(panel_costos,
                              text='Costo postre',
                              fon=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_costo_postre.grid(row=2, column=0)

texto_costo_postre = Entry(panel_costos,
                           font=("Dosis", 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postre)

texto_costo_postre.grid(row=2, column=1, padx=41)

etiqueta_subtotal = Label(panel_costos,
                          text='Costo subtotal',
                          fon=('Dosis', 12, 'bold'),
                          bg='azure4',
                          fg='white')

etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_costos,
                       font=("Dosis", 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=var_subtotal)

texto_subtotal.grid(row=0, column=3, padx=41)


etiqueta_impuesto = Label(panel_costos,
                          text='Costo Impuesto',
                          fon=('Dosis', 12, 'bold'),
                          bg='azure4',
                          fg='white')

etiqueta_impuesto.grid(row=1, column=2)

texto_impuesto = Entry(panel_costos,
                       font=("Dosis", 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=var_impuesto)

texto_impuesto.grid(row=1, column=3, padx=41)

etiqueta_total = Label(panel_costos,
                       text='Costo Total',
                       fon=('Dosis', 12, 'bold'),
                       bg='azure4',
                       fg='white')

etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costos,
                    font=("Dosis", 12, 'bold'),
                    bd=1,
                    width=10,
                    state='readonly',
                    textvariable=var_total)

texto_total.grid(row=2, column=3, padx=41)

# subtotalvitar que la pantalla se cierre
aplicacion.mainloop()
