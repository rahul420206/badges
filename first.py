class Node:
    # Defines a node with a value and a pointer to the next node
    def __init__(self, data):
        self.data = data  # Stores the node value
        self.next = None  # Pointer to the next node (initially None)

class LinkedList:
    # Defines the linked list with a head node
    def __init__(self):
        self.head = None  # Initially, the list is empty

    def append(self, data):
        # Adds a new node to the end of the linked list
        new_node = Node(data)  # Create a new node
        if not self.head:
            self.head = new_node  # If the list is empty, set new node as head
            return
        temp = self.head  # Start from the head node
        while temp.next:
            temp = temp.next  # Move to the last node
        temp.next = new_node  # Link the last node to the new node

    def remove_duplicates(self):
        # Removes duplicate nodes from a sorted linked list
        temp = self.head  # Start from the head node
        while temp and temp.next:
            if temp.data == temp.next.data:  # Check if current and next node have the same value
                temp.next = temp.next.next  # Skip the duplicate node
            else:
                temp = temp.next  # Move to the next node if no duplicate found

    def print_list(self):
        # Prints the linked list elements
        temp = self.head  # Start from the head node
        while temp:
            print(temp.data, end=" -> ")  # Print the current node's data
            temp = temp.next  # Move to the next node
        print("None")  # Indicate the end of the list

# Example usage:
ll = LinkedList()
ll.append(1)
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(3)

print("Original Linked List:")
ll.print_list()

ll.remove_duplicates()  # Remove duplicate nodes

print("After Removing Duplicates:")
ll.print_list()
