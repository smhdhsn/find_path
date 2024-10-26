from model.state import State
from typing import Set

class Frontier:
    """
    A container for managing states and exploration of states.
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

        self.explored_states: Set[State] = set()
        self.states: Set[State] = {initial_states}

    def pop(self) -> State:
        """
        Removes a state from the frontier, adds it to explored states and returns the state.

        Returns:
            State: The last state in the frontier.

        Raises:
            IndexError: If the frontier is empty when attempting to pop.
        """
        if self.is_empty():
            raise IndexError("Cannot pop from an empty frontier")

        state = self.states.pop()
        self.explored_states.add(state)
        return state

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

        if state not in self:
            self.states.add(state)

    def is_empty(self) -> bool:
        """
        Check if the frontier is empty.

        Returns:
            bool: True if the frontier is empty, False otherwise.
        """
        return not self.states

    def __contains__(self, state: State) -> bool:
        """
        Check if a state is either in the frontier or has been explored.

        Args:
            state (State): The state to check.

        Returns:
            bool: True if the state is in the frontier or explored states, False otherwise.
        """
        return state in self.explored_states or state in self.states
