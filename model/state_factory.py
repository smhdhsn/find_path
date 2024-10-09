from model.state import State

def create_state_tree() -> State:
    """
    Creates the initial state tree.

    Returns:
        State: The root state of the tree.
    """
    state_d = State(value="d", next_states=None)
    state_e = State(value="e", next_states=None)
    state_f = State(value="f", next_states=None)

    state_b = State(value="b", next_states=[state_d, state_e])
    state_c = State(value="c", next_states=[state_f])

    state_a = State(value="a", next_states=[state_b, state_c])

    return state_a
