#!/usr/bin/python3
"""module for linked list"""


class Node:
    """Singly linked list node"""
    def __init__(self, data, next_node=None):
        """initialize Node"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """data getter"""
        return self.__data

    @data.setter
    def data(self, data):
        """data setter"""
        if not isinstance(size, int):
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        """next_node getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        """next node setter"""
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node


class SinglyLinkedList:
    """Singly linked list"""


    __head = None

    def __init__(self):
        """initializer"""
        pass

    def sorted_insert(self, value):
        """inserts node"""
        if self.__head == None:
            self.__head = Node(value)
        else:
            list_ = self.__head

            while list_ is not None:
                if list_.data is not None:
                    if list_.data < value:
                        break
                list_ = list_.next_node
                # print("loo {}".format(list_.data))

            node = Node(None)

            node.next_node = list_.next_node
            list_.next_node = node
            self.__head = list_
