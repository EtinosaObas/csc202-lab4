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
    def tree_to_tuple(self, tree: BinTree) -> Any:
        match tree:
            case None:
                return None
            case BTNode(v, left, right):
                return (v, self.tree_to_tuple(left), self.tree_to_tuple(right))

    def test_lookup(self):
        bst_1 = BinarySearchTree(
            chr_before,
            BTNode('b', BTNode('a', None, None), BTNode('c', None, None)),
        )
        bst_2 = BinarySearchTree(
            reverse_before,
            BTNode(9, BTNode(10, None, None), BTNode(8, None, None)),
        )
        p1 = Point2D(2, 2)
        p2 = Point2D(1, 1)
        p3 = Point2D(3, 3)
        bst_3 = BinarySearchTree(point_before, BTNode(p2, BTNode(p1, None, None), BTNode(p3, None, None)))

        self.assertFalse(lookup(bst_3, Point2D(5, 5)))
        self.assertTrue(lookup(bst_1, 'b'))
        self.assertTrue(lookup(bst_2, 8))

    def test_insert_into_empty_tree(self):
        bst = BinarySearchTree(lambda a, b: a < b, None)
        result = insert(bst, 10)
        self.assertEqual(self.tree_to_tuple(result.bt), (10, None, None))

    def test_insert_duplicate_does_not_change_tree(self):
        bst = BinarySearchTree(lambda a, b: a < b, BTNode(10, BTNode(5, None, None), BTNode(15, None, None)))
        result = insert(bst, 10)
        self.assertEqual(self.tree_to_tuple(result.bt), self.tree_to_tuple(bst.bt))

    def test_delete_leaf_node(self):
        bst = BinarySearchTree(lambda a, b: a < b, BTNode(10, BTNode(5, None, None), BTNode(15, None, None)))
        result = delete(bst, 5)
        self.assertEqual(self.tree_to_tuple(result.bt), (10, None, (15, None, None)))

    def test_delete_node_with_one_child(self):
        bst = BinarySearchTree(
            lambda a, b: a < b,
            BTNode(10, BTNode(5, None, BTNode(7, None, None)), BTNode(15, None, None)),
        )
        result = delete(bst, 5)
        self.assertEqual(self.tree_to_tuple(result.bt), (10, (7, None, None), (15, None, None)))

    def test_delete_node_with_two_children(self):
        bst = BinarySearchTree(
            lambda a, b: a < b,
            BTNode(
                10,
                BTNode(5, None, None),
                BTNode(15, BTNode(12, None, None), BTNode(20, None, None)),
            ),
        )
        result = delete(bst, 10)
        self.assertEqual(
            self.tree_to_tuple(result.bt),
            (12, (5, None, None), (15, None, (20, None, None))),
        )

    def test_delete_missing_value_keeps_tree(self):
        bst = BinarySearchTree(lambda a, b: a < b, BTNode(10, BTNode(5, None, None), BTNode(15, None, None)))
        result = delete(bst, 999)
        self.assertEqual(self.tree_to_tuple(result.bt), self.tree_to_tuple(bst.bt))


if __name__ == '__main__':
    unittest.main()
