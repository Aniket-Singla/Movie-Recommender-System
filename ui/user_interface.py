
import sys
sys.path.insert(0,'../')
from model.demographic.recommender import return_top
from PIL import Image, ImageTk
import urllib
import io
import tkinter as tk
from tkinter import ttk
from download_image import get_image

# Simple enough, just import everything from tkinter.
LARGE_FONT = ("Verdana",12)
class MainWindow(tk.Tk):

    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        # tk.Tk.iconbitmap(self,default="w.bitmap")
        tk.Tk.wm_title(self,'Movie Recommendation System')
        container = tk.Frame(self)
        container.pack(side="top",fill = "both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        menubar = tk.Menu(container)
        
        filemenu = tk.Menu(menubar,tearoff=0)
        filemenu.add_command(label = "Demographic Filtering",command = lambda:self.show_frame(Demographic))
        filemenu.add_separator()
        filemenu.add_command(label = "Content Based Filtering",command = lambda:self.show_frame(ContentBased))
        menubar.add_cascade(label="File",menu = filemenu)
        tk.Tk.config(self,menu = menubar)
        self.frames = {}
        # print(type(Demographic))
        for F in (Demographic , ContentBased):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row = 0,column=0,sticky="nsew")

             
        self.show_frame(Demographic)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
    
class Demographic(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label1 = tk.Label(self,text = "Demographic Filtering Page",font = LARGE_FONT)
        label1.pack()
        text = tk.Text(self, wrap=tk.NONE)
        vsb = tk.Scrollbar(orient=tk.VERTICAL ,command=text.yview)
        text.configure(yscrollcommand=vsb.set)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        text.pack(fill=tk.BOTH, expand=True)
        loop_index = 0
        for index, row in return_top(10).iterrows():
            # b = tk.Button(self, text="Button #%s" % i)
            image = get_image(row['id'])
            title = row['title']
            # label = tk.Label(self,image=image,text = title, compound = tk.RIGHT)
            label = tk.Label(self,image=image)
            label.image = image
            text.window_create(tk.END, window=label)
            if loop_index % 3 < 2:
                text.insert(tk.END,title+'\t')
            else:
                text.insert(tk.END,title+'\n')
            loop_index += 1
        text.configure(state="disabled")

        # for index, row in return_top(10).iterrows():
        #     image = get_image(row['id'])
        #     label2 = ttk.Label(self,image=image)
        #     label2.image = image
        #     label2.pack()
        #     label3 = ttk.Label(self,text= row['title'])
        #     label3.pack()
        
        
        
        button1 = ttk.Button(self,text="Content Based",command = lambda : controller.show_frame(ContentBased))
        button1.pack()


class ContentBased(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text = "Content Based Page",font = LARGE_FONT)
        label.pack(pady=10, padx = 10)
        button1 = ttk.Button(self,text="Back To Demographic",command = lambda : controller.show_frame(Demographic))
        button1.pack()

demo = MainWindow()
demo.geometry("1280x720")
demo.mainloop()

