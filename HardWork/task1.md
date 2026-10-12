##### Первый пример кода

###### Код до

Код взят отсюда: 

```python
def complex_arithmetic():
    """
    Function to execute complex arithmetic operations such as addition, subtraction, multiplication, and division.

    Asks the user to choose the operation and input the complex numbers as real and imaginary parts,
    performs the operation, and returns the result.
    """
    print("Enter '1' for complex addition")
    print("Enter '2' for complex subtraction")
    print("Enter '3' for complex multiplication")
    print("Enter '4' for complex division")
    choice = input("enter your choice")
    if choice == "1":
        nums = list(map(int, input("Enter all numbers separated by space: ").split()))
        real_sum = 0
        imag_sum = 0
        for i in range(0, len(nums) - 1, 2):
            real_sum += nums[i]
        for i in range(2, len(nums) - 1, 2):
            imag_sum += nums[i]
        imag_sum += nums[-1]
        return f"{real_sum}+ i{imag_sum}"

    elif choice == "2":
        nums = list(map(int, input("Enter all numbers separated by space: ").split()))
        real_sub = nums[0]
        imag_sub = nums[1]
        for i in range(2, len(nums) - 1, 2):
            real_sub -= nums[i]
        for i in range(3, len(nums) - 1, 2):
            imag_sub -= nums[i]
        imag_sub -= nums[-1]
        return f"{real_sub}+ i{imag_sub}"

    elif choice == "3":
        nums = list(
            map(
                int,
                input(
                    "Enter all numbers separated by space maximum 4 elements: "
                ).split(),
            )
        )
        real = nums[0] * nums[2] - nums[1] * nums[3]
        imag = nums[0] * nums[3] + nums[2] * nums[1]
        return f"{real}+ i{imag}"

    elif choice == "4":
        nums = list(
            map(
                int,
                input(
                    "Enter all numbers separated by space maximum 4 elements: "
                ).split(),
            )
        )
        real = (nums[0] * nums[2] + nums[1] * nums[3]) / (nums[2] ** 2 + nums[3] ** 2)
        imag = (nums[1] * nums[2] - nums[0] * nums[3]) / (nums[2] ** 2 + nums[3] ** 2)
        return f"{real}+ i{imag}"
```

###### Код после
```python
class ComplexNumber():
    def __init__(self, real: int, imag: int):
        self._real = real
        self._imag = imag

    def __str__(self):
        return f"{self._real}+i{self._imag}"
    
    def sum(self, other: 'ComplexNumber'):
        real = self._real+other._real
        imag =  self._imag+other._imag   

        return ComplexNumber(real, imag)
    
    def subtraction(self, other: 'ComplexNumber'):
        real = self._real-other._real
        imag = self._imag-other._imag  

        return ComplexNumber(real, imag)

    def multiplication(self, other: 'ComplexNumber'):
        real = self._real*other._real - self._imag*other._imag
        imag = self._imag*other._real + self._real*other._imag

        return ComplexNumber(real, imag)

    def division(self, other: 'ComplexNumber'):
        real = int((self._real*other._real + self._imag*other._imag)/(other._real^2+other._imag^2))
        imag = int((self._imag*other._real - self._real*other._imag)/(other._real^2+other._imag^2))

        return ComplexNumber(real, imag)    


class ComplexCalculator():
    def start(self):
        print("Enter '1' for complex addition")
        print("Enter '2' for complex subtraction")
        print("Enter '3' for complex multiplication")
        print("Enter '4' for complex division")
        choice = input("enter your choice")

        choises = { 
            "1": lambda num1, num2: num1.sum(num2),
            "2": lambda num1, num2: num1.subtraction(num2),
            "3": lambda num1, num2: num1.multiplication(num2),
            "4": lambda num1, num2: num1.division(num2),
        }

        fun = choises[choice]
        if not fun:
            return

        nums = self._input_numbers("Enter all numbers separated by space: ") 
        return str(self._calculate(nums,fun))
        

    def _calculate(self, nums, fun):
        result = nums.pop()
        while nums:
            result = fun(result, nums.pop())

        return result
    

    def _input_numbers(self, message: str) -> list[ComplexNumber]:        

        nums = list(map(int, input(message).split()))
        len_nums = len(nums)
        pairs = zip(nums[::2],nums[1::2])

        return list(map(lambda real, complex: ComplexNumber(real, complex), pairs))
        
```

###### Рефлексия




##### Второй пример кода

###### Код до

Рефакторить буду метод `spin`

