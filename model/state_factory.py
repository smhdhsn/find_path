from model.state import State

def create_state_tree() -> State:
    """
    Creates the initial state tree.

    Returns:
        State: The root state of the tree.
    """
    state_p = State(value="p", next_states=None)
    state_q = State(value="q", next_states=None)
    state_r = State(value="r", next_states=None)
    state_s = State(value="s", next_states=None)
    state_t = State(value="t", next_states=None)
    state_u = State(value="u", next_states=None)
    state_v = State(value="v", next_states=None)
    state_w = State(value="w", next_states=None)
    state_x = State(value="x", next_states=None)
    state_y = State(value="y", next_states=None)
    state_z = State(value="z", next_states=None)

    state_h = State(value="h", next_states=[state_p, state_q])
    state_i = State(value="i", next_states=[state_r, state_s])
    state_j = State(value="j", next_states=[state_t, state_u])
    state_k = State(value="k", next_states=[state_v, state_w])
    state_l = State(value="l", next_states=[state_x, state_y])
    state_m = State(value="m", next_states=[state_z])
    state_n = State(value="n", next_states=None)
    state_o = State(value="o", next_states=None)

    state_d = State(value="d", next_states=[state_h, state_i])
    state_e = State(value="e", next_states=[state_j, state_k])
    state_f = State(value="f", next_states=[state_l, state_m])
    state_g = State(value="g", next_states=[state_n, state_o])

    state_b = State(value="b", next_states=[state_d, state_e])
    state_c = State(value="c", next_states=[state_f, state_g])

    state_a = State(value="a", next_states=[state_b, state_c])

    return state_a
