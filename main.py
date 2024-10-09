from model.state_factory import create_state_tree
from search.search import find_goal_state
from frontier.frontier import Frontier

goal="f"

def main():
    """
    Main function to initialize the state tree, perform goal search, and display the result.
    """
    initial_state = create_state_tree()
    frontier = Frontier(initial_state)

    result = find_goal_state(frontier, goal)

    if result is None:
        print("There is no solution")
    else:
        print(f"Found the solution {result.value}")

if __name__ == "__main__":
    main()
