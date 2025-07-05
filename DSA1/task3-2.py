# DSA 1
# Section: 2. Dynamic Arrays

# Problem 6
# Implement a dynamic multi-dimensional array with access via syntax like "myArr[1, 2, 3]",
# and the ability to resize dimensions.

# Solution:
# Class name: MultiArray
# Method name: __init__
# Initializes the array. At initialization, the dimension sizes and default value are specified.
# The number of dimensions is determined by the number of size arguments.
# Time complexity: O(n), where n is the number of elements in the multi-dimensional array.

# Method name: __getitem__
# Retrieves an element using an index of the form "myArr[1, 2, 3]".
# Time complexity: O(n), where n is the number of elements in the multi-dimensional array.

# Method name: __setitem__
# Sets an element using an index of the form "myArr[1, 2, 3]".
# Time complexity: O(n), where n is the number of elements in the multi-dimensional array.

# Method name: resize
# Changes the array’s size while preserving the data.
# Raises an error if an attempt is made to change the number of dimensions.
# Time complexity: O(n)

# Note:
# When choosing the internal storage strategy for the multi-dimensional array,
# I considered two options:
# 1) Using a one-dimensional array with index computation for accessing multidimensional data.
# 2) Using nested arrays, where each level is a list containing sub-arrays of one lower dimension,
# and the innermost dimension stores the actual elements.
# I chose the second approach, as it seemed simpler to implement.
# The time complexity of both approaches is O(n), where n is the number of elements in the array.

# Problem 5
# Implement a dynamic array using the accounting (banker's) method.
#
# The idea seems interesting, but I'm not entirely sure how to apply this method to a dynamic array.
# Specifically, it's unclear what would count as a "cheap" operation,
# since insertions and deletions are generally not cheap.


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

