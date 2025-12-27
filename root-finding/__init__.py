"""
Root finding numerical methods : This package contains 
implementations of standard root-finding algorithms used 
in physical and astrophysical problems.
"""


from .bisection import bisection
from .newton_raphson import newton_raphson

__all__ = ["bisection", "newton_raphson"]
