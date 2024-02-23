from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class PhoneBook:
    def __init__(self):
        # Colors 
        self.WHITE = "#fff"
        self.BLACK = "#000"
        self.DARK_BG = "#242323"
        self.PRIMARY = "#252335"
        self.SECONDARY = "#9B1C1C"

        # Variables
        self.width = 600
        self.height = 400
        self.frame_height1 = 50
        self.frame_height2 = 50
        self.frame_height3 = self.height - self.frame_height1 - self.frame_height2
        self.frame_width3 = 220
        self.frame_width2 = self.width -self.frame_width3
        self.game_frame_height = self.height - (self.frame_height1*2) - self.frame_height2
        self.button_width = 7
        self.dimensions = f"{self.width}x{self.height}"

        # Instantiating window/screen/display
        self.window = Tk()
        self.window.title("Phone Book")
        self.window.geometry(self.dimensions)
        self.window.configure(background=self.WHITE)
        self.window.resizable(width=FALSE, height=FALSE)
        
    def main(self):
    
        # Frames
        frame_up = Frame(self.window, width=self.width, height=self.frame_height1, bg=self.PRIMARY)
        frame_up.grid(row=0, column=0, padx=0)

        
        # table frame
        score_frame = Frame(self.window, width=self.frame_width3, height=self.frame_height3, bg=self.DARK_BG)
        score_frame.grid(row=1, column=0, sticky=NE)
        
        # controls frame
        controls_frame = Frame(self.window, width=self.frame_width2, height=self.frame_height2, bg=self.SECONDARY)
        controls_frame.grid(row=2, column=0, padx=0)
  
        # frame up widgets
        app_name = Label(frame_up, text="Rock Paper Scissors", height=1, font=('Arial 16 bold'), bg=self.PRIMARY, fg=self.WHITE, anchor=NW)
        app_name.place(x=5, y=5)
        
        # game header frame
        game_header_frame = Frame(self.window, width=self.frame_width2, height=self.frame_height2, bg=self.SECONDARY)
        game_header_frame.place(x=0, y=self.frame_height1)
        
        # game frame
        game_frame = Frame(self.window, width=self.frame_width2, height=self.game_frame_height, bg=self.DARK_BG)
        game_frame.place(x=0, y=self.frame_height1 + self.frame_height1)
        
        # user score display
        game_header_pc_l = Label(game_header_frame, text="Computer", width=15, height=1, font=('Arial 16'), bg=self.SECONDARY, fg=self.WHITE, anchor=NW)
        game_header_pc_l.place(x=40, y=10)
        game_header_user_l = Label(game_header_frame, text="Player", width=15, height=1, font=('Arial 16'), bg=self.SECONDARY, fg=self.WHITE, anchor=NW)
        game_header_user_l.place(x=270, y=10) 
        
        
        # score label display
        score_label = Label(score_frame, text="Score", width=15, height=1, font=('Arial 14'), bg=self.DARK_BG, fg=self.WHITE, anchor=NW)
        score_label.place(x=10, y=20)
        
        # round label display
        round_label = Label(score_frame, text="Round : ", width=15, height=1, font=('Arial 12'), bg=self.DARK_BG, fg=self.WHITE, anchor=NW)
        round_label.place(x=10, y=60)
        score_round_label = Label(score_frame, text="10", width=15, height=1, font=('Arial 12'), bg=self.DARK_BG, fg=self.WHITE, anchor=NW)
        score_round_label.place(x=90, y=60)


        # user score display
        user_label = Label(score_frame, text="User : ", width=15, height=1, font=('Arial 12'), bg=self.DARK_BG, fg=self.WHITE, anchor=NW)
        user_label.place(x=10, y=100) 
        user_score_label = Label(score_frame, text="5", width=15, height=1, font=('Arial 12'), bg=self.DARK_BG, fg=self.WHITE, anchor=NW)
        user_score_label.place(x=90, y=100)
        
        # computer score display
        user_label = Label(score_frame, text="Computer : ", width=15, height=1, font=('Arial 12'), bg=self.DARK_BG, fg=self.WHITE, anchor=NW)
        user_label.place(x=10, y=140)
        computer_score_label = Label(score_frame, text="10", width=15, height=1, font=('Arial 12'), bg=self.DARK_BG, fg=self.WHITE, anchor=NW)
        computer_score_label.place(x=90, y=140)

        # learderboard label display
        learderboard_label = Label(score_frame, text="Learderboard", width=15, height=1, font=('Arial 14'), bg=self.DARK_BG, fg=self.WHITE, anchor=NW)
        learderboard_label.place(x=10, y=180)
        

        # user games won score display
        user_label = Label(score_frame, text="User : ", width=15, height=1, font=('Arial 12'), bg=self.DARK_BG, fg=self.WHITE, anchor=NW)
        user_label.place(x=10, y=220) 
        user_score_label = Label(score_frame, text="5", width=15, height=1, font=('Arial 12'), bg=self.DARK_BG, fg=self.WHITE, anchor=NW)
        user_score_label.place(x=90, y=220)
        
        # computergames won score display
        user_label = Label(score_frame, text="Computer : ", width=15, height=1, font=('Arial 12'), bg=self.DARK_BG, fg=self.WHITE, anchor=NW)
        user_label.place(x=10, y=260)
        computer_score_label = Label(score_frame, text="10", width=15, height=1, font=('Arial 12'), bg=self.DARK_BG, fg=self.WHITE, anchor=NW)
        computer_score_label.place(x=90, y=260)        
        
        def scissors():
            pass
        
        def rock():
            pass
        
        def paper():
            pass
        
        # view button
        view_button = Button(controls_frame, text="Rock", width=self.button_width, height=1, font=('Ivy 16 bold'), bg=self.SECONDARY, fg=self.WHITE, command=scissors)
        view_button.place(x=12, y=8)
        
        # add button
        add_button = Button(controls_frame, text="Paper", width=self.button_width, height=1, font=('Ivy 16 bold'), bg=self.SECONDARY, fg=self.WHITE, command=rock)
        add_button.place(x=140, y=8)
        
        # update button
        update_button = Button(controls_frame, text="Scissors", width=self.button_width, height=1, font=('Ivy 16 bold'), bg=self.SECONDARY, fg=self.WHITE, command=paper)
        update_button.place(x=268, y=8)
        
        
        self.window.mainloop()

if __name__ == '__main__':
    PhoneBook().main().run()
    
