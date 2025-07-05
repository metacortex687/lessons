# DSA 1
# Section: 2. Динамические массивы

# Problem 6
# Реализовать динамический массив с доступом до элемментов в виде "myArr[1,2,3]". И возможностью меняь размер измерений. 
# Solution:
# Class name: MultiArray
# Method name: __init__ 
# Инициализирует массив. При устанвое указывается размер измерений и значение по умолчанию. 
# Колиество измерений определяется числом занчений размера измерения.
# Алгоритмическая сложность O(n) где n число элементов в многомерном масссиве
# Method name: __getitem__
# Получает элемент по иднексу вида "myArr[1,2,3]". Алгоритмическая сложность O(n) где n число элементов в многомерном масссиве
# Method name: __setitem__
# Устанавливает элемент по индексу вида "myArr[1,2,3]". Алгоритмическая сложность O(n) где n число элементов в многомерном масссиве
# Method name: resize
# Меняет размер массива сохраняя данные в нем. При попытке изменить число измерений выдает ошибку. Алгоритмическая сложность O(n)
# 
# Note:
# При выборе споосба хранения данных внутри многомерного массива, рассматривал вариант создания одномерного массива 
# и вычисления индекса в нем для хранения данных многомерного массива. 
# И вариант когда массив содержит в себе ссылки на массив размерности меньше на иденицу. 
# И вмассиве с размерностью 1, уже содержатся сохраняемые элементы.
# Выбрал второй вариант, так показался проще с точки зрения реализации. Алгоритмическая сложность обоих решений,  O(n) где n число элементов в многомерном масссиве.

# Problem 5
# Реализовать динамический массив с использованием банковского метода.
#
# Идея кажется интересной. Не вполне понял как применить этот метод к динамическому массиву. В частности что такое дешевая операция, 
# например операции вставки и удаления элементов не являются дешевыми.


import ctypes

class MultiArray:
    
    def __init__(self,*shape, default = None):
        self.shape = list(shape)
        self.default = default
        self.mult_buffer = self._make_mult_bufer(self.shape)
    
    def _make_mult_bufer(self,shape):
      
        array = (shape[0] * ctypes.py_object)()
        
        if len(shape) == 1:
            for i in range(shape[0]):
                array[i] = self.default
        else:
            for i in range(shape[0]):
                array[i] = ctypes.py_object(self._make_mult_bufer(shape[1:])) 
                
        return array
    
    
    def _copy_mult_bufer(self, shape_dist, bufer_dist, shape_source, bufer_source):
        if len(shape_dist) !=  len(shape_source):
            raise Exception("Shape mismatch: shape_dist and shape_source must have the same number of dimensions.")

        if len(shape_dist) == 1:
            for i in range(min(shape_dist[0],shape_source[0])):
                bufer_dist[i] = bufer_source[i]
        else:
            for i in range(min(shape_dist[0],shape_source[0])):
                self._copy_mult_bufer(shape_dist[1:], bufer_dist[i], shape_source[1:], bufer_source[i])
    

    def _check_coord(self,coords):
        
        if len(coords) != len(self.shape):
            raise IndexError('Too many indices for array.')            
        
        for index, size in zip(coords,self.shape):
            if index < 0 or index >= size:
                raise IndexError('Index is out of bounds.')     
              
    def _get_value(self,array, coords):
        
        result = array
        for i in range(len(coords)):
            result = result[coords[i]]
            
        return result

    def _set_value(self,array, coords, value):
        
        _array = array
        for i in range(len(coords)-1):
            _array = _array[coords[i]]
            
        _array[coords[-1]] = value        

    def resize(self,*new_shape):
        new_shape = list(new_shape)
        if len(self.shape) != len(new_shape):
            raise IndexError("Reshape error: number of dimensions must remain the same.")
        
        new_bufer = self._make_mult_bufer(new_shape)
        
        self._copy_mult_bufer(new_shape, new_bufer, self.shape, self.mult_buffer)
         
        self.shape = new_shape
        self.mult_buffer = new_bufer
        
    def __getitem__(self,coords):
        coords = list(coords)
        self._check_coord(coords)
        return self._get_value(self.mult_buffer,coords)

        
    def __setitem__(self, coords, value):
        coords = list(coords)
        self._check_coord(coords)
        self._set_value(self.mult_buffer,coords,value)

