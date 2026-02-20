import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**9)
from bst import *

@dataclass(frozen=True)
class Point2D:
    x: int
    y: int

def chr_before(a: str, b: str) -> bool:
    return a < b

def point_before(p1: Point2D, p2: Point2D) -> bool:
    d1 = p1.x**2 + p1.y**2
    d2 = p2.x**2 + p2.y**2
    return d1 < d2

def reverse_before(a: Any, b: Any) -> bool:
    return a > b

class BSTTests(unittest.TestCase):
    bst_1 = BinarySearchTree(
            chr_before,
            BTNode('b',
                   BTNode('a', None, None),
                   BTNode('c', None, None))
        )
    bst_2: BinarySearchTree = BinarySearchTree(
            reverse_before,
            BTNode(9,
                   BTNode(10, None, None),
                   BTNode(8, None, None))
        )
    p1 = Point2D(2,2)
    p2 = Point2D(1,1)
    p3 = Point2D(3, 3)  

    bst_3 = BinarySearchTree(
        point_before,
        BTNode(p2,
               BTNode(p1, None, None),
               BTNode(p3, None, None))
        )

    def test_lookup(self):
        self.assertEqual(lookup(self.bst_3, Point2D(5, 5)), False)
        self.assertEqual(lookup(self.bst_1, 'b'), True)
        self.assertEqual(lookup(self.bst_2, 8), True)




if (__name__ == '__main__'):
    unittest.main()