from __future__ import annotations
from typing import List

class State:
    """
    A representation of a state in the search space.
    """

    def __init__(self, value: str) -> None:
        """
        Initialize the State with next states.

        Args:
            value (str): Value inside the current state.

        Raises:
            ValueError: If the value is not provided or is an empty string.
        """
        if value is None or value == "":
            raise ValueError("Value must be provided")

        self.parent_state: State = None
        self.next_states: List = []
        self.value: str = value

    def set_next(self, *next_states: State) -> None:
        """
        Responsible for setting the next states to this state.

        Args:
            next_states (List[State]): Next states of this state.

        Raises:
            ValueError: If the provided list of states is not a list of instances of State.
        """
        if not all(isinstance(state, State) for state in next_states):
            raise ValueError("Next states must be of type State")

        self.next_states = next_states

    def set_parent(self, parent_state: State) -> None:
        """
        Sets the parent state of this state.

        Args:
            next_states (State): Parent state of the current state.

        Raises:
            ValueError: If the provided state is not a list of instance of State.
        """
        if not isinstance(parent_state, State):
            raise ValueError("Parent state must be of type State")

        self.parent_state = parent_state

    def get_next(self) -> List[State]:
        """
        Get the next states.

        Returns:
            List[State]: The next states.

        Raises:
            ValueError: If no next states are available.
        """
        if self.next_states is None:
            raise ValueError("No next states available")

        return self.next_states

    def is_leaf(self) -> bool:
        """
        Check if the state is a leaf node.

        Returns:
            bool: True if the state is a leaf node, False otherwise.
        """
        return len(self.next_states) == 0

    def is_goal(self, goal: str) -> bool:
        """
        Check if the state is a goal state.

        Returns:
            bool: True if the state is a goal state, False otherwise.
        """
        return self.value == goal

    def get_path(self) -> str:
        """
        Returns the path from root state to this state.

        Returns:
            str: The path from root state to this state.
        """
        state: State = self
        path: str = self.value

        while True:
            state = state.parent_state

            if state is None:
                return path

            path = f"{state.value} ->> {path}"
