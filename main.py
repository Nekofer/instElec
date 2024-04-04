import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
import numpy as np
from tkinter import *
from PIL import Image, ImageTk
import time
import subprocess
import matplotlib.pyplot as plt


# Crear la ventana Splash Screen
splash_screen = ttk.Window(themename = 'darkly')


# Configurar la ventana Splash Screen
splash_screen.overrideredirect(True)
splash_w = 300
splash_h = 400
sdisplay_w = splash_screen.winfo_screenwidth()
sdisplay_h = splash_screen.winfo_screenheight()
left = int(sdisplay_w / 2 - splash_w / 2)
top = int(sdisplay_h / 2 - splash_h / 2)
splash_screen.geometry(f'{splash_w}x{splash_h}+{left}+{top}')
splash_screen.resizable(False, False)


# Agregar una imagen de fondo a la ventana Splash Screen
image_original = Image.open('panas.jpg').resize((220, 240))
image_tk = ImageTk.PhotoImage(image_original)
label = ttk.Label(master = splash_screen, image = image_tk)
label.place(x = 36, y = 30)


# Mostrar la ventana Splash Screen durante unos segundos
splash_screen.update()
time.sleep(3)


# Cerrar la ventana Splash Screen
splash_screen.withdraw()
splash_screen.destroy() #quitar


def button_func():
    R = float(entryR.get())
    L = float(entryL.get())
    C = float(entryC.get())
    f = float(entryF.get())
    V = float(entryV.get())

    w = 2 * np.pi * f
    Z_R = R
    Z_L = w * L * 1j
    Z_C = 1 / (w * C * 1j)
    Z_total = Z_R + Z_L + Z_C

    I = np.abs(V / Z_total)
    phi = np.angle(Z_total)

    P = V * I * np.cos(phi)
    Q = V * I * np.sin(phi)
    S = V * I
    PF = np.cos(phi)

    # Calcula las coordenadas rectangulares, polares y exponenciales de la impedancia total
    Z_rectangular = np.real(Z_total) + np.imag(Z_total) * 1j
    Z_polar = np.abs(Z_total) * np.exp(1j * np.angle(Z_total))
    Z_exponencial = np.abs(Z_total) * np.exp(np.angle(Z_total) * 1j)

    # widgets results
    labelZ = ttk.Label(master = window, text = "Impedancia total: {:.2f} Ohm".format(np.abs(Z_total)), font = 'Arial 16')
    labelI = ttk.Label(master = window, text = "Corriente: {:.2f} A, Desfase: {:.2f} rad".format(I, phi), font = 'Arial 16')
    labelP = ttk.Label(master = window, text = "Potencia activa: {:.2f} W".format(P), font = 'Arial 16')
    labelQ = ttk.Label(master = window, text = "Potencia reactiva: {:.2f} VAR".format(Q), font = 'Arial 16')
    labelS = ttk.Label(master = window, text = "Potencia aparente: {:.2f} VA".format(S), font = 'Arial 16')
    labelPF = ttk.Label(master = window, text = "Factor de potencia: {:.2f}".format(PF), font = 'Arial 16')
    labelZr = ttk.Label(master = window, text ="Coordenadas rectangulares: {:.2f} + {:.2f}j Ohm".format(np.real(Z_total), np.imag(Z_total)), font = 'Arial 16')
    labelZp = ttk.Label(master = window, text = "Coordenadas polares: {:.2f} Ohm, {:.2f} rad".format(np.abs(Z_total), np.angle(Z_total)), font = 'Arial 16')
    labelZe = ttk.Label(master = window, text = "Coordenadas exponenciales: {:.2f} exp({:.2f}j rad)".format(np.abs(Z_total), np.angle(Z_total)), font = 'Arial 16')

    # places
    labelZ.place(x = 30, y = 350)
    labelI.place(x = 30, y=390)
    labelP.place(x=30, y=430)
    labelQ.place(x=30, y=470)
    labelS.place(x=30, y=510)
    labelPF.place(x=30, y=550)
    labelZr.place(x=330,y=350)
    labelZp.place(x=400, y=390)
    labelZe.place(x=330, y=430)

    t = np.linspace(0, 1e-3, 1000)

    # Graficar la impedancia en forma polar
    plt.subplot(2, 2, 1, polar=True)
    plt.plot([0, np.angle(Z_total)], [0, np.abs(Z_total)], 'b')
    plt.title('Impedancia')

    # Graficar la corriente en forma de flecha
    plt.subplot(2, 2, 2, polar=True)
    plt.arrow(0, 0, np.angle(I, deg=True), np.abs(I), width=0.03)
    plt.title('Corriente')

    # Graficar las potencias en un gráfico de barras
    plt.subplot(2, 2, 3)
    plt.bar(['Aparente', 'Reactiva', 'Real'], [P, Q, S])
    plt.ylabel('Potencia (W)')
    plt.title('Potencias')

    # Graficar el factor de potencia
    plt.subplot(2, 2, 4)
    plt.plot(PF, 'r')
    plt.ylim([-1, 1])
    plt.title('Factor de Potencia')

    # Mostrar todas las gráficas
    plt.show()

    # Results
    print("Impedancia total: {:.2f} Ohm".format(np.abs(Z_total)))
    print("Corriente: {:.2f} A, Desfase: {:.2f} rad".format(I, phi))
    print("Potencia activa: {:.2f} W".format(P))
    print("Potencia reactiva: {:.2f} VAR".format(Q))
    print("Potencia aparente: {:.2f} VA".format(S))
    print("Factor de potencia: {:.2f}".format(PF))
    print("Impedancia total:")
    print("Coordenadas rectangulares: {:.2f} + {:.2f}j Ohm".format(np.real(Z_total), np.imag(Z_total)))
    print("Coordenadas polares: {:.2f} Ohm, {:.2f} rad".format(np.abs(Z_total), np.angle(Z_total)))
    print("Coordenadas exponenciales: {:.2f} exp({:.2f}j rad)".format(np.abs(Z_total), np.angle(Z_total)))


