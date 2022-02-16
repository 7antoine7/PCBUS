from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("PCBUS")
root.geometry("1920x1080")

incrementXY_list = ["0.1 mm","1 mm","10 mm"]
incrementZ_list = ["0.001 mm","0.01 mm","0.1 mm"]

incrementX_var = StringVar(root)
incrementX_var.set(incrementXY_list[0])
incrementY_var = StringVar(root)
incrementY_var.set(incrementXY_list[0])
incrementZ_var = StringVar(root)
incrementZ_var.set(incrementZ_list[0])

jogXup_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/up_X_arrow.png').resize((150,150), Image.ANTIALIAS))
jogXdown_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/down_X_arrow.png').resize((150,150), Image.ANTIALIAS))
jogYup_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/up_Y_arrow.png').resize((150,150), Image.ANTIALIAS))
jogYdown_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/down_Y_arrow.png').resize((150,150), Image.ANTIALIAS))
jogZup_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/up_Z_arrow.png').resize((150,150), Image.ANTIALIAS))
jogZdown_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/down_Z_arrow.png').resize((150,150), Image.ANTIALIAS))
homeXY_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/home_button.png').resize((150,150), Image.ANTIALIAS))
mesh_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/mesh_button.png').resize((150,150), Image.ANTIALIAS))
modeAuto_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/mode_auto.png').resize((100,100), Image.ANTIALIAS)) 
modeMan_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/mode_manuel.png').resize((100,100), Image.ANTIALIAS)) 
modeSingle_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/mode_cycle.png').resize((100,100), Image.ANTIALIAS))
eStop_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/e-stop.png').resize((200,200), Image.ANTIALIAS)) 
arrowUp_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/up_arrow.png').resize((100,100), Image.ANTIALIAS)) 
arrowDown_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/down_arrow.png').resize((100,100), Image.ANTIALIAS))
play_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/play_button.png').resize((100,100), Image.ANTIALIAS))
pause_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/pause_button.png').resize((100,100), Image.ANTIALIAS))
stop_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/stop_button.png').resize((100,100), Image.ANTIALIAS))


jogXup_btn = Button(root, image=jogXup_img, borderwidth=0)
jogXdown_btn = Button(root, image=jogXdown_img, borderwidth=0)
jogYup_btn = Button(root, image=jogYup_img, borderwidth=0)
jogYdown_btn = Button(root, image=jogYdown_img, borderwidth=0)
jogZup_btn = Button(root, image=jogZup_img, borderwidth=0)
jogZdown_btn = Button(root, image=jogZdown_img, borderwidth=0)
homeXY_btn = Button(root, image=homeXY_img, borderwidth=0)
mesh_btn = Button(root, image=mesh_img, borderwidth=0)
modeAuto_btn = Button(root, image=modeAuto_img, borderwidth=0) 
modeMan_btn = Button(root, image=modeMan_img, borderwidth=0)
modeSingle_btn = Button(root, image=modeSingle_img, borderwidth=0)
eStop_btn = Button(root, image=eStop_img, borderwidth=0)
arrowUp_btn = Button(root, image=arrowUp_img, borderwidth=0)
arrowDown_btn = Button(root, image=arrowDown_img, borderwidth=0)
play_btn = Button(root, image=play_img, borderwidth=0)
pause_btn = Button(root, image=pause_img, borderwidth=0)
stop_btn =  Button(root, image=stop_img, borderwidth=0)

incrementX_ddm = OptionMenu(root, incrementX_var, *incrementXY_list)
incrementY_ddm = OptionMenu(root, incrementY_var, *incrementXY_list)
incrementZ_ddm = OptionMenu(root, incrementZ_var, *incrementXY_list)

incrementX_lbl = Label(root,text="Incréments X :", font=("Arial", 24), padx=5)
incrementY_lbl = Label(root,text="Incréments Y :", font=("Arial", 24), padx=5)
incrementZ_lbl = Label(root,text="Incréments Z :", font=("Arial", 24), padx=5)

jogXup_btn.grid(row=0, column=1)
jogXdown_btn.grid(row=2, column=1)
jogYup_btn.grid(row=1, column=0)
jogYdown_btn.grid(row=1, column=2)
jogZup_btn.grid(row=0, column=3)
jogZdown_btn.grid(row=2, column=3)
homeXY_btn.grid(row=1, column=1)
mesh_btn.grid(row=1, column=3)

incrementX_lbl.grid(row=3, column=1)
incrementX_ddm.grid(row=3, column=2)
incrementY_lbl.grid(row=4, column=1)
incrementY_ddm.grid(row=4, column=2)
incrementZ_lbl.grid(row=5, column=1)
incrementZ_ddm.grid(row=5, column=2)

modeAuto_btn.grid(row=6, column=0)
modeMan_btn.grid(row=6, column=1)
modeSingle_btn.grid(row=6, column=2)

play_btn.grid(row=7, column=0)
pause_btn.grid(row=7, column=1)
stop_btn.grid(row=7, column=2)

eStop_btn.grid(row=4, column=4)


root.mainloop()
