# Exercise 8.1: Modified MergeSort
# To get a more concrete example you can check this blog 
# https://developer.nvidia.com/blog/merge-sort-explained-a-data-scientists-algorithm-guide/

class ModifiedMergeSort:
    def __init__(self, data):
        '''instantiate two class attributes'''
        self.data = list(set(data))
        self.pieces = []
        # self.__make_atoms()
   
    def __make_atoms(self):
        '''private method''' 
        self.pieces = [[n] for n in self.data]
        # return self.pieces

    def __combine(self):
        '''another private method that does the 'upward combine' part of Mergesort'''
        self.updated_pieces = [] # This ?? variable ?? will hold the combined (sorted) result of left subpiece and the right subpiece
        if len(self.pieces)%2 != 0: # this method only work if the length of the pieces attribute is divisible by 2
            self.pieces[-2] += self.pieces[-1]
            self.pieces.pop()

        for i in range(0, len(self.pieces), 2):
            merged = self.__subpiece_sort(self.pieces[i]+self.pieces[i+1])
            self.updated_pieces.append(merged)
        
        self.pieces = self.updated_pieces
        # return self.pieces
    
    def __subpiece_sort(self, subpieces):
        '''private method'''
        for h in range(len(subpieces)):
            for i in range(len(subpieces)-h-1):
                if subpieces[i] > subpieces[i+1]:
                    temp = subpieces[i]
                    subpieces[i] = subpieces[i+1]
                    subpieces[i+1] = temp

        return subpieces
    
    def sorting(self):
        '''orchestrates the entire sorting procedure'''
        if not self.data:
            return self.data
        # while len(self.pieces) > 1:
        #     self.__combine()
        # return self.pieces[0]
        return [n for piece in self.pieces for n in piece]
    

## Create BinarySearch class ##   
class BinarySearch:
    def __init__(self, data):
        '''initiate a constructor'''
        self.data = data # a sorted list
        
    def search(self, val):
        if not self.data:
            return False
        start_ind = 0
        end_ind = len(self.data)-1
        mid_ind = (start_ind+end_ind)//2
        
        while (self.data[mid_ind] != val) and start_ind<=end_ind:
            if val < self.data[mid_ind]:
                end_ind = mid_ind - 1
            else:
                start_ind = mid_ind + 1 
            mid_ind = (start_ind+end_ind)//2
            
        if self.data[mid_ind]==val:
            return True
        else:
            return False
        
if __name__ == '__main__':
    # sample = [6, 2, 5, 1, 9]
    sample = [-32, -18, -35, -666]
    merge = ModifiedMergeSort(sample)
    khojThesearch = BinarySearch(sample)

    merge._ModifiedMergeSort__make_atoms()
    print(merge.pieces)
    merge._ModifiedMergeSort__combine()
    # print(merge.pieces)
    # print(merge._ModifiedMergeSort__combine())



    print(merge.sorting())
    print(khojThesearch.search(-32))