def new_window(): #quitar
    askyesno = messagebox.askyesno('Instalaciones electricas', 'Desea crear una nueva ventana?')
    if askyesno:
        window.withdraw()
        extra = ttk.Toplevel()
        extra.title('Instalaciones electricas')
        extra.iconbitmap('elec.ico')
        extra_w = 850
        extra_h = 650
        edisplay_w = window.winfo_screenwidth()
        edisplay_h = window.winfo_screenheight()
        eleft = int(edisplay_w / 2 - extra_w / 2)
        etop = int(edisplay_h / 2 - extra_h / 2)
        extra.geometry(f'{extra_w}x{extra_h}+{eleft}+{etop}')

        # window size
        extra.resizable(False, False)

        # security event
        extra.bind('<Escape>', lambda event: window.quit())

        # menu
        menu = ttk.Menu(extra)

        # sub menu 1
        file_menu = ttk.Menu(menu, tearoff=False)
        file_menu.add_command(label='New', command=new_window)
        file_menu.add_command(label='Open', command=lambda: print('Open file'))
        menu.add_cascade(label='File', menu=file_menu)

        # sub menu 2
        help_menu = tk.Menu(menu, tearoff=False)
        help_menu.add_command(label='Help entry', command=lambda: print('Help'))
        menu.add_cascade(label='Help', menu=help_menu)

        extra.configure(menu=menu)

        # widgets
        labelR = ttk.Label(master=extra, text='Resistencia:', font='Arial 16')
        entryR = ttk.Entry(master=extra, font='Arial 16')
        labelC = ttk.Label(master=extra, text='Capacitancia:', font='Arial 16')
        entryC = ttk.Entry(master=extra, font='Arial 16')
        labelL = ttk.Label(master=extra, text='Inductancia:', font='Arial 16')
        entryL = ttk.Entry(master=extra, font='Arial 16')
        labelF = ttk.Label(master=extra, text='Frecuencia:', font='Arial 16')
        entryF = ttk.Entry(master=extra, font='Arial 16')
        labelV = ttk.Label(master=extra, text='Voltaje:', font='Arial 16')
        entryV = ttk.Entry(master=extra, font='Arial 16')
        button = ttk.Button(master=extra, text='Calcular', command=button_func)

        # places
        labelR.place(x=15, y=30)
        labelC.place(x=15, y=70)
        labelL.place(x=15, y=110)
        labelF.place(x=15, y=150)
        labelV.place(x=15, y=190)

        entryR.place(x=160, y=28, width=120)
        entryC.place(x=160, y=68, width=120)
        entryL.place(x=160, y=108, width=120)
        entryF.place(x=160, y=148, width=120)
        entryV.place(x=160, y=188, width=120)

        button.place(x=80, y=260, width=150, height=50)

        # import images
        image_original = Image.open('photo.png').resize((380, 280))
        image_tk = ImageTk.PhotoImage(image_original)
        label = ttk.Label(master=extra, image=image_tk)
        label.place(x=380, y=28)

        # run
        extra.mainloop()
    else:
        pass


