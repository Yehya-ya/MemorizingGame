import tkinter as tk
import random
from tkinter import messagebox

ENTRY_X = 65
ENTRY_Y = 35
image_x = 1536
image_y = 756
NUM = 2
start_NUM = NUM
level = 1
b = []


class number:
    def __init__(self, count):
        self.count = count - (int(count/12) * 12)
        self.level = int(count/12) + 1
        self.label = tk.Label(canvas, text="", bg="White",
                              font=("Helvetica", 16))
        self.entry = tk.Entry(frame, bg="#ffffff", bd=5, fg="#1111ff",
                              font="Mistral 20", relief="flat", width=4, disabledbackground='#dddddd', state='disable', justify='center')

    def display_entry(self):
        self.entry.delete(0, 'end')
        level_all = int(NUM/12)+1
        if level_all > self.level:
            self.entry.place_configure(relx=(
                (self.count*2+1)/(12*2)), rely=(self.level) / (level_all+1), anchor='center')
        else:
            self.entry.place_configure(relx=((self.count*2+1)/(
                (NUM+1 - ((self.level-1)*12))*2)), rely=(self.level) / (level_all+1), anchor='center')

    def display_label(self):
        self.x = random.randint(0, 4)/10
        self.y = random.randint(0, 4)/10
        self.num = random.randint(0, 99)
        self.label.configure(text=str(self.num), bg='#ffffff')
        self.label.place_configure(relheight=0.18, relwidth=0.18, relx=(
            self.x*2)+0.01, rely=(self.y*2)+0.01)

    def delete_label(self):
        self.label.place_forget()

    def forget(self):
        self.entry.place_forget()


def show(lis, n):
    if n <= NUM:
        lis[n].display_label()
        print(lis[n].num)
        frame.after(1000, lambda: show2(lis, n))
    else:
        print("///////////////////////////////////")
        check_button.configure(stat='active')
        for i in lis:
            i.entry.configure(state='normal')


def show2(lis, n):
    lis[n].delete_label()
    show(lis, n+1)


def search(st):
    if st.isdigit():
        n = int(st)
        for i in b:
            if n == i.num:
                i.num = -1
                return True

    return False


def reset():
    global NUM, level, b
    for x in b:
        x.forget()
    b.clear()
    NUM = start_NUM
    level = 1
    for i in range(NUM+1):
        b.append(number(i))
        b[i].display_entry()


def add():
    global NUM, level
    NUM += 1
    level += 1
    b.append(number(NUM))


def check():
    global group, level
    flage = True
    for i in b:
        st = i.entry.get()
        if(st):
            if not search(st):
                if messagebox.askyesno("Game Over", "You Have lost...\nDo you  wan to retry ?"):
                    flage = False
                    reset()
                    break
                else:
                    w_exit()
                    return

        else:
            messagebox.showwarning(
                "Warning", "Please fill all the entries before you click the button")
            flage = False
            break

    if flage:
        messagebox.showinfo(
            "Good Work", "Congratulation!!!!!!\npress 'Ok' button to continue to the next level")
        add()
    group.configure(text="level " + str(level))
    check_button.configure(state='disable')
    for i in b:
        i.display_entry()
        i.entry.configure(state='disable')

    show(b, 0)


def w_exit():
    root.destroy()


def draw():
    ######## destroy the start menu #######

    start_canvas.destroy()

    ######## draw the Frames #########

    canvas.place(relwidth=0.8, relheight=0.7, relx=0.2, rely=0.0)
    canvas.create_image(image_x/2, image_y/2, image=image)
    frame.place(relwidth=0.8, relheight=0.3, relx=0.2, rely=0.7)
    frame_left.place(relwidth=0.2, relheight=1)

    ###### intialize first Numbers ######

    for x in range(NUM+1):
        b.append(number(x))
        b[x].display_entry()
    show(b, 0)

    ####### draw the left frame's components #######

    text_level.place(relx=0.5, rely=0.5, anchor='center')
    group.place(relheight=0.6, relwidth=1, relx=0, rely=0)
    check_button.place(relheight=0.08, relwidth=0.5,
                       relx=0.5, rely=0.8, anchor='center')
    exit_button.place(relheight=0.08, relwidth=0.5,
                      relx=0.5, rely=0.95, anchor='center')

####################### intialize #######################
# root #


root = tk.Tk()
root.wm_title(string="My Game")
root.minsize(height=700, width=1200)

# the frames #

canvas = tk.Canvas(root, height=image_y, width=image_x, bg='#000000')
image = tk.PhotoImage(file="photo.png")
frame = tk.Frame(root, bg="#191919", bd=10)
frame_left = tk.Frame(root, bg="#252525", bd=10)

# level frame #

group = tk.LabelFrame(frame_left, text="level 1", font=(
    "Mistral", 40), fg="#2222ff", bg="#252525", labelanchor='s', padx=0, pady=0)
text_level = tk.Label(group, text="\nWelcome to the:\n\nMEMORY GAME\n\n\n\n\n1. The first level will start with\na "+ str(NUM + 1) +" numbers' pattern \n\n2. In each level you pass the\npattern increases by 1\n\n3. By losing you will restart\nfrom the beginning", font=(
    "arial", 13), fg="#9999ff", bg='#252525')

# Buttons #

check_button = tk.Button(frame_left, text="Check",
                         font='arial 15', state='disable', command=check)
exit_button = tk.Button(frame_left, text="Exit", bg='#ff0000', fg='#ffffff',
                        activebackground='#ff0000', activeforeground='#ffffff', font='arial 15', command=w_exit)

####### the start menu ##########

start_canvas = tk.Canvas(root, height=1080, width=2194, bg='#000000')
start_canvas.place(relheight=1, relwidth=1)
image_M = tk.PhotoImage(file='photo_M.png')
start_canvas.create_image(2194/2, 1080/2, image=image_M)
start_button = tk.Button(start_canvas, text="start", font='arial 25',
                         bg='#222222', fg='#dddddd', command=draw, relief='flat')
start_button.place(relx=0.5, rely=0.72, relheight=0.1,
                   relwidth=0.4, anchor='center')
exit_button2 = tk.Button(start_canvas, text="Exit", bg='#ff0000', fg='#ffffff',
                         activebackground='#ff0000', activeforeground='#ffffff', font='arial 25', command=w_exit, relief='flat')
exit_button2.place(relheight=0.1, relwidth=0.4,
                   relx=0.5, rely=0.88, anchor='center')
text_t = tk.Label(start_canvas, text="MEMORY GAME", font=(
    "arial", 50), fg="#ff9999", bg='#000000')
text_d = tk.Label(start_canvas, text="This game is about memorizing patterns of numbers.\n\nIt starts with a pattern of "+ str(NUM + 1) +" numbers you have to fill the entries with those numbers.\n\nYou will pass the level If you memorized the numbers correctly\n\nOtherwise you will restart from the beginning", font=(
    "arial", 20), fg="#ff9999", bg='#000000')
text_t.place(relx=0.5, rely=0.2, anchor='center')
text_d.place(relx=0.5, rely=0.45, anchor='center')

root.mainloop()
