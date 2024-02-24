from random import randint

def message(won_label, msg):
    won_label.configure(text=msg)

def winner(self, player, pc, won_label, user_score_label, computer_score_label):
    player_score = 0
    computer_score = 0
    
    if player == pc:
        message(won_label, "It a tie")
    if player == self.rock:
        if pc == self.paper: 
            message(won_label, 'Pc won')
            computer_score = self.computer_score + 1
            self.computer_score = computer_score
            computer_score_label.configure(text=computer_score)
        else:
            message(won_label, 'You win')
            player_score = self.player_score + 1
            self.player_score = player_score
            user_score_label.configure(text=player_score)
    elif player == self.paper:
        if pc == self.scissor:
            message(won_label, 'Pc won')
            computer_score = self.computer_score + 1
            self.computer_score = computer_score
            computer_score_label.configure(text=computer_score)
        else:
            message(won_label, 'You win')
            player_score = self.player_score + 1
            self.player_score = player_score
            user_score_label.configure(text=player_score)
    elif player == self.scissor:
        if pc == self.rock:
            message(won_label, 'Pc won')
            computer_score = self.computer_score + 1
            self.computer_score = computer_score
            computer_score_label.configure(text=computer_score)
        else:
            message(won_label, 'You win')
            player_score = self.player_score + 1
            self.player_score = player_score
            user_score_label.configure(text=player_score)
    else:
        pass

def choice(self, 
           player_select,
           p_canvas, 
           c_canvas, 
           saved_c_rock, 
           saved_c_paper, 
           saved_c_scissors,
           saved_p_rock,
           saved_p_paper,
           saved_p_scissors,
           won_label,
           score_round_label,
           user_score_label,
           computer_score_label,
           userboard_score_label,
           board_computer_score_label,
           Button,
           frame_up
           ):
    
    if self.game_round >= 11:
        return None
    new_round : int = self.game_round + 1
    
    def play_again(play_again_button):
        user_score_label.configure(text=0)
        computer_score_label.configure(text=0)
        self.player_score = 0
        self.computer_score = 0
        self.game_round = 0
        score_round_label.configure(text=0)
        play_again_button.place_forget()
    if new_round >= 12:
        return
    else:
        if new_round == 11:
            
            if self.player_score > self.computer_score:
                new_score : int = self.leaderboard_player_score + 1
                self.leaderboard_player_score = new_score
                userboard_score_label.configure(text=new_score)
            elif self.computer_score > self.player_score:
                new_score : int = self.leaderboard_computer_score + 1
                self.leaderboard_computer_score = new_score
                board_computer_score_label.configure(text=new_score)
                    
            # play again button
            play_again_button = Button(frame_up, text="Play again", width=20, height=1, font=('Ivy 10 bold'), bg=self.SECONDARY, fg=self.WHITE, command=lambda:play_again(play_again_button))
            play_again_button.place(x=380, y=8)
            return
        
        computer_choice = ['rock', 'paper', 'scissors']
        pc_rand_select = computer_choice[randint(0, 2)]

        if pc_rand_select == self.rock:
            c_canvas.delete('all')
            c_canvas.create_image(100,100,image=saved_c_rock)
            self.my_play = 'Your play'     
        elif pc_rand_select == self.paper:
            c_canvas.delete('all')
            c_canvas.create_image(100,100,image=saved_c_paper)
            self.my_play = 'Your play'
        elif pc_rand_select == self.scissor:
            c_canvas.delete('all')
            c_canvas.create_image(100,100,image=saved_c_scissors)
            self.my_play = 'Your play'
            
        # player selections
        if player_select == self.rock:
            p_canvas.delete('all')
            p_canvas.create_image(100,100,image=saved_p_rock)
            self.my_play = "Computer's play"
        elif player_select == self.paper:
            p_canvas.delete('all')
            p_canvas.create_image(100,100,image=saved_p_paper)
            self.my_play = "Computer's play"
        elif player_select == self.scissor:
            p_canvas.delete('all')
            p_canvas.create_image(100,100,image=saved_p_scissors)
            self.my_play = "Computer's play"
            
        if self.my_play == 'Your play':
            won_label.configure(text="Computer's play")
        elif self.my_play == "Computer's play":
            won_label.configure(text="Your play")
                        
            
        self.game_round = new_round
        score_round_label.configure(text=new_round)
            
        winner(self, player_select, pc_rand_select, won_label, user_score_label, computer_score_label)