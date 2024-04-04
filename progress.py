from tkinter import *
from tkinter.ttk import *
import ttkbootstrap as ttk
from PIL import Image, ImageTk
import time

window = ttk.Window(themename = 'darkly')
window.title('Instalaciones electricas')
window.iconbitmap('elec.ico')
window_w = 300
window_h = 400
display_w = window.winfo_screenwidth()
display_h = window.winfo_screenheight()
left = int(display_w / 2 - window_w / 2)
top = int(display_h / 2 - window_h / 2)
window.geometry(f'{window_w}x{window_h}+{left}+{top}')
window.resizable(False, False)
window.bind('<Escape>', lambda event: window.quit())

image_original = Image.open('panas.jpg').resize((220, 240))
image_tk = ImageTk.PhotoImage(image_original)
label = ttk.Label(master = window, image = image_tk)
label.place(x = 36, y = 30)

def start():
    GB = 100
    download = 0
    speed = 1
    while(download<GB):
        time.sleep(0.05)
        bar['value']+=(speed/GB)*100
        download+=speed
        percent.set(str(int((download/GB)*100))+"%")
        text.set(str(download)+"/"+str(GB)+" GB completed")
        window.update_idletasks()

percent = StringVar()
text = StringVar()

bar = Progressbar(window,orient=HORIZONTAL,length=300)
bar.place(y = 295, height = 28)

percentLabel = Label(window,textvariable=percent)
percentLabel.place(x = 500, y = 500)
taskLabel = Label(window,textvariable=text)
taskLabel.place(x = 500, y = 500)

button = Button(window,text="Iniciar",command=start)
button.place(x = 120 , y = 340)

window.mainloop()

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
splash_screen.destroy()