def open_pdf():
    # Ruta del archivo PDF que se va a abrir
    file_path = "electric.pdf"

    # Abrir el archivo PDF con el visor predeterminado del sistema
    subprocess.call(["open", file_path]) #quitar

# window
window = ttk.Window(themename = 'darkly')
window.title('Instalaciones electricas')
window.iconbitmap('elec.ico')
window_w = 850
window_h = 650
display_w = window.winfo_screenwidth()
display_h = window.winfo_screenheight()
left = int(display_w / 2 - window_w / 2)
top = int(display_h / 2 - window_h / 2)
window.geometry(f'{window_w}x{window_h}+{left}+{top}')

# window size
window.resizable(False, False)

# security event
window.bind('<Escape>', lambda event: window.quit())

# menu
menu = ttk.Menu(window) #quitar

# sub menu 1
file_menu = ttk.Menu(menu, tearoff = False)
file_menu.add_command(label = 'New', command = new_window)
file_menu.add_command(label = 'Open', command = lambda : print('Open file'))
menu.add_cascade(label = 'File', menu = file_menu)

# sub menu 2
help_menu = tk.Menu(menu, tearoff = False)
help_menu.add_command(label = 'Help entry', command = open_pdf)
menu.add_cascade(label = 'Help', menu = help_menu)

window.configure(menu = menu) #quitar

# widgets
labelR = ttk.Label(master = window, text = 'Resistencia:', font = 'Arial 16')
entryR = ttk.Entry(master = window, font = 'Arial 16')
labelC = ttk.Label(master = window, text = 'Capacitancia:', font = 'Arial 16')
entryC = ttk.Entry(master = window, font = 'Arial 16')
labelL = ttk.Label(master = window, text = 'Inductancia:', font = 'Arial 16')
entryL = ttk.Entry(master = window, font = 'Arial 16')
labelF = ttk.Label(master = window, text = 'Frecuencia:', font = 'Arial 16')
entryF = ttk.Entry(master = window, font = 'Arial 16')
labelV = ttk.Label(master = window, text = 'Voltaje:', font = 'Arial 16')
entryV = ttk.Entry(master = window, font = 'Arial 16')
button = ttk.Button(master = window, text = 'Calcular', command = button_func)


# places
labelR.place(x = 15, y = 30)
labelC.place(x = 15, y = 70)
labelL.place(x = 15, y = 110)
labelF.place(x = 15, y = 150)
labelV.place(x = 15, y = 190)

entryR.place(x = 160, y = 28, width = 120)
entryC.place(x = 160, y = 68, width = 120)
entryL.place(x = 160, y = 108, width = 120)
entryF.place(x = 160, y = 148, width = 120)
entryV.place(x = 160, y = 188 , width=120)

button.place(x = 80, y = 260, width = 150, height = 50)


# import images
image_original = Image.open('photo.png').resize((380, 280))
image_tk = ImageTk.PhotoImage(image_original)
label = ttk.Label(master = window, image = image_tk)
label.place(x = 380, y = 28) #quitar


# run
window.mainloop()
