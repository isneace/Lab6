"""
Date: 10/4/2018
Developer: Isaac Neace
Program: Lab 6

Description: Opens a .dat file and splits up each task according to how long it takes
             For example if there is a process that takes 3 seconds it will go into
             Queue 1. If the process is longer than 3 seconds it will go into queue 2
             and if the process is longer than 100 seconds it will go into queue 3
             
"""

from Queue2 import Queue2


#Creates an object to seperate the two columns in the text file
class TimeNode():
    def __init__(self, mil, task):
        self.mil = mil
        self.task = task

    def getMil(self):
        return self.mil
    def getTask(self):
        return self.task

    def updateMil(self, mil):
        self.mil = mil
    def updateTask(self, task):
        self.task = task


fp = open("Linux_multipleQs-Jobs.dat", "r") #Opens text file and reads it.

#Creates 3 queues
Q1 = Queue2()
Q2 = Queue2()
Q3 = Queue2()

#Reads the text file and enqueue the values into Q1 (the first queue)
while True:
    line = fp.readline()
    if line == "":
        break


    line = line.strip()
    field = line.split()
    instruction = field[0]
    time = field[1]

    ms = "ms"

    for ms in (time):
        newTime = time.replace("ms", "") #filters out the ms in each time value to convert to a number

    timeFloat = float(newTime)
    index = TimeNode(timeFloat, instruction)
    Q1.enqueue(index)

avg1 = 0
avg2 = 0
avg3 = 0

#Scans through all of the first queue to filter out the processes that are longer than 3 seconds
for i in range(Q1.size()):
    current = Q1.dequeue()
    process = current.getData()
    

    if process.getMil() <= 3.0:
        Q1.enqueue(process)
        avg1 += process.getMil()

    #Adds the processes that have longer times than 3 to the second queue
    elif process.getMil() > 3.0:
        newProcess = float(process.getMil()) - 3.0
        Q2.enqueue(newProcess)
        #print type(newProcess), newProcess


#print Q2.size()
#Filters out the processes that are longer than 100 seconds
for i in range(Q2.size()):
    
    current = Q2.dequeue()
    process = current.getData()
    #print type(process), process
    if process > 3.0 and process <= 100.0:
        Q2.enqueue(process)
        avg2 += process

    #Adds the processes that are longer than 100 seconds to the 3rd queue
    elif process > 100.0:
        newProcess = process - 100.0
        Q3.enqueue(newProcess)
        avg3 += process
        #print process
                

#Calculates the final averages of each queue         
finalAVG1 = avg1 / Q1.size()
finalAVG2 = avg2 / Q2.size()
finalAVG3 = avg3 / Q3.size()

#Print results
print "In queue 1 there are: ", Q1.size(), " instructions"
print "In queue 2 there are: ", Q2.size(), " instructions"
print "In queue 3 there are: ", Q3.size(), " instructions"

print "The average of queue 1: ", finalAVG1
print "The average of queue 2: ", finalAVG2
print "The average of queue 3: ", finalAVG3

"""
In queue 1 there are:  2942  instructions
In queue 2 there are:  1459  instructions
In queue 3 there are:  551  instructions
The average of queue 1:  1.98631203263
The average of queue 2:  51.3311651816
The average of queue 3:  5041.40593466
"""

        
        

    
    
