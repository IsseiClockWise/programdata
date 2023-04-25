import tkinter

window = tkinter.Tk()
window.title(u' タイトル ')

label = tkinter.Label(window, text='Hello World')
label.grid()

button = tkinter.Button(window, text=" クリックしてね ")
button.grid()

window.geometry('320x240')

window.mainloop()
