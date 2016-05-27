
import sys
class GarageHeap:
    '''
    Garage Heap that orders jobs by a given comparison function.
    '''
    __slots__ = 'data', 'size', 'above_fn'

    def __init__(self, above_fn):
        '''
        Constructor takes a comparison function.
        :param above_fn: Function that takes in two heap objects and returns true if comparison
        returns true in the above function.
        '''
        self.data = []
        self.size = 0
        self.above_fn = above_fn

    def insertHeap(self, job):
        '''
        Inserts a job into the heap and increases its size.
        :param job: job to be inserted
        '''
        self.data.append(job)
        self.size += 1
        self.bubbleUpHeap(self.size-1)

    def parent(self,position):
        '''
        Function to compute the parent location of a position.
        :param position: position in the heap
        :return: position of parent
        '''
        return (position-1)//2

    def bubbleUpHeap(self, position):
        '''
        Starts from the given position and moves the job up into heap as far as necessary.
        :param position: Place to start bubbling up from.
        '''
        while position > 0 and self.above_fn(self.data[position], self.data[self.parent(position)]):
            self.data[position],self.data[self.parent(position)] = \
                self.data[self.parent(position)],self.data[position]
            position = self.parent(position)

    def popHeap(self):
        '''
        Checks if job on top is already done or not, if its done then keep popping jobs
        till you get unfinished job and then remove that job and return.
        :return: Unfinished Job on top of the heap
        '''
        temp = self.data[0]
        while temp.done is True and self.size > 0:
            self.__popHeap()
            temp = self.data[0]
        if self.size > 0:
            self.__popHeap()
            temp.done = True
        else:
            print("No more jobs to do!!")
            sys.exit(0)
        return temp

    def __popHeap(self):
        '''
        Helper function for popping job from the heap.
        :return: None
        '''
        self.size -= 1
        if self.size > 0:
            self.data[0] = self.data.pop(self.size)
            self.bubbleDownHeap(0)

    def bubbleDownHeap(self, position):
        '''
        Starts from the given position and moves the job as far down the
        heap as necessary.
        :param position: Place to start bubbling down from.
        :return: None
        '''
        swap = self.topHeap(position)
        while swap != position:
            self.data[position], self.data[swap] = self.data[swap], self.data[position]
            position = swap
            swap = self.topHeap(position)

    def topHeap(self, position):
        '''
        Finds the value among position and it's two children that should be at
        the top and correctly handles end-of-heap issues.
        :param position: Index of job
        :return: position of top value
        '''
        leftChild = position*2+1
        rightChild = position*2+2
        if leftChild >= self.size:
            return position
        if rightChild >= self.size:
            if self.above_fn(self.data[position], self.data[leftChild]):
                return leftChild
            else:
                return position

        if self.above_fn(self.data[leftChild], self.data[rightChild]):
            if self.above_fn(self.data[position], self.data[leftChild]):
                return position
            else:
                return leftChild
        else:
            if self.above_fn(self.data[position], self.data[rightChild]):
                return position
            else:
                return rightChild
