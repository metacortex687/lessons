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
        pairs = zip(nums[0:len_nums-1:2],nums[1:len_nums:2])

        return list(map(lambda real, complex: ComplexNumber(real, complex), pairs))
        
```

###### Рефлексия

