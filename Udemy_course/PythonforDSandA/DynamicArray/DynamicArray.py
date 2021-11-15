import ctypes


class DynamicArray(object):
    '''
    DYNAMIC ARRAY CLASS (Similar to Python List)
    '''

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        """
        Return number of elements sorted in array
        """
        return self.n


    def __getitem__(self, k):
        """
        Return element at index k
        """
        if not 0<=k<=self.n:
            return IndexError('K is out of bounds!')
        return self.A[k]

    def append(self, ele):
        """
        Add element to end of the array
        """
        if self.n == self.capacity:
            self._resize(2*self.capacity)

        self.A[self.n] = ele
        self.n += 1

    def _resize(self, new_cap):
        """
        Resize internal array to capacity new_cap
        """
        B = self.make_array(new_cap)
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
        self.capacity = new_cap

    def make_array(self, new_cap):
        """
        Returns a new array with new_cap capacity
        """
        return (new_cap * ctypes.py_object)()



arr = DynamicArray()
arr.append(1)
print(len(arr))
arr.append(2)
print(len(arr))
print(arr[1])
