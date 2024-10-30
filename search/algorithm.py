"""
Contains search algorithm implementations for the find_path application.
"""
from typing import Optional
from search.frontier import Frontier
from models import State

def find_goal_state(frontier: Frontier, goal: str) -> Optional[State]:
    """
    Searches for the goal state using the provided frontier.

    Args:
        frontier (Frontier): The frontier to manage the search nodes.
        goal (str): The value of the goal state to find.

    Returns:
        Optional[State]: The goal state if found, else None.
    """
    while frontier.not_empty():
        node = frontier.remove()

        if node.is_goal(goal):
            return node

        if not node.is_leaf():
            next_nodes = node.get_next()

            for node in next_nodes:
                frontier.push(node)

    return None
