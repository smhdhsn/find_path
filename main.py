from frontier.frontier import Frontier
from storage.queue import Queue

from factory.state import create_state_tree
from search.search import find_goal_state
from input.stdin import read_stdin

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
        print(f"Found the solution!\nThe path to solution: ({result.get_path()})")
    else:
        print("There is no solution.")

if __name__ == "__main__":
    main()
