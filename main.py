from tkinter import *
import pyshorteners as p
import pyperclip as pc



x = ''
root = Tk()

# function to submit the user link
def submit():
    # print('enter your link:', end='')
    link = e1.get()
    s = p.Shortener()
    global x
    x = x+str(s.tinyurl.short(link))
    t1.insert(END, x)
    return



# function to copy the shortened url
def copy():

    pc.copy(x)
    root.destroy()



root.geometry('400x200')
root.title('URl shortener')
l1 = Label(root, text='Enter your URL here:')
l1.grid(row=0, column=0, padx=10, pady=10)
entry_text = StringVar()
e1 = Entry(root, textvariable=entry_text, width=20, bg='snow')
e1.grid(row=0, column=1, padx=10, pady=10)
b1 = Button(root, text='submit', bg='light grey', command=submit)
b1.grid(row=1, column=1, padx=10, pady=10)
b2 = Button(root, text='copy url', bg='light grey', command=copy)
b2.grid(row=3, column=1, padx=10, pady=10)
t1 = Text(root, width=30, height=1, bg='white')
t1.grid(row=2, column=1, padx=10, pady=10)
l2 = Label(root, text='shortened url:')
l2.grid(row=2, column=0, padx=10, pady=10)
root.configure(background='Lightskyblue1')
root.mainloop()
























