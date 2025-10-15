class ArrayList:
    def __init__(self):
        self.array = []
        self.curr_size = 1

    def update_size(self):
        self.curr_size = int(self.curr_size * 1.5 + 1)

    def is_place(self) -> bool:
        return len(self.array) < self.curr_size

    def add_data(self, data):
        if not self.is_place():
            self.update_size()

        self.array.append(data)

    def show_array(self):
        if not self.array:
            print("array is empty.")
            return
        print(f"array: {self.array}")

    def array_getter(self):
        if not self.array:
            raise ValueError("array is empty.")
        return self.array

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_data(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node       # -> determinate next link
            new_node.previous = self.tail   # -> determinate previous link
            self.tail = new_node            # -> set next value

    def show_list(self):
        current_element = self.head
        print("linked_list: ", end="")
        while current_element:
            print(current_element.data, end=" <-> ")
            current_element = current_element.next
        print("end")

    def list_getter(self):
        if self.head is None:
            raise ValueError("linkedlist is empty.")

        linkedlist = []
        current_element = self.head
        while current_element:
            linkedlist.append(current_element.data)
            current_element = current_element.next

        return linkedlist

def read_file(file):
    with open(file, "r") as r:
        line = r.readline().strip()

    if not line:
        raise IndexError("error: file is empty.")

    data = [d for d in line.split(",")]
    print(f"parsed numbers: {data}")
    return data

def distribute_data(data, array, linkedlist):
    for n, i in enumerate(data, start=1):
        if n % 2 == 0:  # -> even
            linkedlist.add_data(i)
        else:
            array.add_data(i)

def write_file(file, array, linkedlist):
    with open(file, "a") as a:
        try:
            a.write("array_list: " + str(array.array_getter()) + "\n")
            a.write("linked_list: " + str(linkedlist.list_getter()) + "\n")
        except ValueError as v:
            print(f"error: {v}")
            exit(1)

if __name__=="__main__":
    try:
        data = read_file("data.txt")
    except ValueError as e:
        print(f"error: {e}.")
        exit(1)
    except IndexError:
        print("error: file is empty.")
        exit(1)

    array = ArrayList()
    linked_list = LinkedList()

    distribute_data(data, array, linked_list)

    array.show_array()
    linked_list.show_list()

    write_file("data_result.txt", array, linked_list)