import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy

from keras.models import load_model

model = load_model("C:\\Users\\Foste\\Desktop\\Saved model\\Saved_model.h5")

classes = {
    0: 'Dog',
    1: 'Horse',
    2: 'Elephant',
    3: 'Butterfly',
    4: 'Chicken',
    5: 'Cat',
    6: 'Cow',
    7: 'Sheep',
    8: 'Spider',
    9: 'Squirrel'
}

def upload_image():
    file_path = filedialog.askopenfilename()
    uploaded = Image.open(file_path)
    uploaded.thumbnail(((root.winfo_width()/2.25),(root.winfo_height()/2.25)))
    im = ImageTk.PhotoImage(uploaded)
    sign_image.configure(image=im)
    sign_image.image = im
    label.configure(text=' ')
    show_classify_button(file_path)

def show_classify_button(file_path):
    classify_btn = Button(root, text="Classify Image", command =lambda: classify(file_path), padx=10, pady =5)
    classify_btn.configure(background = "white", foreground = "black", font=('arial', 10, 'bold'))
    classify_btn.place(relx = 0.79,rely=0.46)

def classify(file_path):
    image = Image.open(file_path)
    image = image.resize((180,180))
    image = numpy.expand_dims(image, axis = 0)
    image = numpy.array(image)
    pred = numpy.argmax(model.predict(image)[0], axis=-1)
    sign = classes[pred]
    print(sign)
    label.configure(foreground = 'white', text=sign)


root = tk.Tk()
root.geometry("700x700") # size of root frame.
root.title("Animal Classifier")
root.configure(background="#425080")


heading = Label(root,text = "Animal Classifier", font=('Verdana', 45, 'bold'))
heading.configure(background = '#425080', foreground = 'black')
heading.pack()

upload = Button(root, text = "Upload an image", command = upload_image, padx=10, pady=5)
upload.configure(background = "white", foreground = "black", font=('arial', 10, 'bold'))
upload.pack(side = BOTTOM, pady = 50)

sign_image = Label(root)
sign_image.pack(side = BOTTOM,expand = True)

label = Label(root, background = '#425080', font = ('arial', 25, 'bold'))
label.pack(side = BOTTOM, expand = True)

root.mainloop()