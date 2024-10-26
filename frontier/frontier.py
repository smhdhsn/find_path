from storage.storage import Storage
from model.state import State
from typing import Set

class Frontier:
    """
    A container for managing states and exploration of states.
    """

    def __init__(self, storage: Storage) -> None:
        """
        Initialize the Frontier with an initial state.

        Args:
            storage (Storage): The storage mechanism to use (e.g., StackStorage or QueueStorage).

        Raises:
            ValueError: If the provided storage is not an instance of Storage.
        """
        if not isinstance(storage, Storage):
            raise ValueError("Input storage must be of type Storage")

        self.explored_states: Set[State] = set()
        self.storage: Storage = storage

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
            self.storage.push(state)

    def not_empty(self) -> bool:
        """
        Check if the frontier is empty.

        Returns:
            bool: True if the frontier is empty, False otherwise.
        """
        return not self.storage.empty()

    def remove(self) -> State:
        """
        Removes a state from the frontier, adds it to explored states and returns the state.

        Returns:
            State: The last state in the frontier.

        Raises:
            IndexError: If the frontier is empty when attempting to remove.
        """
        state = self.storage.remove()
        self.explored_states.add(state)
        return state

    def __contains__(self, state: State) -> bool:
        """
        Check if a state is either in the frontier or has been explored.

        Args:
            state (State): The state to check.

        Returns:
            bool: True if the state is in the frontier or explored states, False otherwise.
        """
        return state in self.explored_states or state in self.storage
