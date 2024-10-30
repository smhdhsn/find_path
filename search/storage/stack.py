"""
Stack storage implementation for search algorithms in the find_path application.
"""

from typing import List
from models import State
from .abstract import Storage

class Stack(Storage):
    """
    Stack-based storage mechanism for the frontier (LIFO).
    """

    def __init__(self, initial_state: State) -> None:
        """
        Initialize the stack storage with empty storage of type list.

        Args:
            initial_state (State): Contains the initial state to explore.

        Raises:
            ValueError: If the provided state is not an instance of State.
        """
        if not isinstance(initial_state, State):
            raise ValueError("Initial state must be of type State")

        self.states: List[State] = [initial_state]

    def push(self, state: State) -> None:
        """
        Add a state to the storage.

        Args:
            state (State): The state to add.
        """
        self.states.append(state)

    def remove(self) -> State:
        """
        Remove and return a state from the storage.

        Returns:
            State: The next state in the storage.

        Raises:
            IndexError: If the storage is empty when attempting to remove.
        """
        if self.empty():
            raise IndexError("Cannot remove from empty storage")

        return self.states.pop()

    def empty(self) -> bool:
        """
        Check if the storage is empty.

        Returns:
            bool: True if the storage is empty, False otherwise.
        """
        return not self.states

    def __contains__(self, state: State) -> bool:
        """
        Check if a state is in the storage.

        Args:
            state (State): The state to check.

        Returns:
            bool: True if the state is in the storage, False otherwise.
        """
        return state in self.states
