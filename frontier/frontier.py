from model.state import State
from typing import List

class Frontier:
    """
    A container for states waiting to be explored.
    """

    def __init__(self, initial_states: State) -> None:
        """
        Initialize the Frontier with an initial state.

        Args:
            initial_states (State): Initial state object.

        Raises:
            ValueError: If the provided state is not an instance of State.
        """
        if not isinstance(initial_states, State):
            raise ValueError("Initial state must be of type State")

        self.states: List[State] = [initial_states]

    def pop(self) -> State:
        """
        Remove and return the last state from the frontier.

        Returns:
            State: The last state in the frontier.

        Raises:
            IndexError: If the frontier is empty when attempting to pop.
        """
        if self.is_empty():
            raise IndexError("Cannot pop from an empty frontier")

        return self.states.pop()

    def push(self, state: State) -> None:
        """
        Add a state to the frontier.

        Args:
            state (State): The state to add.

        Raises:
            ValueError: If the provided state is not an instance of State.
        """
        if not isinstance(state, State):
            raise ValueError("State must be of type State")

        self.states.append(state)

    def is_empty(self) -> bool:
        """
        Check if the frontier is empty.

        Returns:
            bool: True if the frontier is empty, False otherwise.
        """
        return len(self.states) == 0
