# -*- coding: utf-8 -*-
"""
This is the unittest for pentapy.
"""
from __future__ import division, absolute_import, print_function

import unittest
import numpy as np
import pentapy as pp
from pentapy.py_solver import penta_solver1 as ps1
from pentapy.py_solver import penta_solver2 as ps2

class TestPentapy(unittest.TestCase):
    def setUp(self):
        self.seed = 19031977
        self.size = 1000
        self.rand = np.random.RandomState(self.seed)
        self.mat = (self.rand.rand(5, self.size) - 0.5) * 1e-5
        self.rhs = self.rand.rand(self.size) * 1e5

    def test_solve1(self):
        self.mat_col = pp.shift_banded(self.mat, col_to_row=False)
        self.mat_ful = pp.create_full(self.mat, col_wise=False)

        sol_row = pp.solve(self.mat, self.rhs, is_flat=True, solver=1)
        sol_col = pp.solve(
            self.mat_col,
            self.rhs,
            is_flat=True,
            index_row_wise=False,
            solver=1,
        )
        sol_ful = pp.solve(self.mat_ful, self.rhs, solver=1)
        sol_pyt = ps1(self.mat, self.rhs)

        diff_row = np.max(np.abs(np.dot(self.mat_ful, sol_row) - self.rhs))
        diff_col = np.max(np.abs(np.dot(self.mat_ful, sol_col) - self.rhs))
        diff_ful = np.max(np.abs(np.dot(self.mat_ful, sol_ful) - self.rhs))
        diff_pyt = np.max(np.abs(np.dot(self.mat_ful, sol_pyt) - self.rhs))

        diff_row_col = np.max(
            np.abs(self.mat_ful - pp.create_full(self.mat_col))
        )
        self.assertAlmostEqual(diff_row * 1e-5, 0.0)
        self.assertAlmostEqual(diff_col * 1e-5, 0.0)
        self.assertAlmostEqual(diff_ful * 1e-5, 0.0)
        self.assertAlmostEqual(diff_pyt * 1e-5, 0.0)
        self.assertAlmostEqual(diff_row_col * 1e5, 0.0)

    def test_solve2(self):
        self.mat_col = pp.shift_banded(self.mat, col_to_row=False)
        self.mat_ful = pp.create_full(self.mat, col_wise=False)

        sol_row = pp.solve(self.mat, self.rhs, is_flat=True, solver=2)
        sol_col = pp.solve(
            self.mat_col,
            self.rhs,
            is_flat=True,
            index_row_wise=False,
            solver=2,
        )
        sol_ful = pp.solve(self.mat_ful, self.rhs, solver=2)
        sol_pyt = ps2(self.mat, self.rhs)

        diff_row = np.max(np.abs(np.dot(self.mat_ful, sol_row) - self.rhs))
        diff_col = np.max(np.abs(np.dot(self.mat_ful, sol_col) - self.rhs))
        diff_ful = np.max(np.abs(np.dot(self.mat_ful, sol_ful) - self.rhs))
        diff_pyt = np.max(np.abs(np.dot(self.mat_ful, sol_pyt) - self.rhs))

        diff_row_col = np.max(
            np.abs(self.mat_ful - pp.create_full(self.mat_col))
        )
        self.assertAlmostEqual(diff_row * 1e-5, 0.0)
        self.assertAlmostEqual(diff_col * 1e-5, 0.0)
        self.assertAlmostEqual(diff_ful * 1e-5, 0.0)
        self.assertAlmostEqual(diff_pyt * 1e-5, 0.0)
        self.assertAlmostEqual(diff_row_col * 1e5, 0.0)


if __name__ == "__main__":
    unittest.main()
