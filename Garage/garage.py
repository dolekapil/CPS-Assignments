
"""
CSCI-603: Lab 8
Author-1: Kapil Dole (kmd1712@g.rit.edu)

This program takes file as a input which contains jobs and which person is ready to take up
the job. Both Cathy and Howard pickup job based on their priority, Cathy picks up job with
maximum cost whereas Howard picks up job with minimum time. Adding and removing of jobs are
done in O(log(n)).
"""

import sys
from jobs import Job
from garage_heap import GarageHeap

def main():
    '''
    This is main function which takes file containing jobs as input and prints whoever
    is doing job.
    :return: None.
    '''
    cathy = GarageHeap(lambda x, y: x.cost > y.cost)
    howard = GarageHeap(lambda x, y: x.time < y.time)
    file = input("Enter the name of the file which contains garage jobs.")
    try:
        fileHandle = open(file)
        for line in fileHandle:
            line = line.strip()
            data = line.split()
            if len(data) == 3 and data[1].isnumeric() and data[2].isnumeric():
                n = Job(data[0], int(data[1]), int(data[2]))
                cathy.insertHeap(n)
                howard.insertHeap(n)
                print(n)
            elif len(data) == 2 and (data[0] == 'Cathy' or data[0] == 'cathy') and data[1] == 'ready':
                    job = cathy.popHeap()
                    print("Cathy starting job", job.name)
            elif len(data) == 2 and (data[0] == 'Harold' or data[0] == 'harold') and data[1] == 'ready':
                job = howard.popHeap()
                print("Harold starting job", job.name)
            else:
                print("Invalid input, please try again with valid input.")
                sys.exit(0)
    except FileNotFoundError:
        print("please enter valid file name.")
        sys.exit(0)

if __name__ == '__main__':
    main()