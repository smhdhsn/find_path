from frontier.frontier import Frontier
from model.state import State
from typing import Optional

def find_goal_state(frontier: Frontier, goal: str) -> Optional[State]:
    """
    Searches for the goal state using the provided frontier.

    Args:
        frontier (Frontier): The frontier to manage the search nodes.
        goal (str): The value of the goal state to find.

    Returns:
        Optional[State]: The goal state if found, else None.
    """
    while not frontier.empty():
        node = frontier.remove()

        print(f"Node <{node.value}> has been removed from the frontier.")

        if node.is_goal(goal):
            return node

        if not node.is_leaf():
            next_nodes = node.get_next()

            for node in next_nodes:
                frontier.push(node)
