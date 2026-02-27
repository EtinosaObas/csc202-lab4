import sys
import unittest
from typing import *
from dataclasses import dataclass
import math
import matplotlib.pyplot as plt
import numpy as np
import random
import time
sys.setrecursionlimit(10**9)
from bst import *

TREES_PER_RUN : int = 10000

# Returns a BinarySearchTree with 'n' random floats between 0 and 1
def random_tree(n: int) -> BinarySearchTree:
    bt = None
    def float_before(a: float, b: float)-> bool:
        return a < b

    def helper(bt: BinTree, val: float):
        match bt:
            case None:
                return BTNode(val, None, None)
            case BTNode(v, l , r):
                if not float_before(val, v) and not float_before(v, val):
                    return bt
                elif float_before(val, v):
                    return BTNode(v, helper(l, val), r )
                else:
                    return BTNode(v, l, helper(r, val))
    
    for _ in range(n):
        bt = helper(bt, random.random())
    
    return BinarySearchTree(float_before, bt)

# Returns the height of a BST
def height(bst: BinarySearchTree)-> int:
    bt = bst.bt
    def helper(bt: BinTree)-> int:
        match bt:
            case None:
                return 0
            case BTNode(_, l, r):
                return 1 + max(helper(l), helper(r))   
    return helper(bt)

# Graphs the average height of a random tree
def random_tree_graph() -> None:
   
    def avg_rand(n:float) -> float:
        count = 0
        for _ in range(TREES_PER_RUN):
            tree = random_tree(n)
            h = height(tree)
            count += h
        return count/TREES_PER_RUN
    
    n_max_rand = 70    
    step = (n_max_rand - 1) / 49
    x_coords : List[float] = [int(round(1 + i * step)) for i in range(50) ]
    y_coords : List[float] = [ avg_rand(x) for x in x_coords ]

    x_numpy : np.ndarray = np.array( x_coords )
    y_numpy : np.ndarray = np.array( y_coords )

    plt.plot( x_numpy, y_numpy, label = 'Height of Random Tree as Function of N' )
    plt.xlabel("Number of Values (N)")
    plt.ylabel("Avg. Height of TREES_PER_RUN Trees")
    plt.title("Height of Random Tree")
    plt.grid(True)
    plt.legend() 
    plt.show()

# Graphs the time complexity of insert()
def insert_graph_creation() -> None:
    def avg_insert(n:float) -> float:
        total = 0.0
        for _ in range(TREES_PER_RUN):
            tree = random_tree(n)  

            start = time.perf_counter()
            _ = insert(tree, 0.001)  
            end = time.perf_counter()

            total += (end - start)
        return total / TREES_PER_RUN 
    
    n_max_insert = 150
    step = (n_max_insert - 1) / 49
    x_coords : List[float] = [int(round(1 + i * step)) for i in range(50) ]
    y_coords : List[float] = [ avg_insert(x) for x in x_coords ]

    x_numpy : np.ndarray = np.array( x_coords )
    y_numpy : np.ndarray = np.array( y_coords )
    plt.plot( x_numpy, y_numpy, label = 'Insert Time as Function of N' )
    plt.xlabel("Number of Values (N)")
    plt.ylabel("Avg. Time to insert Value Into Random Tree")
    plt.title("Insert Time Complexity")
    plt.grid(True)
    plt.legend() 
    plt.show()


if (__name__ == '__main__'):
    random_tree_graph()
    insert_graph_creation()