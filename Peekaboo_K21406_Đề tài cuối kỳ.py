#khai báo thư viện
from googletrans import Translator
from tkinter import *
from PIL import Image, ImageTk

screen = Tk ()
screen.title ("Translation")
screen.geometry ("800x650")

image = Image.open ("hello.jpg")
image_load = ImageTk.PhotoImage(image)

image_screen = Label(image=image_load)
image_screen.place (x=0,y=0)

#clear
def clear_text():
    box1.delete(1.0,END)
    box2.delete(1.0,END)

#translate
def translate ():
    dict = Translator()
    text_translate =box1.get (1.0,END)
    dict_action = dict.translate(text=text_translate, src="en", dest="vi")
    box2.insert(1.0,dict_action.text)

tieu_de = Label(text=" Peekaboo Translation",font=(("Times new roman"),40))
tieu_de.pack(side=TOP)

#box
box1 = Text (font=(("Times new roman"),12),height=10,width=60)
box1.pack(pady=20)

box2 = Text (font=(("Times new roman"),12),height=10,width=60)
box2.pack(pady=60)

#button
translate_button=Button(text="Translate",font=(("Times new roman"),14),command=translate)
translate_button.place (x=50,y=300)

translate_clear=Button(text="Clear",font=(("Times new roman"),14),command=clear_text)
translate_clear.place (x=670,y=300)

screen.mainloop()

