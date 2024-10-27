from storage.abstract import Storage
from model.state import State
from collections import deque
from typing import Deque

class Queue(Storage):
    """
    Queue-based storage mechanism for the frontier (FIFO).
    """

    def __init__(self, initial_state: State) -> None:
        """
        Initialize the queue storage with empty storage of type deque.

        Args:
            initial_state (State): Contains the initial state to explore.

        Raises:
            ValueError: If the provided state is not an instance of State.
        """
        if not isinstance(initial_state, State):
            raise ValueError("Initial state must be of type State")

        self.states: Deque[State] = deque([initial_state])

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

        return self.states.popleft()

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
