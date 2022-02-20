from cgitb import text
from tkinter import *
from PIL import ImageTk, Image
import os

# get directory
directoryPath = os.path.dirname(__file__)
assetsPath = os.path.abspath(os.path.join(
    os.path.join(directoryPath, os.pardir), "assets"))


root = Tk()
root.title("PCBUS")
root.geometry("1920x1080")

incrementXY_list = ["0.1 mm", "1 mm", "10 mm"]
incrementZ_list = ["0.001 mm", "0.01 mm", "0.1 mm"]

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

<<<<<<< HEAD
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
arrowUp_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/up_arrow.png').resize((int(arrowResizeX/2),int(arrowResizeY/2)), Image.ANTIALIAS)) 
arrowDown_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/down_arrow.png').resize((int(arrowResizeX/2),int(arrowResizeY/2)), Image.ANTIALIAS))
play_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/play_button.png').resize((squareButtonResize,squareButtonResize), Image.ANTIALIAS))
pause_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/pause_button.png').resize((squareButtonResize,squareButtonResize), Image.ANTIALIAS))
stop_img = ImageTk.PhotoImage(Image.open('C:/Users/rbiss/Documents/Universite de Sherbrooke/Etudes/Session 4/PCBUS/assets/stop_button.png').resize((squareButtonResize,squareButtonResize), Image.ANTIALIAS))
=======
jogXup_img = ImageTk.PhotoImage(Image.open(
    assetsPath + '/up_X_arrow.png').resize((arrowResizeX, arrowResizeY), Image.ANTIALIAS))
jogXdown_img = ImageTk.PhotoImage(Image.open(
    assetsPath + '/down_X_arrow.png').resize((arrowResizeX, arrowResizeY), Image.ANTIALIAS))
jogYup_img = ImageTk.PhotoImage(Image.open(
    assetsPath + '/up_Y_arrow.png').resize((arrowResizeY, arrowResizeX), Image.ANTIALIAS))
jogYdown_img = ImageTk.PhotoImage(Image.open(
    assetsPath + '/down_Y_arrow.png').resize((arrowResizeY, arrowResizeX), Image.ANTIALIAS))
jogZup_img = ImageTk.PhotoImage(Image.open(
    assetsPath + '/up_Z_arrow.png').resize((arrowResizeX, arrowResizeY), Image.ANTIALIAS))
jogZdown_img = ImageTk.PhotoImage(Image.open(
    assetsPath + '/down_Z_arrow.png').resize((arrowResizeX, arrowResizeY), Image.ANTIALIAS))
homeXY_img = ImageTk.PhotoImage(Image.open(assetsPath + '/home_button.png').resize(
    (squareButtonResize, squareButtonResize), Image.ANTIALIAS))
mesh_img = ImageTk.PhotoImage(Image.open(assetsPath + '/mesh_button.png').resize(
    (squareButtonResize, squareButtonResize), Image.ANTIALIAS))
modeAuto_img = ImageTk.PhotoImage(Image.open(assetsPath + '/mode_auto.png').resize(
    (rectangleButtonResizeX, rectangleButtonResizeY), Image.ANTIALIAS))
modeMan_img = ImageTk.PhotoImage(Image.open(assetsPath + '/mode_manuel.png').resize(
    (rectangleButtonResizeX, rectangleButtonResizeY), Image.ANTIALIAS))
modeSingle_img = ImageTk.PhotoImage(Image.open(assetsPath + '/mode_cycle.png').resize(
    (rectangleButtonResizeX, rectangleButtonResizeY), Image.ANTIALIAS))
eStop_img = ImageTk.PhotoImage(Image.open(
    assetsPath + '/e-stop.png').resize((200, 200), Image.ANTIALIAS))
arrowUp_img = ImageTk.PhotoImage(Image.open(
    assetsPath + '/up_arrow.png').resize((arrowResizeX, arrowResizeY), Image.ANTIALIAS))
arrowDown_img = ImageTk.PhotoImage(Image.open(
    assetsPath + '/down_arrow.png').resize((arrowResizeX, arrowResizeY), Image.ANTIALIAS))
play_img = ImageTk.PhotoImage(Image.open(assetsPath + '/play_button.png').resize(
    (squareButtonResize, squareButtonResize), Image.ANTIALIAS))
pause_img = ImageTk.PhotoImage(Image.open(assetsPath + '/pause_button.png').resize(
    (squareButtonResize, squareButtonResize), Image.ANTIALIAS))
stop_img = ImageTk.PhotoImage(Image.open(assetsPath + '/stop_button.png').resize(
    (squareButtonResize, squareButtonResize), Image.ANTIALIAS))
