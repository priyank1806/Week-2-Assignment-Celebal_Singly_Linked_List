# Node class representing each node in the list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class managing the nodes
class LinkedList:
    def __init__(self):
        self.head = None

    # Add node to the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Print the linked list
    def print_list(self):
        if not self.head:
            print("List is Empty")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Delete the nth node (1-based index)
    def delete_nth_node(self, n):
        try:
            if not self.head:
                raise Exception("Cannot Delete from an Empty List")

            if n <= 0:
                raise IndexError("Index must be >= 1 ")

            if n == 1:
                self.head = self.head.next
                return

            current = self.head
            for i in range(n - 2):
                if not current.next:
                    raise IndexError("Index out of Range")
                current = current.next

            if not current.next:
                raise IndexError("Index out of Range")

            current.next = current.next.next

        except Exception as e:
            print("Error:", e)

# Sample Test
if __name__ == "__main__":
    my_list = LinkedList()
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    my_list.append(40)

    print("Original List:")
    my_list.print_list()

    print("\nDeleting 2nd Node️")
    my_list.delete_nth_node(2)

    print("Updated List:")
    my_list.print_list()

    print("\nTrying to Delete 5th Node (out of range)")
    my_list.delete_nth_node(5)
