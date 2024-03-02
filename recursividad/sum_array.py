class SumArray:

    def sum_array(self, arr, index):
        if index >= len(arr):
            return 0
        else:
            return arr[index] + self.sum_array(arr, index + 1)
        
    def push(self, arr, element):
        arr += [element]
        return arr
    
    def print_array(self, arr):
        print(arr)