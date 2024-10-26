from model.state import State
from typing import List, Set

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
        self.states: List[State] = [initial_states]

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
            self.states.append(state)

    def empty(self) -> bool:
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

class StackFrontier(Frontier):
    """
    Handles exploration of the frontier in a FILO way like a stack.
    """

    def remove(self) -> State:
        """
        Removes a state from the frontier, adds it to explored states and returns the state.

        Returns:
            State: The last state in the frontier.

        Raises:
            IndexError: If the frontier is empty when attempting to remove.
        """
        if self.empty():
            raise IndexError("Cannot remove from an empty frontier")

        state = self.states[-1]
        self.states = self.states[:-1]
        self.explored_states.add(state)

        return state

class QueueFrontier(Frontier):
    """
    Handles exploration of the frontier in a FIFO way like a queue.
    """

    def remove(self) -> State:
        """
        Removes a state from the frontier, adds it to explored states and returns the state.

        Returns:
            State: The last state in the frontier.

        Raises:
            IndexError: If the frontier is empty when attempting to remove.
        """
        if self.empty():
            raise IndexError("Cannot remove from an empty frontier")

        state = self.states[0]
        self.states = self.states[1:]
        self.explored_states.add(state)

        return state
