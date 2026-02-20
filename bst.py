import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**9)

BinTree: TypeAlias = Union[None, 'BTNode']

@dataclass(frozen= True)
class BTNode:
    value: Any
    left: BinTree
    right: BinTree


@dataclass(frozen= True)
class BinarySearchTree:
    comes_before : Callable[[Any,Any], bool]
    bt : BinTree
    
# Returns whether or not a value exsists within a binary search tree
def lookup(bst: BinarySearchTree, value:Any)-> bool:
    cb = bst.comes_before
    def helper(bt: BinTree) -> bool:
        match bt:
            case None:
                return False
            case BTNode(v, left, right):
                if not cb(value, v) and not cb(v, value):
                    return True
                elif cb(value, v):  
                    return helper(left)
                else:                   
                    return helper(right)
    return helper(bst.bt)
        