

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f'Valor del nodo es: {self.value}'


class LinkedList:

    def __init__(self):
        self.first = None

    def append(self, value):
        node = Node(value)
        if self.first is not None:
            node.next = self.first
        self.first = node

    def print_nodes(self):
        node = self.first
        while node:
            print(node)
            node = node.next


def main():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.print_nodes()


if __name__ == '__main__':
    main()
