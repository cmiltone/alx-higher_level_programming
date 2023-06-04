#!/usr/bin/python3
"""
This is a simple module to multiply matrices using numpy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    return np.matmul(m_a, m_b)
