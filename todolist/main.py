
# Libraries
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Crud import CRUD

class Todolist:
    def __init__(self):
         # Colors
        self.WHITE = "#fff"
        self.BLACK = "#000"
        self.DARK_BG = "#242323"
        self.PRIMARY = "#252335"
        self.SECONDARY = "#9B1C1C"

        # Variables
        self.width = 500
        self.height = 400
        self.frame_height1 = 50
        self.frame_height2 = 70
        self.frame_height3 = 100
        self.button_width = 7
        self.dimensions = f"{self.width}x{self.height}"

        # Instantiating window/screen/display
        self.window = Tk()
        self.window.title("Task list")
        self.window.geometry(self.dimensions)
        self.window.configure(background=self.WHITE)

    def main(self):
        # Init CRUD method
        crud_method = CRUD
        # Frames
        frame_up = Frame(self.window, width=self.width, height=self.frame_height1, bg=self.DARK_BG)
        frame_up.grid(row=0, column=0, padx=0, pady=1)

        frame_down = Frame(self.window, width=self.width, height=self.frame_height2, bg=self.WHITE)
        frame_down.grid(row=1, column=0, padx=0, pady=1)

        # frame up widgets
        app_name = Label(frame_up, text="Task list", height=1, font=('Ivy 16 bold'), fg=self.WHITE, bg=self.DARK_BG, anchor=NW)
        app_name.place(x=5, y=5)
        
        # table frame
        frame_table = Frame(self.window, width=self.width, height=self.frame_height3, bg=self.DARK_BG)
        frame_table.grid(row=2, column=0, columnspan=2, padx=10, pady=2, sticky=NW)
       
        # function
        def show():
            global tree
            
            list_header = ['Tasks', 'Done']
            # demo_list = crud_method.view()
            
            tree = ttk.Treeview(frame_table, selectmode="extended", columns=list_header, show="headings")
            
            vsb = ttk.Scrollbar(frame_table, orient="vertical", command=tree.yview)
            hsb = ttk.Scrollbar(frame_table, orient="horizontal", command=tree.xview)
            
            tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
            
            
            tree.grid(column=0, row=0, sticky='nsew')
            vsb.grid(column=1, row=0, sticky='ns')
            hsb.grid(column=0, row=1, sticky='ew')
            
            # tree head
            tree.heading(0, text="To do", anchor=NW)
            tree.heading(1, text="Done", anchor=NW)
            
            # tree colums
            tree.column(0, width=400, anchor='nw')
            tree.column(1, width=50, anchor='nw')
            
            demo_list = [["Set up a readme file","done"], ["push to github", '']]
            
            for item in demo_list:
                tree.insert('', 'end', values=item)
       
        show()        
        
         # frame down 
        name_label = Label(frame_down, text="Add Task *", width=20, height=3, font=('Arial 12'), bg=self.WHITE, anchor=NW)
        name_label.place(x=10, y=20)
        entry_name = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief='solid')
        entry_name.place(x=105, y=22)
        
        def show():
            pass
        
        # pass data in function
        def insert():
                Name = entry_name.get() # get input
                
                if Name == '': # check if it empty
                    messagebox.showwarning('Error', 'Please enter task')
                
                # if its not empty
                data = [Name, False]
                crud_method.add(data)
                messagebox.showinfo('Success', 'Task added sucessfull')
                entry_name.delete(0, 'end')
        
        def set_update():
            pass
        
        def to_remove():
            pass
               
        # add button
        add_button = Button(frame_down, text="Add", width=self.button_width, height=1, font=('Arial 8 bold'), bg=self.SECONDARY, fg=self.WHITE, command=insert)
        add_button.place(x=290, y=22)
        
        # update button
        update_button = Button(frame_down, text="Edit", width=self.button_width, height=1, font=('Arial 8 bold'), bg=self.SECONDARY, fg=self.WHITE, command=set_update)
        update_button.place(x=360, y=22)
        
        # delete button
        delete_button = Button(frame_down, text="Delete", width=self.button_width, height=1, font=('Arial 8 bold'), bg=self.SECONDARY, fg=self.WHITE, command=to_remove)
        delete_button.place(x=430, y=22)
        self.window.mainloop()

if __name__ == '__main__':
    Todolist().main().run()
