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
        pairs = zip(nums[0:len_nums-1],nums[1:len_nums])

        return list(map(lambda real, complex: ComplexNumber(real, complex), pairs))
        


