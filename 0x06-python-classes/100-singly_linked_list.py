#!/usr/bin/python3
"""define node of singly-linked list"""


class Node:
    """singly-linked list node rep"""

    def __init__(self, data, next_node=None):
        """new node initialization"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """set data"""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """set next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """singly-linked list"""

    def __init__(self):
        """Initalization"""
        self.__head = None

    def sorted_insert(self, value):
        """new node insertion to the SinglyLinkedList"""
        i = Node(value)
        if self.__head is None:
            u.next_node = None
            self.__head = i
        elif self.__head.data > value:
            i.next_node = self.__head
            self.__head = i
        else:
            j = self.__head
            while (j.next_node is not None and
                    j.next_node.data < value):
                j = j.next_node
            i.next_node = j.next_node
            j.next_node = i

    def __str__(self):
        """print rep. of a SinglyLinked list"""
        values = []
        j = self.__head
        while j is not None:
            values.append(str(j.data))
            j = j.next_node
        return ('\n'.join(values))
