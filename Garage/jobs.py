
class Job:
    '''
    Class job stores name of job, time it takes to complete, cost required and whether it is
    done or not.
    '''
    __slots__='name','time','cost','done'

    def __init__(self,name,time,cost):
        '''
        Constructor that takes name, time and cost for the job.
        :param name: name of job.
        :param time: time required to complete the job.
        :param cost: Estimated cost required.
        :return: None.
        '''
        self.name = name
        self.time = time
        self.cost = cost
        self.done = False

    def __str__(self):
        '''
        It returns string representation of the job in below format.
        :return: String representation of job.
        '''
        return "New job arriving! Job name: " + self.name + ", "+str(float(self.time)) + " hours and $"+str(float(self.cost))