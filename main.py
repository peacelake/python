import click
from time import sleep
# from array import array


class Inteval:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper


class Sample:
    def __init__(self, len):
        self.length = len

    # @staticmethod
    def progressbar(self):
        with click.progressbar(length=100, label='Running %') as bar:
            for i in range(self.length):
                bar.update(i)
                sleep(0.1)

    def printarray(self, arr):
        print ', '.join(str(x) for x in arr)

    def mergesort(self, arr):
        length = len(arr)
        self.mergecore(arr, 0, length - 1)

    def mergecore(self, arr, start, end):
        if start >= end:
            return

        mid = (start + end) / 2;
        self.mergecore(arr, start, mid)
        self.mergecore(arr, mid + 1, end)
        self.domerge(arr, start, mid, end)

    def domerge(self, arr, start, mid, end):
        temp = []
        i = start
        j = mid + 1
        k = 0
        while i <= mid and j <= end:
            if arr[i] < arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1

        if i <= mid:
            while i <= mid:
                temp.append(arr[i])
                i += 1

        if j <= end:
            while j <= end:
                temp.append(arr[j])
                j += 1

        arr[start:end + 1] = temp

    def createGenerator(self):
        mylist = range(3)
        for i in mylist:
            yield i

    #def MergeInterval(self, listeA, listB):

sample = Sample(100)
sample.progressbar()

myGenerator = sample.createGenerator()
for i in myGenerator:
    print(i)
    
data = [5, 1, 3, 8, 7, 4, 2, 9, 6]
sample.printarray(data)
sample.mergesort(data)
sample.printarray(data)

# inteval = Inteval(-10, -1)
# print(inteval.lower, inteval.upper)

q2data1 = [10, -1, 0, 2, 4, 10]
q2data2 = [-5, 1]


