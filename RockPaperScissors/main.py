from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from Controls import choice

class Game:
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
        self.window.title("Rock | Paper | Scissors")
        self.window.geometry(self.dimensions)
        self.window.configure(background=self.WHITE)
        self.window.resizable(width=FALSE, height=FALSE)
        
        # 
        self.my_play : str = "Your play"
        self.computer_play : str = "Computers play"
        self.player_wins : str = "You win!!"
        self.computer_wins : str = "Computer wins!!"
        self.tie : str = "It's a tie!!"
        self.paper : str = 'paper'
        self.scissor : str = 'scissor'
        self.rock : str = 'rock'
        
        # 
        self.user_play : bool = True
        self.pc_play : bool = False
        
        # 
        self.game_round : int = 0
        self.player_score : int = 0
        self.computer_score : int = 0
        self.computer_choice : int = 0
        
        self.leaderboard_player_score : int = 0
        self.learderboard_computer_score : int = 0
                        
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
        computer_canvas = Canvas(game_header_frame, bg=self.SECONDARY, width=100, height=150, highlightthickness=0)
        computer_canvas.place(x=30, y=5)
        
        player_canvas = Canvas(game_header_frame, bg=self.SECONDARY, width=100, height=150, highlightthickness=0)
        player_canvas.place(x=260, y=5)
        
        # COMPUTER IMAGE
        c_player = Image.open('assets/pc.png').convert('RGBA')
        c_player.resize((100, 100))
        c_player.save('assets/pc_resized.png')
        
        c_player_img = Image.open('assets/pc_resized.png')
        c_player_img.resize((50, 50))
        saved_c_player = ImageTk.PhotoImage(c_player_img)
        computer_canvas.create_image(50,25,image=saved_c_player)

        
        # PLAYER IMAGE
        player = Image.open('assets/player.png').convert('RGBA')
        player.resize((100, 100))
        player.save('assets/player_resized.png')
        
        player_img = Image.open('assets/player_resized.png')
        player_img.resize((100, 100))
        saved_player = ImageTk.PhotoImage(player_img)
        player_canvas.create_image(50,25,image=saved_player)
              
        
        # score label display
        score_label = Label(score_frame, text="Score", width=15, height=1, font=('Arial 14'), bg=self.DARK_BG, fg=self.SECONDARY, anchor=NW)
        score_label.place(x=10, y=20)
        
        # round label display
        round_label = Label(score_frame, text="Round : ", width=15, height=1, font=('Arial 12'), bg=self.DARK_BG, fg=self.SECONDARY, anchor=NW)
        round_label.place(x=10, y=60)
        score_round_label = Label(score_frame, text=self.game_round, width=15, height=1, font=('Arial 12'), bg=self.DARK_BG, fg=self.SECONDARY, anchor=NW)
        score_round_label.place(x=90, y=60)


        # user score display
        user_label = Label(score_frame, text="Player : ", width=15, height=1, font=('Arial 12'), bg=self.DARK_BG, fg=self.WHITE, anchor=NW)
        user_label.place(x=10, y=100) 
        user_score_label = Label(score_frame, text=self.player_score, width=15, height=1, font=('Arial 12'), bg=self.DARK_BG, fg=self.WHITE, anchor=NW)
        user_score_label.place(x=90, y=100)
        
        # computer score display
        user_label = Label(score_frame, text="Computer : ", width=15, height=1, font=('Arial 12'), bg=self.DARK_BG, fg=self.WHITE, anchor=NW)
        user_label.place(x=10, y=140)
        computer_score_label = Label(score_frame, text=self.computer_score, width=15, height=1, font=('Arial 12'), bg=self.DARK_BG, fg=self.WHITE, anchor=NW)
        computer_score_label.place(x=90, y=140)

        # learderboard label display
        learderboard_label = Label(score_frame, text="Learderboard", width=15, height=1, font=('Arial 14'), bg=self.DARK_BG, fg=self.SECONDARY, anchor=NW)
        learderboard_label.place(x=10, y=180)
        

        # user games won score display
        user_label = Label(score_frame, text="Player : ", width=15, height=1, font=('Arial 12'), bg=self.DARK_BG, fg=self.WHITE, anchor=NW)
        user_label.place(x=10, y=220) 
        userboard_score_label = Label(score_frame, text=0, width=15, height=1, font=('Arial 12'), bg=self.DARK_BG, fg=self.WHITE, anchor=NW)
        userboard_score_label.place(x=90, y=220)
        

        # computergames won score display
        user_label = Label(score_frame, text="Computer : ", width=15, height=1, font=('Arial 12'), bg=self.DARK_BG, fg=self.WHITE, anchor=NW)
        user_label.place(x=10, y=260)
        board_computer_score_label = Label(score_frame, text=0, width=15, height=1, font=('Arial 12'), bg=self.DARK_BG, fg=self.WHITE, anchor=NW)
        board_computer_score_label.place(x=90, y=260)
        
        won_label = Label(frame_up, text=self.my_play, width=20, height=1, font=('Arial 12'), bg=self.PRIMARY, fg=self.WHITE, anchor=NW)
        won_label.place(x=290, y=10)

        c_canvas = Canvas(game_frame, bg=self.DARK_BG, width=200, height=200, highlightthickness=0)
        p_canvas = Canvas(game_frame, bg=self.DARK_BG, width=200, height=200, highlightthickness=0)
        # c_canvas = Grid()
        c_canvas.place(x=-5, y=20)
        p_canvas.place(x=200, y=20)
        
   
        # computer images
        # COMPUTER ROCK
        c_rock = Image.open('assets/c_rock.png').convert('RGBA')
        c_rock.resize((100, 100))
        c_rock.save('assets/c_rock_resized.png')
        
        open_c_rock = Image.open('assets/c_rock_resized.png')
        open_c_rock.resize((100, 100))
        saved_c_rock = ImageTk.PhotoImage(open_c_rock)
        # c_canvas.create_image(100,100,image=saved_c_rock)
        
        # PLAYER ROCK
        p_rock = Image.open('assets/rock.png').convert('RGBA')
        p_rock.resize((100, 100))
        p_rock.save('assets/rock_resized.png')
        
        open_p_rock = Image.open('assets/rock_resized.png')
        open_p_rock.resize((100, 100))
        saved_p_rock = ImageTk.PhotoImage(open_p_rock)
         
        # COMPUTER PAPER
        c_paper = Image.open('assets/c_paper.png').convert('RGBA')
        c_paper.resize((100, 100))
        c_paper.save('assets/c_paper_resized.png')
        
        open_c_paper = Image.open('assets/c_paper_resized.png')
        open_c_paper.resize((100, 100))
        saved_c_paper = ImageTk.PhotoImage(open_c_paper)

        
        # PLAYER SCISSORS
        p_scissors = Image.open('assets/scissors.png').convert('RGBA')
        p_scissors.resize((100, 100))
        p_scissors.save('assets/scissors_resized.png')
        
        open_p_scissors = Image.open('assets/scissors_resized.png')
        open_p_scissors.resize((100, 100))
        saved_p_scissors = ImageTk.PhotoImage(open_p_scissors)

        
        # COMPUTER SCISSORS
        c_scissors = Image.open('assets/c_scissors.png').convert('RGBA')
        c_scissors.resize((100, 100))
        c_scissors.save('assets/c_scissors_resized.png')
        
        open_c_scissors = Image.open('assets/c_scissors_resized.png')
        open_c_scissors.resize((100, 100))
        saved_c_scissors = ImageTk.PhotoImage(open_c_scissors)
        
        
        # PLAYER PAPER
        p_paper = Image.open('assets/paper.png').convert('RGBA')
        p_paper.resize((100, 100))
        p_paper.save('assets/paper_resized.png')
        
        open_p_paper = Image.open('assets/paper_resized.png')
        open_p_paper.resize((100, 100))
        saved_p_paper = ImageTk.PhotoImage(open_p_paper)
         
        # rock button
        rock_button = Button(controls_frame, text="Rock", width=self.button_width, height=1, font=('Ivy 16 bold'), bg=self.SECONDARY, fg=self.WHITE, command=lambda:choice(self, self.rock, p_canvas, c_canvas, saved_c_rock, saved_c_paper, saved_c_scissors, saved_p_rock, saved_p_paper, saved_p_scissors, won_label, score_round_label, user_score_label, computer_score_label, userboard_score_label, board_computer_score_label, Button, frame_up))
        rock_button.place(x=12, y=8)
        
        # paper button
        paper_button = Button(controls_frame, text="Paper", width=self.button_width, height=1, font=('Ivy 16 bold'), bg=self.SECONDARY, fg=self.WHITE, command=lambda:choice(self, self.paper, p_canvas, c_canvas, saved_c_rock, saved_c_paper, saved_c_scissors, saved_p_rock, saved_p_paper, saved_p_scissors, won_label, score_round_label, user_score_label, computer_score_label, userboard_score_label, board_computer_score_label, Button, frame_up))
        paper_button.place(x=140, y=8)
        
        # scissor button
        scissor_button = Button(controls_frame, text="Scissors", width=self.button_width, height=1, font=('Ivy 16 bold'), bg=self.SECONDARY, fg=self.WHITE, command=lambda:choice(self, self.scissor, p_canvas, c_canvas, saved_c_rock, saved_c_paper, saved_c_scissors, saved_p_rock, saved_p_paper, saved_p_scissors, won_label, score_round_label, user_score_label, computer_score_label, userboard_score_label, board_computer_score_label, Button, frame_up))
        scissor_button.place(x=268, y=8)
        
        
        self.window.mainloop()

if __name__ == '__main__':
    Game().main().run()
    
