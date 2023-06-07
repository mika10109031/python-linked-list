class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None


    def add_to_front(self,data):
        new_node = node (data)
        new_node.next = self.head
        self.head = new_node

    def add_to_add(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove_front(self):
        if self.head is None:
            return
        
        self.head = self.head.next

    def remove_end(self):
        if self.head is None:
            return
        
        if self.head.next is None:
            self.head = None
            return
        
        current = self.head
        while current.current.next.next:
            current = current.next
            current.next = None


    def print_linked_list(self):
        current = self.head
        while current:
            print(current.data, end= " ")
            current = current.next
        print()

linked_list = linkedList()

linked_list.add_to_front(3)
linked_list.add_to_front(2)
linked_list.add_to_front(1)


linked_list.add_to_front(4)
linked_list.add_to_front(5)
linked_list.add_to_front(6)

print("linked list awal:")
linked_list.print_linked_list()


linked_list.remove_front()
linked_list.remove_end()

print("linked list setelah penghapusan:")
linked_list.print_linked_list()




