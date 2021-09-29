from tkinter import*
from ttkthemes import ThemedTk
import tkinter.ttk as ttk
from tkinter.font import Font
import pyqrcode
import png
from pyqrcode import QRCode

root = ThemedTk(theme="arc")
root.configure(background = "black")
root.title("QrTK")
root.geometry('779x35')
root.resizable(False , False)
def make():

        
    import string
    import random
    from urllib.parse import urlparse
    N = 7
    res = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k = N))
  
    x = urlparse(urle.get()).hostname
    url = pyqrcode.create(urle.get()) 
    url.png(x+'-'+str(res)+'.png', scale = 6)


urll = Label(root , width = 10 , text = "Enter Url : " , fg = "white" , bg = "black" , font = ("Microsoft PhagsPa" , 13))
urll.grid(row = 0 , column = 0)
text = StringVar()
text.set("Enter file name to be saved as")
urle = ttk.Entry(root ,  width = 62,font = ("Microsoft PhagsPa" , 13))
urle.grid(row = 0 , column = 1 , ipady = 2)
urlmake = ttk.Button(root , width = 13 , text = "Convert Url" , command = make)
urlmake.grid(row = 0 , column = 2,ipady = 2)

mainloop()
