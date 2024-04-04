import tkinter as tk
from PIL import Image, ImageTk
import ttkbootstrap as ttk
import time


def main_function():
    splash_screen.destroy()  # Destruir la ventana del splash screen cuando se haya ejecutado la función principal
    # window
    window = ttk.Window(themename='darkly')
    window.title('Instalaciones electricas')
    window.iconbitmap('elec.ico')
    window_w = 1000
    window_h = 600
    display_w = window.winfo_screenwidth()
    display_h = window.winfo_screenheight()
    left = int(display_w / 2 - window_w / 2)
    top = int(display_h / 2 - window_h / 2)
    window.geometry(f'{window_w}x{window_h}+{left}+{top}')

    # window size
    window.resizable(False, False)

    # security event
    window.bind('<Escape>', lambda event: window.quit())

    # style
    style = ttk.Style()

    # menu
    menu = ttk.Menu(window)

    # sub menu 1
    file_menu = ttk.Menu(menu, tearoff=False)
    file_menu.add_command(label='New', command=new_window)
    file_menu.add_command(label='Open', command=lambda: print('Open file'))
    file_menu.add_separator()
    menu.add_cascade(label='File', menu=file_menu)

    # sub menu 2
    help_menu = tk.Menu(menu, tearoff=False)
    help_menu.add_command(label='Help entry', command=lambda: print('Help'))
    menu.add_cascade(label='Help', menu=help_menu)

    window.configure(menu=menu)

    # widgets
    labelR = ttk.Label(master=window, text='Resistencia:', font='Arial 24')
    entryR = ttk.Entry(master=window, font='Arial 24')
    labelC = ttk.Label(master=window, text='Capacitancia:', font='Arial 24')
    entryC = ttk.Entry(master=window, font='Arial 24')
    labelL = ttk.Label(master=window, text='Inductancia:', font='Arial 24')
    entryL = ttk.Entry(master=window, font='Arial 24')
    labelF = ttk.Label(master=window, text='Frecuencia:', font='Arial 24')
    entryF = ttk.Entry(master=window, font='Arial 24')
    button = ttk.Button(master=window, text='Calcular', command=button_func)

    # places
    labelR.place(x=20, y=50)
    labelC.place(x=20, y=150)
    labelL.place(x=20, y=250)
    labelF.place(x=20, y=350)

    entryR.place(x=220, y=45, width=120)
    entryC.place(x=220, y=145, width=120)
    entryL.place(x=220, y=245, width=120)
    entryF.place(x=220, y=345, width=120)

    button.place(x=125, y=460, width=150, height=50)

    # import images
    image_original = Image.open('photo.png').resize((380, 280))
    image_tk = ImageTk.PhotoImage(image_original)
    label = ttk.Label(master=window, image=image_tk)
    label.place(x=480, y=100)

    window.mainloop()



def close_splash_screen():
    splash_screen.withdraw()  # Ocultar la ventana del splash screen
    main_function()  # Ejecutar la función principal


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

# Configurar un temporizador para cerrar la ventana del splash screen después de un tiempo determinado
splash_screen.after(5000, close_splash_screen)

splash_screen.mainloop()


def button_func():
    pass


def new_window():
    pass


