
from tkinter import *

root=Tk()
root.title("Driving License")
root.geometry("300x400")

root.configure(bg="white")
canvas=Canvas(root,width=300,height=400)
canvas.create_image(0,0,anchor=NW)
canvas.create_rectangle(0, 0, 300, 55, fill="#1463B0")
canvas.create_rectangle(0, 345, 300, 400, fill="#1463B0")

label_heading = canvas.create_text(150,90, font=('Times', '24', 'bold italic') ,text="Driving License")
label_nametag = canvas.create_text(40,165, font=('Times', '16', 'bold') ,text="Name :")
label_Adress_tag = canvas.create_text(40,205, font=('Times', '16', 'bold') ,text="Address :")
label_ID_tag = canvas.create_text(50,250, font=('Times', '16', 'bold') ,text="ID :")

label_name = Label(root)
label_Address = Label(root)
label_ID = Label(root)

def myCardDetails():
    name = "Ibrahim"
    print(type(name))   
    Address = 9996965124
    print(type(Address))
    ID = ["6999768126488"]
    print(type(ID))
    
    label_name['text'] = name
    label_Address['text'] = Address
    label_ID['text'] = ID
    
    
button1 = Button(root, text = "Show my Driving ID", command=myCardDetails)

button1.configure(width = 20 , activebackground = "#9EC6EE", relief= FLAT)
button1_window = canvas.create_window(150, 330, anchor=CENTER, window=button1)
label_Name_window = canvas.create_window(120, 165, anchor=CENTER, window=label_name)
label_ID_window = canvas.create_window(90, 205, anchor=CENTER, window=label_ID)
label_Address_window = canvas.create_window(155, 252, anchor=CENTER, window=label_Address)
canvas.pack()

root.mainloop()