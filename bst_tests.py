import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**9)
from bst import *


class BSTTests(unittest.TestCase):
    bst_1 = BinarySearchTree(
            comes_before,
            BTNode(2,
                   BTNode(1, None, None),
                   BTNode(3, None, None))
        )
    #bst_2: BinarySearchTree =

    def test_lookup(self):
        self.assertEqual(lookup(self.bst_1, 4), False)



if (__name__ == '__main__'):
    unittest.main()