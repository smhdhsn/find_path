from __future__ import annotations
from typing import Optional, List

class State:
    """
    A representation of a state in the search space.
    """

    def __init__(self, next_states: Optional[List[State]]) -> None:
        """
        Initialize the State with next states.

        Args:
            next_states (Optional[List[State]]): Next states to be explored.

        Raises:
            ValueError: If the provided list of states is presented and is not a list of instances of State.
        """
        if next_states is not None and not all(isinstance(state, State) for state in next_states):
            raise ValueError("Next states must be of type State")

        self.next_states: List[State] = next_states

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
        return self.next_states is None or len(self.next_states) == 0

    def is_goal(self) -> bool:
        """
        Check if the state is a goal state.

        Returns:
            bool: True if the state is a goal state, False otherwise.
        """
        pass
