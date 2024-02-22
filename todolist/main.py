
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
        self.small_w_width = 380
        self.height = 400
        self.small_w_height = 160
        self.frame_height1 = 50
        self.frame_height2 = 70
        self.frame_height3 = 100
        self.button_width = 7
        self.dimensions = f"{self.width}x{self.height}"
        self.small_w_dimensions = f"{self.small_w_width}x{self.small_w_height}"

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
        frame_table = Frame(self.window, width=self.small_w_width, height=self.frame_height3, bg=self.DARK_BG)
        frame_table.grid(row=2, column=0, columnspan=2, padx=10, pady=2, sticky=NW)
       
        # function
        def show():
            global tree
            
            list_header = ['Tasks', 'Done']
            
            task_list = crud_method.view() # stored tasks
            
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
            tree.column(0, width=380, anchor='nw')
            tree.column(1, width=80, anchor='nw')
            
            # iterating through task for display
            for item in task_list:
                tree.insert('', 'end', values=item)
       
        show()        
        
         # frame down 
        name_label = Label(frame_down, text="Add Task *", width=20, height=3, font=('Arial 12'), bg=self.WHITE, anchor=NW)
        name_label.place(x=10, y=20)
        entry_name = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief='solid')
        entry_name.place(x=105, y=22)
                
        # pass data in function
        def insert():
                Name = entry_name.get() # get input
                
                if Name == '': # check if it empty
                    messagebox.showwarning('Error', 'Please enter task')
                
                # if its not empty
                data = [Name, "Not Done"]
                crud_method.add(data)
                show()
                entry_name.delete(0, 'end')
                
        
        def set_update():
            # row selected
            tree_data = tree.focus()
            tree_dictionary = tree.item(tree_data)
            tree_list = tree_dictionary['values']
            
            if tree_list == "":
                return messagebox.showerror("Error", "Please select to-do to edit in task list")
                
            Task = str(tree_list[0])
            Completed = str(tree_list[1])

            # Init frame
             # Instantiating window/screen/display
            edit_window = Tk()
            edit_window.title("Update task")
            edit_window.geometry(self.small_w_dimensions)
            edit_window.configure(background=self.WHITE)
            edit_frame = Frame(edit_window, width=self.width, height=self.small_w_height)
            edit_frame.grid(row=0, column=0, padx=0, pady=1)
            
            edit_label = Label(edit_frame, text="Edit Task *", width=20, height=3, font=('Arial 10'), anchor=NW)
            edit_label.place(x=10, y=20)
            entry_edit = Entry(edit_frame, width=40, justify='left', highlightthickness=2, relief='solid')
            entry_edit.insert(0, Task)
            entry_edit.place(x=100, y=20)
            
            done_label = Label(edit_frame, text="Compeleted ?", width=15, height=1, font=('Ivy 10'), anchor=NW)
            done_label.place(x=10, y=60)
            combo_done = ttk.Combobox(edit_frame, width=37)
            combo_done['values'] = [ 'Done', 'Not Done']
                
            combo_done.insert(0, Completed)
            combo_done.place(x=100, y=60)
            
            def save():
                Done = combo_done.get()
                Edit = entry_edit.get()
                
                data = [Edit, Done]
                crud_method.edit(data, Task)
                show()
                edit_window.destroy()
            # add button
            edit_button = Button(edit_frame, text="Save", width=self.button_width, height=1, font=('Arial 8 bold'), bg=self.PRIMARY, fg=self.WHITE, command=save)
            edit_button.place(x=285, y=100)
        
        
        def to_remove():
            try:
                tree_data = tree.focus()
                tree_dictionary = tree.item(tree_data)
                tree_list = tree_dictionary['values']
                task = str(tree_list[0])
                crud_method.remove(task)                
                show()
            except:
                messagebox.showinfo('Error',  "Select to-do from phone task list")
            
               
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
