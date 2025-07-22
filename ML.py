data = [
{"id": "101", "priority": "normal"},
{"id": "102", "priority": "urgent"},
{"id": "103", "priority": "urgent"},
{"id": "104", "priority": "normal"},
{"id": "105", "priority": "normal"},
{"id": "106", "priority": "urgent"}
]
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class EmergrencyQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def is_empty(self):
        return self.head is None and self.tail is None
    
    def enqueue(self, report):
        new_report = Node(report)
        if self.is_empty():
            self.head = self.tail = new_report
            return
        if report['priority'] == "normal":
            self.tail.next = new_report
            new_report.prev = self.tail
            self.tail = new_report
            return
        current = self.head
        while current and current.data['priority'] == "urgent":
            current = current.next
        if current is None:
            self.tail.next = new_report
            new_report.prev = self.tail
            self.tail = new_report
        elif current == self.head:
            new_report.next = self.head
            self.head.prev = new_report
            self.head = new_report
        else:
            prev_node = current.prev
            prev_node.next = new_report
            new_report.prev = prev_node
            new_report.next = current
            current.prev = new_report
            
    def dequeue(self):
        if self.is_empty():
            return None
        removed = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return removed.data
    
    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
        print()
        
queue = EmergrencyQueue()
for report in data:
    queue.enqueue(report)
    
queue.display()