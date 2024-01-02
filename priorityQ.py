'''Your work is to allow people to enter the queue one by one. But, there is a catch, there are priority members, whom you need to allow to enter first. 
In front of the bar, you installed an old metal stick and added a circuit to it so it can connect to the internal computer of the bar.

Now you start coding up programs so that the metal stick will shift when someone should enter else it would remain straight blocking the entrance.

Moreover, you also saw that there are many people who come and join the queue at the front without going to the back, the stick shouldn't allow 
such actions and would not move if they don't go and stand at the back of 
the queue. Finally, you also need to set up the priority member entrance 
routine to the program to make it exactly similar to your work. 


Exercise 7.1: Managing Queue
To make your metal stick maintain the queue (or line), you define a class Queue.
In this Queue class you need to do the following task, so that the metal performs 
the task similar to you being a bouncer.

Tasks

- The metal stick must know who are there in the queue. 
For that reason, initialize a constructor which receives an argument data of the 
datatype list. 
Store this argument as a class attribute, data, for further use.'''
class Q:
    def __init__(self, data=[]): # initialize a constructor which receives an argument data
                                 # of the datatype list
        self.data = data        # Store this argument as a class attribute, data, 
                                # for further use
 
        # class attributes are variables stored within the class such that they are 
        # accessible to all other methods of a class. 
    '''
    - Your stick must let each person from the queue enter. 
    For this, you must create a method named dequeue(self). 
    It doesn't need to receive any argument, but it must update the 
    class attribute data at the end. The dequeue method must check if the 
    class attribute data is not empty. If it is not empty, 
    it should remove the first element from data and return it. 
    If data is empty, it should return None.'''

    def dequeue(self):
            if len(self.data)==0:
                return None
            else:
                return self.data[0]
            
            del self.data[0]
    '''- Now you must make a solution for adding people who are coming late at the end 
    of the queue. 
    There might be single people or a group of people who are coming and joining the queue. 
    So your stick must accommodate a solution for both of these scenarios. For this, 
    you create an enqueue(self) method which receives an argument person. 
    Check for the datatype of person and add it to the end of the class attribute data 
    if person is a float or int, else if it is a list or a tuple, 
    extend the class attribute data to add each element of person to it.'''
    
    def enqueue(self, person):
            if isinstance(person, int) or isinstance(person, float):
                self.data.append(person)
            elif isinstance(person, list) or isinstance(person, tuple):
                self.data.extend(person)

    def is_member(self, person):
        if person in self.data:
            return True
        else:
            return False
        
# '''
# Exercise 7.2: Managing Priorities
# Now you must create your solution and program it to the metal stick for 
# incorporating priority members. 
# For this you need to create a PriorityQueue class, which inherits from the previous 
# Queue class. After you have created the PriorityQueue class do the following tasks.

# Tasks

# -Initialize a constructor which receives two arguments data and priority  
# each of the datatype list. 
# Call the parent's class constructor (by using super keyword) 
# and pass the data argument to it. 
# This will automatically create a class attribute data.
# But, our class attribute data should also incorporate priority. 
# So, update the class attribute data such that it now uses the priority too. 
# Suppose the argument, data = [1,2,3] and priority = [22 , 11 , 67], 
# then you should formulate the class attribute data such that 
# self.data = [(1, 22), (2, 11), (3, 67)].
# '''
# class PriorityQ(Q):
#     def __init__(self, data=[], priority=[]):
#         super().__init__(data)
#         self.data = list(zip(data, priority))
#         self.priority = priority
    
#     '''
#     - Create a method sorted_queue(self), which doesn't take any argument. 
#     This method just sorts the class attribute self.data  based on the priority. 
    
#     Remember: The self.data attribute is a list of tuples, 
#     where each tuple contains 2 elements - the first is the person and 
#     the second is the priority. You need to sort the self.data such that the tuple 
#     with the highest priority value (2nd element of the tuple) 
#     will come at the index-0 of the list (self.data) and so on.
#     In this context, a higher numerical value represents a higher priority.  
#     '''
#     def sorted_queue(self):
#             self.data = sorted(self.data, key=lambda person_priority:person_priority[1], reverse=True)