>>>>>>> 023c40e4adc7a6fb112961b153ad772ed6cd59ac

bdwith = 0
fontPrincipal = ("Arial", 24)
fontSecondaire = ("Arial", 14)

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
stop_btn = Button(root, image=stop_img, borderwidth=bdwith)

incrementX_ddm = OptionMenu(root, incrementX_var, *incrementXY_list)
incrementX_ddm.config(bd=5, font=fontSecondaire, width=12)
incrementY_ddm = OptionMenu(root, incrementY_var, *incrementXY_list)
incrementY_ddm.config(bd=5, font=fontSecondaire, width=12)
incrementZ_ddm = OptionMenu(root, incrementZ_var, *incrementZ_list)
<<<<<<< HEAD
incrementZ_ddm.config(bd=5, font=fontSecondaire, width=12)

incrementX_lbl = Label(root,text="Incréments X :", font=fontPrincipal, width=12, anchor='w')
incrementY_lbl = Label(root,text="Incréments Y :", font=fontPrincipal, width=12, anchor='w')
incrementZ_lbl = Label(root,text="Incréments Z :", font=fontPrincipal, width=12, anchor='w')
machineStatus_lbl = Label(root,text="Machine Status :", font=fontPrincipal)
X_lbl = Label(root, text="X", font=fontPrincipal)
Y_lbl = Label(root, text="Y", font=fontPrincipal)
Z_lbl = Label(root, text="Z", font=fontPrincipal)
position_lbl = Label(root, text="Position :", font=fontPrincipal)
distanceToGo_lbl = Label(root, text="Distance to Go :", font=fontPrincipal)
speeds_lbl = Label(root, text="Speeds :", font=fontPrincipal)
feed_lbl = Label(root, text="Feed =", font=fontSecondaire)
spindle_lbl = Label(root, text="Spindle =", font=fontSecondaire)
overwrite_lbl = Label(root, text="Overwrite =", font=fontSecondaire)
overwrite1_lbl = Label(root, text="Overwrite :", font=fontPrincipal)
=======

incrementX_lbl = Label(root, text="Incréments X :",
                       font=font, width=12, anchor='w')
incrementY_lbl = Label(root, text="Incréments Y :",
                       font=font, width=12, anchor='w')
incrementZ_lbl = Label(root, text="Incréments Z :",
                       font=font, width=12, anchor='w')
machineStatus_lbl = Label(root, text="Machine Status",
                          font=font, width=12, anchor='w')
X_lbl = Label(root, text="X", font=font)
Y_lbl = Label(root, text="Y", font=font)
Z_lbl = Label(root, text="Z", font=font)
position_lbl = Label(root, text="Position", font=font)
distanceToGo_lbl = Label(root, text="Distance to Go", font=font)
>>>>>>> 023c40e4adc7a6fb112961b153ad772ed6cd59ac

jogXup_btn.place(x=120, y=0)
jogXdown_btn.place(x=120, y=210)
jogYup_btn.place(x=0, y=120)
jogYdown_btn.place(x=210, y=110)
jogZup_btn.place(x=345, y=0)
jogZdown_btn.place(x=345, y=210)
homeXY_btn.place(x=120, y=120)
mesh_btn.place(x=345, y=120)

incrementX_lbl.place(x=50, y=355)
incrementX_ddm.place(x=280, y=355)
incrementY_lbl.place(x=50, y=405)
incrementY_ddm.place(x=280, y=405)
incrementZ_lbl.place(x=50, y=455)
incrementZ_ddm.place(x=280, y=455)

modeAuto_btn.place(x=10, y=525)
modeMan_btn.place(x=155, y=525)
modeSingle_btn.place(x=300, y=525)

play_btn.place(x=35, y=625)
pause_btn.place(x=180, y=625)
stop_btn.place(x=325, y=625)

machineStatus_lbl.place(x=500, y=0)
position_lbl.place(x=560, y=50)
distanceToGo_lbl.place(x=760, y=50)
X_lbl.place(x=500, y=100)
Y_lbl.place(x=500, y=150)
Z_lbl.place(x=500, y=200)

speeds_lbl.place(x=500, y=300)
feed_lbl.place(x=525, y=350)
spindle_lbl.place(x=525, y=375)
overwrite_lbl.place(x=525, y=400)
overwrite1_lbl.place(x=700, y=300)
arrowUp_btn.place(x=750, y=350)
arrowDown_btn.place(x=750, y=415)

eStop_btn.place(x=900,y=525)


root.mainloop()
