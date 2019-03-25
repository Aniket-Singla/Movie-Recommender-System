"""
There are many ways of making GUI using tkinter:
a) Extend tk.Tk class and add Frames as Objects to this Class
b) Extend tk.Frame class and make an object of tk.Tk class and pass Frame to this o

"""

# from tkinter import *

# from PIL import Image, ImageTk
# class Window(Frame):

#     def __init__(self, master=None):
        
#         Frame.__init__(self, master)   
#         self.master = master

#         #with that, we want to then run init_window, which doesn't yet exist
#         self.init_window()

#     #Creation of init_window
#     def init_window(self):

#         # changing the title of our master widget      
#         self.master.title("GUI")

#         # allowing the widget to take the full space of the root window
#         self.pack(fill=BOTH, expand=1)

#         # creating a menu instance
#         menu = Menu(self.master)
#         self.master.config(menu=menu)
#         file = Menu(menu)
#         file.add_command(label="Exit", command=self.client_exit)
#         menu.add_cascade(label="File", menu=file)


#         # create the file object)
#         edit = Menu(menu)

#         # adds a command to the menu option, calling it exit, and the
#         # command it runs on event is client_exit
#         edit.add_command(label="Show Img", command=self.showImg)
#         edit.add_command(label="Show Text", command=self.showText)

#         #added "file" to our menu
#         menu.add_cascade(label="Edit", menu=edit)

#     def showImg(self):
#         load = Image.open("an.jpg")
#         render = ImageTk.PhotoImage(load)

#         # labels can be text or images
#         img = Label(self, image=render)
#         img.image = render
#         img.place(x=0, y=0)


#     def showText(self):
#         text = Label(self, text="Hey there good lookin!")
#         text.pack()
        

#     def client_exit(self):
#         exit()


# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()
root.geometry("400x300")
#creation of an instance
app = Window(root)
#mainloop 
root.mainloop()  

# LARGE_FONT = ("Verdana",12)
# class Demo(tk.Tk):

#     def __init__(self,*args,**kwargs):
#         tk.Tk.__init__(self,*args,**kwargs)
#         container = tk.Frame(self)

#         container.pack(side="top",fill = "both",expand=True)
#         container.grid_rowconfigure(0,weight=1)
#         container.grid_columnconfigure(0,weight=1)

#         self.frames = {}
#         frame = StartPage(container,self)
#         self.frames[StartPage] = frame

#         frame.grid(row = 0,column=0,sticky="nsew")
#         self.show_frame(StartPage)

#     def show_frame(self, cont):
#         frame = self.frames[cont]
#         frame.tkraise()
    
# class StartPage(tk.Frame):
#     def __init__(self,parent,container):
#         tk.Frame.__init__(self,parent)
#         label = tk.Label(self,text = "Aniket's Start Page",font = LARGE_FONT)
#         label.pack(pady=10, padx = 10)

# demo = Demo()
# demo.mainloop()


result = str(return_top(12))
m = tk.Tk()
m.title('Demographic Filtering')
bool = False
def action(bool=bool):
    if bool!=True:
        T = tk.Label(m,text = return_top(12))
        T.grid() 
        bool = True
tk.Button(m,text="Display",width=5,height=3,
                   fg="red",bg="light green", 
                   command=action).grid(row=1, column=1) 


# T.insert(tk.END, return_top(10)) 
# button = tk.Button(m, text='Stop', width=25)
# button.grid()

t1 = tk.Text(m)
# t1.insert(10,return_top(10))
m.mainloop()    