#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 11:33:17 2024

@author: sakinahrosli
"""


class Tree:
    # initialize nodes position
    def __init__(self, content, left=None, right=None):
        self.content = content
        self.left = left
        self.right = right


def averagePositive(tree):
    # create empty list to store the nodes
    nodes_list = []

    # check if node
    if not tree:
        return nodes_list

    # Create an empty stack
    stack = [tree]

    # Use while to loop until the stack is not empty

    while stack:
        # Pop the stack and assign the popped node as the current node
        current_node = stack.pop()

        nodes_list.append(current_node.content)

        # traverse the tree and append to stack
        if current_node.right:
            stack.append(current_node.right)

        if current_node.left:
            stack.append(current_node.left)

    # use list comprehension to remove the negative value from the nodes list
    nodes_list = [i for i in nodes_list if i > 0]

    # calculate the average
    avg = round(sum(nodes_list)/len(nodes_list), 4)

    return avg


node1 = Tree(-5)
node2 = Tree(-7)
node3 = Tree(3.55555)
node4 = Tree(4)
node5 = Tree(-9)
node6 = Tree(3)
node7 = Tree(-8)

# First Level
node1.right = node3
node1.left = node2

# Second level
node2.left = node4
node2.right = node5

# Third Level
node5.left = node6
node5.right = node7

print(averagePositive(node1))
# print(preorder_traversal(node1))
