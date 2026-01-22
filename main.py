from tkinter import *
from tkinter import messagebox as msg
from tkinter import filedialog as fd
import pyqrcode 
import png
from PIL import Image, ImageTk

#Title and Base Canvas
window = Tk()
window.title("Heaventica QRGenerator")
window.geometry("500x700")

#Icon Title
ico = Image.open("star.png")
photo = ImageTk.PhotoImage(ico)
window.wm_iconphoto("star.png", photo)

#Header
label = Label(window, text="QRGenerator", 
              font=("Dacherry", 36))
label.pack()

#Creating QR
def createQR():
    filepath = fd.asksaveasfilename(defaultextension='qrcode',
                                    initialfile= "qrcode",
                                    filetypes= [("PNG", '.png')])
    
    if filepath:
        if filepath.endswith('png'): 
            get_qr = pyqrcode.create(qr_generator.get())
            get_qr.png(filepath, scale= 5)     
            msg.showinfo(title="Success", message=f"QR Code saved on {filepath}")
        else:
            get_qr=f"{filepath}.png"
            get_qr.png(filepath, scale= 5)     
            msg.showinfo(title="Success", message=f"QR Code saved on {filepath} ")
            
        #Showing QR    
        global qr_preview
        qr_preview = ImageTk.PhotoImage(Image.open(filepath))
        qr_preview_label.config(image=qr_preview)

#Image of Chinatsu (wife)
chinatsu = Image.open("chinatsu.png").resize((260, 240))
chinatsu = ImageTk.PhotoImage(chinatsu)
image_label = Label(window, image= chinatsu)
image_label.pack(side= TOP, pady= 20)

#Inputing QR
qr_generator = Entry(window,
                font=("Arial", 12),
                width= 40,)
qr_generator.pack(side=TOP, padx=10, pady=10)   

#Save Button
save_file = Button(window,
                text="save", 
                command=createQR,
                pady= 5, padx= 20, bd= 5, relief=GROOVE)
save_file.pack(side= TOP, pady=10)

#Preview QR
qr_preview_label = Label(window, text="Your QR Preview:")
qr_preview_label.pack()



window.mainloop()