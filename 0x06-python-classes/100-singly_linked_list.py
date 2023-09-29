#!/usr/bin/python3

"""classes"""


class Node:
    """Node"""

    def __init__(self, data, next_node=None):
        """new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter"""
        return (self.__data)

    @data.setter
    '''setter'''
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getters"""
        return (self.__next_node)

    @next_node.setter
    '''setter'''
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class"""

    def __init__(self):
        """Initalization"""
        self.__head = None

    def sorted_insert(self, value):
        """insert"""
        n = Node(value)
        if (self.__head is None):
            n.next_node = None
            self.__head = n
        elif (self.__head.data > value):
            n.next_node = self.__head
            self.__head = n
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            n.next_node = tmp.next_node
            tmp.next_node = n

    def __str__(self):
        """str"""
        value = []
        tmp = self.__head
        while tmp is not None:
            value.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(value))
