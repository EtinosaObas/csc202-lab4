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

# Helper for insert
def insert_helper(comes_before: Callable[[Any, Any], bool], tree: BinTree, value: Any) -> BinTree:
    match tree:
        case None:
            return BTNode(value, None, None)
        case BTNode(v, left, right):
            if comes_before(value, v):
                return BTNode(v, insert_helper(comes_before, left, value), right)
            elif comes_before(v, value):
                return BTNode(v, left, insert_helper(comes_before, right, value))
            else:
                return tree

def insert(bst: BinarySearchTree, value: Any) -> BinarySearchTree:
    return BinarySearchTree(bst.comes_before, insert_helper(bst.comes_before, bst.bt, value))

# Helper to find min
def find_min(tree: BinTree) -> Any:
    match tree:
        case BTNode(v, None, _):
            return v
        case BTNode(_, left, _):
            return find_min(left)

# Helper for delete
def delete_helper(comes_before: Callable[[Any, Any], bool], tree: BinTree, value: Any) -> BinTree:
    match tree:
        case None:
            return None
        case BTNode(v, left, right):
            if comes_before(value, v):
                return BTNode(v, delete_helper(comes_before, left, value), right)
            elif comes_before(v, value):
                return BTNode(v, left, delete_helper(comes_before, right, value))
            else:
                if left is None:
                    return right
                elif right is None:
                    return left
                else:
                    min_val = find_min(right)
                    return BTNode(min_val, left, delete_helper(comes_before, right, min_val))

def delete(bst: BinarySearchTree, value: Any) -> BinarySearchTree:
    return BinarySearchTree(bst.comes_before, delete_helper(bst.comes_before, bst.bt, value))
        