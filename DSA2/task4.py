# Section: 3. Tree Traversal Methods

# Task 3
# Method that returns the key values in breadth-first traversal

# Class: aBST
# Method: WideAllNodes(self) -> list[int]
# - kept the method name for compatibility in case it is used in automatic testing.
# Time Complexity: O(n) - where n is the size of the array

# Solution: In the  array representation of the tree, 
# the elements are already in the required order,
# in those cells where a value is set.


class aBST:

    def __init__(self, depth):

        tree_size = pow(2,depth+1)-1
        self.Tree = [None] * tree_size 
	
    def FindKeyIndex(self, key):
        return self._FindKeyIndex(key,0)
    
    def _FindKeyIndex(self, key, index):
        if index >= len(self.Tree):
            return None
        
        if self.Tree[index] is None:
            return None
        
        if self.Tree[index] == key:
            return index
        
        return self._FindKeyIndex(key,self._NextIndex(key,index))


    def _NextIndex(self,key,index):
        if self.Tree[index] == key:
            return index

        if self.Tree[index] > key:
            return index*2+1
        
        return index*2+2
      
    def WideAllNodes(self) -> list[int]:
        return [key for key in self.Tree if key is not None]

    def _AddKey(self,key, index):
        if index >= len(self.Tree):
            return -1
        
        if self.Tree[index] is None:
            self.Tree[index] = key
            return index 
        
        if self.Tree[index] == key:
            return index
        
        return self._AddKey(key,self._NextIndex(key,index))

        
    def AddKey(self, key):
        return self._AddKey(key,0); 