#     '''
#     - Just like the normal Queue class implement the enqueue method. 
#     But there is a short difference here. The enqueue method here receives two arguments, 
#     person and priority. 
#     You need to make a tuple using the two arguments with the person 
#     as the first element of tuple and the priority as the second element. 
#     You need to add this tuple to the end of the self.data attribute. 
#     Also, you must sort the self.data attribute after adding to make the 
#     prioritized members stand at the beginning of the line.'''
    
#     def enqueue(self, person, priority):
#         self.data.append((person, priority))
#         self.sorted_queue()
         
#     '''
#     -Similarly, implement the dequeue method. You must sort the self.data attribute 
#     and then dequeue. 
#     ( Also don't forget to check if the self.data attribute is empty or not!)
#     '''
#     def dequeue(self):
#         if self.data:
#             self.sorted_queue()
#             self.data.pop(0)

#     def is_member(self, person):
#         for person_priority in self.data:
#             if person == person_priority[0]: 
#             # self.data attribute consists of tuples. 
#             # Each tuple is of size 2, with the person at the index-0 of the tuple.
#                 return True
                
#         return False
    
# '''
# Exercise 7.3: Improving PriorityQueue
# Let's analyze the time complexity of each method in the PriorityQueue we implemented 
# in 7.2. The time complexity of enqueue() and dequeue() is O(NlogN), 
# with N representing the length of self.data. 
# The reason is that both methods use Python's sorted() function, 
# and the time complexity of the sorted() function is O(NlogN). 
# Additionally, is_member() has a time complexity of O(N) in the worst case, 
# as it needs to visit each member of self.data.
# Now, let's implement the ImprovedPriorityQueue class with improved performance 
# for the enqueue() and dequeue() methods, following the tasks.
# '''


# class ImprovedPriorityQ:
#     def __init__(self, data=[], priority=[]):
#         super().__init__(data)
#         self.data = list(zip(data, priority))
#         self.priority = priority
#         self.size = 0
import heapq
class PriorityQueue:
    def __init__(self) -> None:
        self.q = []
        self.index = 0

#     '''' 
#     - Similar to the 7.2 implementation, the enqueue method takes two arguments: 
#     person and priority. Create a tuple with person as the first element 
#     and priority as the second, then add this tuple to the end of self.data. 
#     Unlike 7.2, sorting self.data is not required.
#     '''
    def enqueue(self, person, priority):
        if isinstance(person, (float, int)) and isinstance(priority, (float, int)):
                self.data.append((person, priority))
                
        elif isinstance(person, (list, tuple)) and isinstance(priority, (list, tuple)):
            entries = list(zip(person, priority))
            for entry in entries:
                self.data.append(entry)
        
    def enQ(self, item, priority):
        heapq.heappush(self.q, (priority, self.index, item))
        self.index += 1

#     '''
#     - In the dequeue method, first, iterate through self.data to find the 
#     tuple with the highest priority. Then, remove the found tuple from self.data,
#     and return the person, which is the first element of the found tuple. 
#     If self.data is empty, it have to return None. 
#     Similar to enqueue(), in dequeue() as well, we do not perform sorting.
#     '''
    
    def dequeue(self):
        highest_priority = 0
        if self.data:
            for i in self.data:
                if i[1] > highest_priority:
                    highest_priority = i[1]
            for i in self.data:        
                if highest_priority == i[1]:
                    highest_priority_tupl = i
                    self.data.remove(highest_priority_tupl)

            return highest_priority_tupl[0]
        else:
            return None
        
    def dQ(self):
        return heapq.heappop(self.q)[-1]
    

#     def is_member(self, person):
#         return any(person == entry[0] for entry in self.data) 

        

 
    