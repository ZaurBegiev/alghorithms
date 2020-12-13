from typing import Any, Union


class MinHeap:
    def __init__(self):
        self.data = [0]
        self.current_size = 0
    
    def __len__(self) -> int:
        return len(self.data)
 
    def sift_up(self, index: int) -> None:
        while index // 2 > 0:
            parent_index = index // 2
            if self.data[index] < self.data[parent_index]:
                self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
            index = index // 2
 
    def insert(self, k: int) -> None:
        self.data.append(k)
        self.current_size += 1
        self.sift_up(self.current_size)
 
    def sift_down(self, i: int) -> None:
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.data[i] > self.data[mc]:
                self.data[i], self.data[mc] = self.data[mc], self.data[i]
            i = mc
 
    def min_child(self, i: int) -> int:
        if (i * 2)+1 > self.current_size:
            return i * 2
        else:
            if self.data[i*2] < self.data[(i*2)+1]:
                return i * 2
            else:
                return (i * 2) + 1
 
    def delete_min(self) -> Union[None, str]:
        if len(self) == 1:
            return 'Empty heap'
 
        root = self.data[1]
 
        self.data[1] = self.data[self.current_size]

        *self.data, _ = self.data
 
        self.current_size -= 1
 
        self.sift_down(1)

        return root

    def __repr__(self):
        return str(self.data)

my_heap = MinHeap()
my_heap.insert(5)
my_heap.insert(6)
my_heap.insert(7)
my_heap.insert(9)
my_heap.insert(13)
my_heap.insert(11)
my_heap.insert(10)

print(my_heap.delete_min())
print(my_heap)