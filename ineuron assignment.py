#!/usr/bin/env python
# coding: utf-8

# In[6]:


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0


# In[8]:


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())      
print(stack.is_empty()) 

print(stack.pop())      
print(stack.pop())      
print(stack.is_empty()) 


# In[ ]:


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0


# In[9]:


queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())      
print(queue.is_empty())     

print(queue.dequeue())      
print(queue.dequeue())      
print(queue.is_empty())     


# In[ ]:





# In[ ]:




