"""
Package for search algorithms and related classes in the find_path application.
"""

from .algorithm import find_goal_state
from .frontier import Frontier

# Expose methods at the package level.
__all__ = [
    'find_goal_state',
    'Frontier'
]