```python
# Import Required Library
from tkinter import *
from tkinter import ttk
from random import *

# Create Object
root = Tk()

# Set geometry
root.geometry("500x500")

root.title("Rock-Paper-Scissors-Game")

# List of players
list = ["rock","paper","scissors"]

choose_number = randint(0,2)
print(choose_number) # For testing if it works

label = Label(root,text="Computer ",width = 20,height=4,font=("algerian",15))
label.pack()

def spin():
    choose_number = randint(0,2)
    label.config(text=list[choose_number])
    if user_select.get() == "Rock":
        user_select_value = 0
        print(user_select_value)
    elif user_select.get() == "Paper":
        user_select_value = 1
        print(user_select_value)
    elif user_select.get() == "Scissors":
        user_select_value = 2
        print(user_select_value)

    if user_select_value == 0:
        if choose_number == 0:
            wl_label.config(text="Tie! - "+" Computer:Bad luck")
        elif choose_number == 1:
            wl_label.config(text="YOU Loose - "+" Computer: I am better ")
        elif choose_number == 2 :
            wl_label.config(text="YOU Won - "+" Computer: You won by luck")

    elif user_select_value == 1:
        if choose_number == 1:
            wl_label.config(text="Tie! - "+" Computer: Nice game")
        elif choose_number == 0:
            wl_label.config(text="YOU Won - "+" Computer: Shit how you are better")
        elif choose_number == 2 :
            wl_label.config(text="YOU Loose - "+" Computer: booo")

    elif user_select_value == 2:
        if choose_number == 2:
            wl_label.config(text="Tie!")
        elif choose_number == 0:
            wl_label.config(text="YOU Loose - "+" Computer: I am playing this game since i was born")
        elif choose_number == 1 :
            wl_label.config(text="YOU Won")



# Adding dropdown box for Rock,Paper,Scissors
user_select = ttk.Combobox(root,value=["Rock","Paper","Scissors"])
user_select.current(0)
user_select.pack()

# Add Labels,Button
wl_label = Label(root,text="",font=("arial",10),width=50,height=4)
wl_label.pack()

button = Button(root,text="Spin!",font=("bell mt",10),command=spin)
button.pack()

root.mainloop()
```

##### Код после

```python
from tkinter import *
from tkinter import ttk
from random import choice
from enum import Enum, auto

# Create Object
root = Tk()

# Set geometry
root.geometry("500x500")

root.title("Rock-Paper-Scissors-Game")

label = Label(root,text="Computer ",width = 20,height=4,font=("algerian",15))
label.pack()

class ResultGame(Enum):
    WIN = auto()
    TIE = auto()
    LOOSE = auto()

    @classmethod
    def reverced_result(cls, value: 'ResultGame'):
        return {
            cls.WIN: cls.LOOSE,
            cls.TIE: cls.TIE,
            cls.LOOSE: cls.WIN,
        }[value]    


class Turn(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()

    @classmethod
    def random(cls):
        return random.choice(list(cls))
    
    @classmethod
    def from_str(cls, value: str):
        return {
            "Rock": cls.ROCK,
            "Paper": cls.PAPER,
            "Scissors": cls.SCISSORS,
        }[value]
    
    @classmethod
    def to_str(cls, value: 'Turn'):
        return {
            cls.ROCK: "Rock",
            cls.PAPER: "Paper",
            cls.SCISSORS: "Scissors",
        }[value]
    

class Game: #сделать ли отдельный класс который отвечает за вид 

    def _play(player1_turn: Turn, player2_turn: Turn):

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
        }[(player1_turn, player2_turn)]

        player2_result = player1_result.reverced_result()

        return (player1_result, player2_result)
    

    def spin(self):
        turn_computer = Turn.random()
        turn_player = Turn.from_str(user_select.get())

        player_result, computer_result = self._play(turn_player, turn_computer)

        message_player = self._message_player(player_result)
        message_computer = self._message_computer(computer_result)

        message = message_player

        if message_computer:
            message = f"{message} - Computer: {message_computer}" 

        label.config(text=Turn.to_str(turn_computer))
        wl_label.config(text=message)


    def _message_player(self, result: ResultGame):
        return {
            ResultGame.WIN: "YOU Won",
            ResultGame.TIE: "YOU Tie!",
            ResultGame.LOOSE: "YOU Loose",
        }
        

    def _message_computer(self, result: ResultGame):
        avaible_messages = {
            ResultGame.WIN: ["I am better","booo",""],
            ResultGame.TIE: ["Bad luck", "Nice game", "I am playing this game since i was born"],
            ResultGame.LOOSE: ["You won by luck", "Shit how you are better", ""],
        }

        return random.choice(avaible_messages)
    



# Adding dropdown box for Rock,Paper,Scissors
user_select = ttk.Combobox(root,value=["Rock","Paper","Scissors"])
user_select.current(0)
user_select.pack()

# Add Labels,Button
wl_label = Label(root,text="",font=("arial",10),width=50,height=4)
wl_label.pack()

game = Game()
button = Button(root,text="Spin!",font=("bell mt",10),command=game.spin)
button.pack()

root.mainloop()
```


###### Рефлексия

На следующих этапах рефакторинга, можно было бы создать класс для работы с формой игры.
Сейчас код при этом взаимодействует с объектами вне контекста класса, это элементы формы.