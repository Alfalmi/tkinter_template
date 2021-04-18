from Tkinter import *

# Main class
class Application:
    def __init__(self, master):  # Constructor
        def program_functions(): # Program functions
            print("Awesomeness")
        frame = Frame(master)
        frame.pack()
        btn_one = Button(master, text='Exit', command=quit)
        btn_one.pack(side=BOTTOM)

root = Tk()
app = Application(root)
root.title('Title Here')
root.minsize(300,300)

root.mainloop()


