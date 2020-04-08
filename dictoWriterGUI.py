from tkinter import*
from tkinter import messagebox
try:
    from PIL import Image, ImageTk
except:
    try:
        response = messagebox.askyesno("Import Error", "Do you want to install missing Library?")
        # if response == "yes":
        #     os.system("sudo pip3 install Pillow")
        # else:
        #     messagebox.askyesno("Import Error", "Did not install missing Library!")
    except:
        messagebox.showinfo("Import Error", "Please install pillow library!")

myFont = "Courier"
myFontSize = 12
icon_path = "E:\Visual_Studio_Code\python\GUI\Dicto-Writter_small.ico"
captured_image_path = "E:\Visual_Studio_Code\python\GUI\Dicto-Writter_small.png"

in_s2t_main = " ."

in_t2s_main = " ."

myHelp = "For Step by step help please refer the following link:\r\nHACKERMINDS/Dicto-Writter\r\n(https://github.com/hackerminds/DICTO-WRITTER)"

myAbout = "Canara Engineering College\rAffiliated Visvesvaraya Technological University \n(VTU)\n\nThis is a final year project made by \r\nAmith Rayan Fernandes\t4CB16EC006\nMegha U Shenoy\t\t4CB16EC045\nN Hrishikesh Prabhu\t4CB16EC047\nP Shrivtsa Bhat\t\t4CB16EC055\r\n Under the Guidence of the Mr Vayusutha \n(Asst.Proffesor at Canara Engineering College)"

