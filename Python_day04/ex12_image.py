from tkinter import Tk, PhotoImage, Label, Button

def img1() :
    newImg = PhotoImage(file="image01.png")
    imgLabel.config(image=newImg)
    imgLabel.image = newImg

def img2() :
    newImg = PhotoImage(file="image02.png")
    imgLabel.config(image=newImg)
    imgLabel.image = newImg

def img3() :
    newImg = PhotoImage(file="image03.png")
    imgLabel.config(image=newImg)
    imgLabel.image = newImg

win = Tk()

win.geometry("700x800+100+100")

image = PhotoImage(file="image01.png")
imgLabel = Label(win, image=image, width=500, height=700)

imgLabel.grid(row=0, column=0, columnspan=3)

btn01 = Button(win, text="그림1", command=img1)
btn02 = Button(win, text="그림2", command=img2)
btn03 = Button(win, text="그림3", command=img3)

btn01.grid(row=1, column=0)
btn02.grid(row=1, column=1)
btn03.grid(row=1, column=2)

if __name__ == '__main__' :
    win.mainloop()