from tkinter import Tk, Label, Button
from tkinter.ttk import Combobox

import random
from enum import Enum, auto

class ResultGame(Enum):
    WIN = auto()
    TIE = auto()
    LOOSE = auto()

    def reverced_result(self):
        return {
            ResultGame.WIN: ResultGame.LOOSE,
            ResultGame.TIE: ResultGame.TIE,
            ResultGame.LOOSE: ResultGame.WIN,
        }[self]    


class Turn(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()

    def __str__(self):
        return {
            Turn.ROCK: "Rock",
            Turn.PAPER: "Paper",
            Turn.SCISSORS: "Scissors",
        }[self]

    

class GameRound:
    def __init__(self, player1_turn: Turn, player2_turn: Turn):
        self._player1_turn = player1_turn
        self._player2_turn = player2_turn

    def result(self):
        player1_result = {
            (Turn.ROCK, Turn.ROCK): ResultGame.TIE, 
            (Turn.ROCK, Turn.PAPER): ResultGame.LOOSE,
            (Turn.ROCK, Turn.SCISSORS): ResultGame.WIN,
            (Turn.PAPER, Turn.ROCK): ResultGame.WIN,
            (Turn.PAPER, Turn.PAPER): ResultGame.TIE,
            (Turn.PAPER, Turn.SCISSORS): ResultGame.LOOSE,
            (Turn.SCISSORS, Turn.ROCK): ResultGame.LOOSE,
            (Turn.SCISSORS, Turn.PAPER): ResultGame.WIN,
            (Turn.SCISSORS, Turn.SCISSORS): ResultGame.TIE, 
        }[(self._player1_turn, self._player2_turn)]

        player2_result = player1_result.reverced_result()

        return (player1_result, player2_result)
    

class Game: 

    def __init__(self, root: Tk):
        self._root = root
        self._label_computer = None
        self._user_select = None
        self._wl_label = None       
    

    def _spin(self):
        turn_player = self._turn_player() 
        turn_computer = self._turn_computer()

        player_result, computer_result = GameRound(turn_player, turn_computer).result()

        self._update_form(player_result, computer_result, turn_computer)


    def _turn_computer(self):        
        return random.choice(list(Turn))

    def _turn_player(self):
        return {
            "Rock": Turn.ROCK,
            "Paper": Turn.PAPER,
            "Scissors": Turn.SCISSORS,
        }[self._user_select.get()]


    def _update_form(self, player_result, computer_result, turn_computer):
        message = {
            ResultGame.WIN: "YOU Won",
            ResultGame.TIE: "YOU Tie!",
            ResultGame.LOOSE: "YOU Loose",
        }[player_result]

        message_computer = random.choice({
            ResultGame.WIN: ["I am better","booo",""],
            ResultGame.TIE: ["Bad luck", "Nice game", "I am playing this game since i was born"],
            ResultGame.LOOSE: ["You won by luck", "Shit how you are better", ""],
        }[computer_result])

        if message_computer:
            message = f"{message} - Computer: {message_computer}" 
        self._wl_label.config(text=message)

        self._label_computer.config(text=Turn.to_str(turn_computer))
        
    

    def create_form(self):
        # Set geometry
        self._root.geometry("500x500")

        self._root.title("Rock-Paper-Scissors-Game")

        self._label_computer = Label(self._root, text="Computer ",width = 20,height=4,font=("algerian",15))
        self._label_computer.pack()

        # Adding dropdown box for Rock,Paper,Scissors
        self._user_select = Combobox(self._root, value=["Rock","Paper","Scissors"])
        self._user_select.current(0)
        self._user_select.pack()

        # Add Labels,Button
        self._wl_label = Label(self._root, text="",font=("arial",10),width=50,height=4)
        self._wl_label.pack()


        button = Button(self._root, text="Spin!",font=("bell mt",10),command=self.spin)
        button.pack()

    def mainloop(self):
        self._root.mainloop()



game = Game(Tk())
game.create_form()
game.mainloop()
