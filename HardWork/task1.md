##### Первый пример кода

###### Код до

Код взят отсюда:  https://github.com/Mrinank-Bhowmick/python-beginner-projects/blob/59f55d977821460d14bbe8083ad80e7891f282eb/projects/Calculator/main.py#L68-L126

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

Рефакторил метод `complex_arithmetic()`, у меня это стал метод start() для объекта ComplexCalculator. В исходном методе 4 условия и 4 цикла. Исходная цикломатическая сложность 4+4+1=9. После рефакторинга цикломатическая сложность 2. Увидел модуль, который можно назвать калькулятором, и модуль, который отвечает за бизнес-логику комплексных чисел. Реализовал их с помощью классов ComplexNumber и ComplexCalculator. При этом класс, в котором реализована бизнес-логика комплексных чисел, иммутабелен и цикломатическая сложность каждого метода 1. Могу сказать, что он реализован в декларативном стиле.

Использовал подход - создание специализированных классов. Следующий способ снижения цикломатической сложности - это избавление от `if`. Сделал это через использование словарей. И ушел от явных циклов через функции высшего порядка для работы со списками.

NULL/NONE использую, так меньше кода. Можно было бы избавиться и от них через использование замыкание функций, определяемых в словаре, и пустой функцией по умолчанию.

Отметил эффект, что после нескольких итераций улучшения кода дальнейшее улучшение становится более очевидным и появляются варианты невидимые сначала.

Произошло увеличение функциональности исходного кода. Например, для умножения и деления, в отличие от сложения и вычитания, он не работал со списком чисел. Теперь работает.

##### Второй пример кода



###### Код до

Код взят отсюда: https://github.com/Python-World/python-mini-projects/blob/e0cfd4b0fe5e0bb4d443daba594e83332d5fb720/projects/GUI%20Rock-Paper-Scissors%20Game/Rock-Paper-Scissors%20Game.py#L23-L58

Рефакторить буду метод `spin`.

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
```


###### Рефлексия

Рефакторю метод `spin`, после рефакторинга сделал его частью класса Game. Первоначальная цикломатическая сложность 16, после рефакторинга 1. Такое сильное уменьшение связано с тем, что в этом методе теперь содержится высокоуровневая логика: получить ходы, вычислить результат, отобразить форму. Если раскрыть используемые методы, то там только одно условие, а значит, и при таком подходе цикломатическая сложность 2.

Для снижения цикломатической сложности избавляюсь от `if` через использование словарей и создание специализированных классов. Логика предметной области вычисления результата игры сделана в декларативном стиле с иммутабельными объектами.

Возможно, класс `Game` лучше назвать `GameForm`.


##### Третий пример кода

###### Код до

Взят отсюда: https://github.com/geekcomputers/Python/blob/808584709a9b710d7e0ece36a6ea4ffcf109b537/file_ext_changer.py#L9-L45

```python
def chxten_(files, xten):
    chfile = []
    for file in files:
        ch_file = file.split(".")
        ch_file = ch_file[0]
        chfile.append(ch_file)
    if len(xten) == len(chfile):
        chxten = []
        for i in range(len(chfile)):
            ch_xten = chfile[i] + xten[i]
            chxten.append(ch_xten)
    elif len(xten) < len(chfile) and len(xten) != 1:
        chxten = []
        for i in range(len(xten)):
            ch_xten = chfile[i] + xten[i]
            chxten.append(ch_xten)
        for i in range(1, (len(chfile) + 1) - len(xten)):
            ch_xten = chfile[-+i] + xten[-1]
            chxten.append(ch_xten)
    elif len(xten) == 1:
        chxten = []
        for i in range(len(chfile)):
            ch_xten = chfile[i] + xten[0]
            chxten.append(ch_xten)
    elif len(xten) > len(chfile):
        chxten = []
        for i in range(1, (len(xten) + 1) - len(chfile)):
            f = p(files[-i])
            p.touch(chfile[-i] + xten[-1])
            new = f.read_bytes()
            p(chfile[-i] + xten[-1]).write_bytes(new)
        for i in range(len(chfile)):
            ch_xten = chfile[i] + xten[i]
            chxten.append(ch_xten)
    else:
        return "an error occured"
    return chxten
```

###### Код после

```python
def chxten_(files, xten):
    if len(files) == 0:
        return "an error occured"

    if len(xten) == 0:
        return "an error occured"

    chfile = [file_name.split(".")[0] for file_name in files]

    xten_extend = [xten[-1]]*max(0, len(files)-len(xten))
    chfile_extend = [chfile[-1]]*max(0, len(xten)-len(files))

    result = [file_name + extension for file_name, extension in zip([*chfile, *chfile_extend], [*xten, *xten_extend])]

    # !! побочный эффект 
    if len(files) < len(xten):
        for i in range(1, (len(xten) + 1) - len(chfile)):
            f = p(files[-i])
            p.touch(chfile[-i] + xten[-1])
            new = f.read_bytes()
            p(chfile[-i] + xten[-1]).write_bytes(new)

    return result
```


###### Рефлексия

При подсчете цикломатической сложности исходного кода циклы `for file in files` по смыслу очень похожи на функции высшего порядка для работы со списками, буду считать, что они не добавляют цикломатической сложности. С другой стороны, есть циклы вида `for i in range(1, (len(chfile) + 1) - len(xten))`, для них буду добавлять в единицу цикломатическую сложность. Итого цикломатическая сложность 1 + 5 (условий) + 2 (цикла) = 8.

Код после рефакторинга имеет цикломатическую сложность 1 + 3 (условия) + 1 (цикл) = 5. Не вполне получилось уменьшить цикломатическую сложность вдвое. Одна из причин — то, что в функции был побочный эффект работы с файловой системой, и лучшим решением мне показалось его оставить как есть. Плюс не все циклы считал для подсчета цикломатической сложности первоначального варианта.

Эффектом рефакторинга с понижением цикломатической сложности стало явное выделение побочного эффекта работы с файловой системой.

Для снижения цикломатической сложности избавлялся от if. И активно использовал синтаксический сахар для работы со списками. При этом конструкции вида `[file_name.split(".")[0] for file_name in files]` считаю идентичными, если делать через `map`.


##### Итоговая рефлексия

При рефакторинге происходит более явное выделение логики, и появляются следующие шаги рефакторинга. При этом возможно даже повышение функциональности, как это случилось с калькулятором комплексных чисел.

В проекте игры, которую делаю с использованием Codex, сделал команду анализа цикломатической сложности кода. Нашел класс-"свалку" с 34 методами с цикломатической сложностью некоторых методов в 39. И WMC (Weighted Methods per Class) 328. Которая считается как сумма цикломатической сложности всех методов.

При проектировании предложил объект с 9 методами и один вспомогательный иммутабельный класс. После переписывания WMC = 116, максимальная цикломатическая сложность метода = 10, методов считая приватные = 29. Код при этом стал человекочитаемым. И даже возможен ручной рефакторинг. Есть идеи по дальнейшему улучшению этого класса, но он уже не в топе классов с наибольшей цикломатической сложностью.

Планирую использовать оценку цикломатической сложности для определения наихудших мест проекта.
