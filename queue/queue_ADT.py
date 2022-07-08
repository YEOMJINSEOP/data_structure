class Queue():
    def __init__(self):
        self.queue = []
    
    def enqueue(self, data):
        self.queue.append(data)
        
    def dequeue(slef):
        dequeue_object = None
        if self.isEmpty():
            print("Queue is Empty")
        else:
            dequeue_object = self.queue[0]
            self.queue = self.queue[1:u]
        
        return dequeue_object
    
    def peek(self): # Front에 있는 원소를 확인
        peek_object = None
        if self.isEmpty():
            print("Queue is Empty")
        else:
            peek_object = self.queue[0]
        
        return peek_object
    
    def isEmpty(self):
        is_empty = False
        if len(self.queue) == 0:
            is_empty = True
        return is_empty