class ScrollableFrame(Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = Canvas(self)
        scrollbar = Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


def s2t_frame():
    def startMechine():
        startButton.config(state=DISABLED)
        stopButton.config(state=NORMAL)
        #print(checkButtonVar.get())
        textFrame = LabelFrame(MiddleFrame, font=(myFont, myFontSize) ,text="Conversion Output")
        textFrame.pack(fill="both", expand=True)

        # showText = Text(textFrame, width=720, height=280, padx=10, wrap=WORD, spacing1=1, spacing2=1, spacing3=1)
        # showText.insert(INSERT, "Text Widgetn20 characters widen3 lines high")#END or INSERT
        # showText.pack(fill="both", expand=True)

        showText = ScrollableFrame(textFrame)
        Text = Label(showText.scrollable_frame, padx=10, pady=5, justify=LEFT,font=(myFont, myFontSize) ,text=in_s2t_main)
        Text.pack(fill="both", expand=True)
        showText.pack(fill="both", expand=True)

    def stopMechine():
        startButton.config(state=NORMAL)
        stopButton.config(state=DISABLED)
        for widget in MiddleFrame.winfo_children(): #clear the frame
            widget.destroy()

    #s2t frame initialisation
    frame = Toplevel()
    frame.title("Speech to Text | Dicto Writter")
    frame.iconbitmap(icon_path)
    frame.geometry("720x480")

    #Create Base Frame
    defaultFrame = Frame(frame)
    defaultFrame.pack(fill="both", expand=True,  padx=1, pady=1)

    #Create Main Frame
    MainFrame = Frame(defaultFrame)
    MainFrame.pack(fill="both", expand=True)
    #Create Inner Widgets
    TopFrame = Frame(MainFrame, bd=5, width=720, height=80, padx=2, relief=RIDGE)#, bg="#f0f0f0")
    TopFrame.pack(fill="both", expand=True)

    # Check Box
    checkButtonVar = StringVar()
    feedBackOption =Checkbutton(TopFrame, text="Feedback", variable=checkButtonVar, onvalue="On", offvalue="Off")
    feedBackOption.deselect()
    feedBackOption.pack(side=RIGHT, padx=30, pady=10)

    #Button
    startButton = Button(TopFrame, text="Start", padx=20, pady=10, command=startMechine)
    startButton.pack(side=LEFT, padx=30, pady=10)

    stopButton = Button(TopFrame, text="Stop", padx=20, pady=10, state=DISABLED, command=stopMechine)
    stopButton.pack(side=LEFT, padx=30, pady=10)

    MiddleFrame = Frame(MainFrame, bd=5, width=720, height=280, padx=2, relief=RIDGE, bg="cadet blue")
    MiddleFrame.pack(fill="both", expand=True)

    ''' --------------------- Close Button --------------------- '''
    BottomFrame = Frame(defaultFrame, bd=1, relief=RIDGE, bg="#de1212")
    BottomFrame.pack(side=RIGHT, pady=10)
    Exit = Button(BottomFrame, text="Close", command=frame.destroy, fg="#ffffff", bg="#de1212", relief=FLAT)
    Exit.pack(padx=5, pady=5)


def t2s_frame():
    def showimage():
        #show captured image
        try:
            load = Image.open(captured_image_path)
            render = ImageTk.PhotoImage(load)
            frame = Toplevel()
            frame.title("Captured Image | Dicto Writter")
            frame.iconbitmap(icon_path)
            img = Label(frame, image=render)
            img.image = render
            img.place(x=0, y=0)
            showImage.config(state=DISABLED)
        except :
            response = messagebox.showwarning("Import Error", "Captured Image couldn't dispaly!")

    def captureimage():
        showImage.config(state=NORMAL)
        try:
            for widget in MiddleFrame.winfo_children():  # clear the frame
                widget.destroy()
        except:
            pass
        #capture and show text
        textFrame = LabelFrame(MiddleFrame, font=(myFont, myFontSize) ,text="Conversion Output")
        textFrame.pack(fill="both", expand=True)

        showText = ScrollableFrame(textFrame)
        Text = Label(showText.scrollable_frame, padx=10, pady=5, justify=LEFT,font=(myFont, myFontSize) ,text=in_t2s_main)
        Text.pack(fill="both", expand=True)
        showText.pack(fill="both", expand=True)

    #t2s frame initialisation
    frame = Toplevel()
    frame.title("Text to Speech | Dicto Writter")
    frame.iconbitmap(icon_path)
    frame.geometry("720x480")

    #Create Base Frame
    defaultFrame = Frame(frame)
    defaultFrame.pack(fill="both", expand=True,  padx=1, pady=1)

    MainFrame = Frame(defaultFrame)
    MainFrame.pack(fill="both", expand=True)
    
    #Create Inner Widgets
    TopFrame = Frame(MainFrame, bd=5, width=720, height=240, padx=2, relief=RIDGE, bg="#f0f0f0")
    TopFrame.pack(fill="both", expand=True)

    #Button
    captureButton = Button(TopFrame, text="Capture Image", padx=20, pady=10, command=captureimage)
    captureButton.pack(side=LEFT, padx=30, pady=10)

    showImage = Button(TopFrame, text="Show Image", padx=20, pady=10, command=showimage)
    showImage.pack(side=RIGHT, padx=30, pady=10)

    MiddleFrame = Frame(MainFrame, bd=5, width=720, height=150, padx=2, relief=RIDGE, bg="cadet blue")
    MiddleFrame.pack(fill="both", expand=True)

    ''' --------------------- Close Button --------------------- '''
    BottomFrame = Frame(defaultFrame, bd=1, relief=RIDGE, bg="#de1212")
    BottomFrame.pack(side=RIGHT, pady=10)
    Exit = Button(BottomFrame, text="Close", command=frame.destroy, fg="#ffffff", bg="#de1212", relief=FLAT)
    Exit.pack(padx=5, pady=5)


def help_frame(option):
    frame = Toplevel()
    frame.title("Dicto Writter")
    frame.iconbitmap(icon_path)
    frame.geometry("720x480")
    if option == 'help':
        #Create Main Frame for help
        defaultFrame = Frame(frame)
        defaultFrame.pack(fill="both", expand=True,  padx=1, pady=1)

        #Create Inner Widgets
        TopFrame = LabelFrame(defaultFrame, bd=2, width=480, height=300, padx=30, pady=30, relief=RIDGE, bg="#666666", fg="#ffffff", font=(myFont, 14, "bold"), text="Help")
        TopFrame.pack(fill="both", expand=True)

        helpText = Label(TopFrame, bg="#666666", fg="#ffffff", font=(myFont, myFontSize), text=myHelp)
        helpText.pack(fill="both", expand=True, padx=5, pady=5)

    if option == 'about':
        #Create Main Frame for about
        defaultFrame = Frame(frame)
        defaultFrame.pack(fill="both", expand=True,  padx=1, pady=1)

        #Create Inner Widgets
        TopFrame = LabelFrame(defaultFrame, bd=2, width=480, height=300, padx=30, pady=30, relief=RIDGE, bg="#7280ab", fg="#ffffff", font=(myFont, 14, "bold"), text="About")
        TopFrame.pack(fill="both", expand=True)

        aboutText = Label(TopFrame, fg="#ffffff", bg="#7280ab", font=(myFont, myFontSize), text=myAbout)
        aboutText.pack(fill="both", expand=True, padx=5, pady=5)

if __name__ == "__main__":
    # initialisation of tkinter
    root = Tk()
    root.title("Dicto Writter")
    root.iconbitmap(icon_path)
    root.geometry("480x320")

    ''' Menu Options '''
    menubar = Menu(root)

    select_menu = Menu(menubar, tearoff=0)
    select_menu.add_command(label="Speech to text", command=lambda: s2t_frame())
    select_menu.add_command(label="Text to Speech", command=lambda: t2s_frame())
    select_menu.add_separator()
    select_menu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="Select", menu=select_menu)

    help_menu = Menu(menubar, tearoff=0)
    help_menu.add_command(label="Help Index", command=lambda: help_frame('help'))
    help_menu.add_separator()
    help_menu.add_command(label="About...", command=lambda: help_frame('about'))
    menubar.add_cascade(label="Help", menu=help_menu)

    ''' --------------------- Creating the frame --------------------- '''
    #Create Main Frame
    defaultFrame = Frame(root)
    defaultFrame.pack(fill="both", expand=True,  padx=10, pady=10)

    #Create Inner Widgets
    TopFrame = Frame(defaultFrame, bd=2, width=480, height=300, padx=20, pady=20, relief=RIDGE, bg="light grey")
    TopFrame.pack(fill="both", expand=True)

    # Main Widgets Buttons
    s2t_button = Button(TopFrame, text="Speech to Text", command=s2t_frame, fg="#ffffff", bg="#006773", padx=20, pady=20, relief=RAISED, font=("Helvetica", 14, "bold")).pack(fill="both", expand=True, padx=2, pady=2)

    t2s_button = Button(TopFrame, text="Text to Speech", command=t2s_frame, fg="#ffffff", bg="#006773", padx=20, pady=20, relief=RAISED, font=("Helvetica", 14, "bold")).pack(fill="both", expand=True, padx=2, pady=2)

    ''' --------------------- Exit Button --------------------- '''
    BottomFrame = Frame(defaultFrame, bd=1, relief=RIDGE, bg="#de1212")
    BottomFrame.pack(side=RIGHT, pady=20)
    Exit = Button(BottomFrame, text="Exit", command=root.quit, fg="#ffffff", bg="#de1212", relief=FLAT)
    Exit.pack(padx=5, pady=5)


    root.config(menu=menubar)
    root.mainloop()
