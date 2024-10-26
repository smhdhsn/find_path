from abc import ABC, abstractmethod
from model.state import State

class Storage(ABC):
    """
    Abstract base class for storage mechanisms in the frontier.
    """

    @abstractmethod
    def push(self, state: State) -> None:
        """
        Add a state to the storage.

        Args:
            state (State): The state to add.
        """
        pass

    @abstractmethod
    def remove(self) -> State:
        """
        Remove and return a state from the storage.

        Returns:
            State: The next state in the storage.

        Raises:
            IndexError: If the storage is empty when attempting to remove.
        """
        pass

    @abstractmethod
    def empty(self) -> bool:
        """
        Check if the storage is empty.

        Returns:
            bool: True if the storage is empty, False otherwise.
        """
        pass

    @abstractmethod
    def __contains__(self, state: State) -> bool:
        """
        Check if a state is in the storage.

        Args:
            state (State): The state to check.

        Returns:
            bool: True if the state is in the storage, False otherwise.
        """
        pass
