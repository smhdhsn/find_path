"""
Entry point for the find_path application.
"""

from search.storage import Queue
from search import Frontier, find_goal_state
from problems import create_state_tree
from inputs import read_stdin

def main():
    """
    Main function to initialize the state tree, perform goal search, and display the result.
    """

    initial_state = create_state_tree()

    storage = Queue(initial_state)

    frontier = Frontier(storage)

    goal = read_stdin("Enter a goal: ")

    result = find_goal_state(frontier, goal)

    if result is not None:
        print(
            "Found the solution!",
            f"Path: {result.get_path()}",
            f"Cost: {result.get_path_cost()}",
            f"Explored: {len(frontier.explored_states)}",
            sep="\n",
        )
    else:
        print("There is no solution.")

if __name__ == "__main__":
    main()
