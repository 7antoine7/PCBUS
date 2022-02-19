from cProfile import label
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

arrowResizeX = int(90)
arrowResizeY = int(20/15*arrowResizeX)
squareButtonResize = int(arrowResizeX)
rectangleButtonResizeX = int(3/2*arrowResizeX)
rectangleButtonResizeY = int(17/30*rectangleButtonResizeX)

jogXup_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/up_X_arrow.png').resize((arrowResizeX,arrowResizeY), Image.ANTIALIAS))
jogXdown_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/down_X_arrow.png').resize((arrowResizeX,arrowResizeY), Image.ANTIALIAS))
jogYup_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/up_Y_arrow.png').resize((arrowResizeY,arrowResizeX), Image.ANTIALIAS))
jogYdown_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/down_Y_arrow.png').resize((arrowResizeY,arrowResizeX), Image.ANTIALIAS))
jogZup_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/up_Z_arrow.png').resize((arrowResizeX,arrowResizeY), Image.ANTIALIAS))
jogZdown_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/down_Z_arrow.png').resize((arrowResizeX,arrowResizeY), Image.ANTIALIAS))
homeXY_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/home_button.png').resize((squareButtonResize,squareButtonResize), Image.ANTIALIAS))
mesh_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/mesh_button.png').resize((squareButtonResize,squareButtonResize), Image.ANTIALIAS))
modeAuto_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/mode_auto.png').resize((rectangleButtonResizeX,rectangleButtonResizeY), Image.ANTIALIAS)) 
modeMan_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/mode_manuel.png').resize((rectangleButtonResizeX,rectangleButtonResizeY), Image.ANTIALIAS)) 
modeSingle_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/mode_cycle.png').resize((rectangleButtonResizeX,rectangleButtonResizeY), Image.ANTIALIAS))
eStop_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/e-stop.png').resize((200,200), Image.ANTIALIAS)) 
arrowUp_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/up_arrow.png').resize((arrowResizeX,arrowResizeY), Image.ANTIALIAS)) 
arrowDown_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/down_arrow.png').resize((arrowResizeX,arrowResizeY), Image.ANTIALIAS))
play_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/play_button.png').resize((squareButtonResize,squareButtonResize), Image.ANTIALIAS))
pause_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/pause_button.png').resize((squareButtonResize,squareButtonResize), Image.ANTIALIAS))
stop_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/stop_button.png').resize((squareButtonResize,squareButtonResize), Image.ANTIALIAS))

bdwith = 0
font = ("Arial", 24)

jogXup_btn = Button(root, image=jogXup_img, borderwidth=bdwith)
jogXdown_btn = Button(root, image=jogXdown_img, borderwidth=bdwith)
jogYup_btn = Button(root, image=jogYup_img, borderwidth=bdwith)
jogYdown_btn = Button(root, image=jogYdown_img, borderwidth=bdwith)
jogZup_btn = Button(root, image=jogZup_img, borderwidth=bdwith)
jogZdown_btn = Button(root, image=jogZdown_img, borderwidth=bdwith)
homeXY_btn = Button(root, image=homeXY_img, borderwidth=bdwith)
mesh_btn = Button(root, image=mesh_img, borderwidth=bdwith)
modeAuto_btn = Button(root, image=modeAuto_img, borderwidth=bdwith) 
modeMan_btn = Button(root, image=modeMan_img, borderwidth=bdwith)
modeSingle_btn = Button(root, image=modeSingle_img, borderwidth=bdwith)
eStop_btn = Button(root, image=eStop_img, borderwidth=bdwith)
arrowUp_btn = Button(root, image=arrowUp_img, borderwidth=bdwith)
arrowDown_btn = Button(root, image=arrowDown_img, borderwidth=bdwith)
play_btn = Button(root, image=play_img, borderwidth=bdwith)
pause_btn = Button(root, image=pause_img, borderwidth=bdwith)
stop_btn =  Button(root, image=stop_img, borderwidth=bdwith)

incrementX_ddm = OptionMenu(root, incrementX_var, *incrementXY_list)
incrementY_ddm = OptionMenu(root, incrementY_var, *incrementXY_list)
incrementZ_ddm = OptionMenu(root, incrementZ_var, *incrementZ_list)

incrementX_lbl = Label(root,text="Incréments X :", font=font, width=12, anchor='w')
incrementY_lbl = Label(root,text="Incréments Y :", font=font, width=12, anchor='w')
incrementZ_lbl = Label(root,text="Incréments Z :", font=font, width=12, anchor='w')
machineStatus_lbl = Label(root,text="Machine Status", font=font, width=12, anchor='w')
X_lbl = Label(root, text="X", font=font)
Y_lbl = Label(root, text="Y", font=font)
Z_lbl = Label(root, text="Z", font=font)
position_lbl = Label(root, text="Position", font=font)
distanceToGo_lbl = Label(root, text="Distance to Go", font=font)

jogXup_btn.place(x=120,y=0)
jogXdown_btn.place(x=120,y=210)
jogYup_btn.place(x=0,y=120)
jogYdown_btn.place(x=210,y=110)
jogZup_btn.place(x=345,y=0)
jogZdown_btn.place(x=345,y=210)
homeXY_btn.place(x=120,y=120)
mesh_btn.place(x=345,y=120)

incrementX_lbl.place(x=50, y=355)
incrementX_ddm.place(x=280, y=360)
incrementY_lbl.place(x=50, y=405)
incrementY_ddm.place(x=280, y=410)
incrementZ_lbl.place(x=50, y=455)
incrementZ_ddm.place(x=280, y=460)

modeAuto_btn.place(x=10, y=525)
modeMan_btn.place(x=155, y=525)
modeSingle_btn.place(x=300, y=525)

play_btn.place(x=35, y=625)
pause_btn.place(x=180, y=625)
stop_btn.place(x=325, y=625)

# machineStatus_lbl.grid(row=0,column=4, columnspan=3)
# position_lbl.grid(row=1,column=5)
# distanceToGo_lbl.grid(row=1,column=6)
# X_lbl.grid(row=2,column=4)
# Y_lbl.grid(row=3,column=4)
# Z_lbl.grid(row=4,column=4)

# eStop_btn.grid(row=4, column=4)


root.mainloop()
