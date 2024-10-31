"""
Module to create a sample tree for the find_path application.
"""

from models import State

def create_state_tree() -> State:
    """
    Creates the initial state tree.

    Returns:
        State: The root state of the tree.
    """

    # First level.
    state_a = State("a")

    # Second level.
    state_b = State("b")
    state_c = State("c")

    # Third level.
    state_d = State("d")
    state_e = State("e")
    state_f = State("f")
    state_g = State("g")

    # Forth level.
    state_h = State("h")
    state_i = State("i")
    state_j = State("j")
    state_k = State("k")
    state_l = State("l")
    state_m = State("m")
    state_n = State("n")
    state_o = State("o")

    # Define links.
    state_a.set_next(state_b, state_c)
    state_b.set_next(state_d, state_e)
    state_c.set_next(state_f, state_g)
    state_d.set_next(state_h, state_i)
    state_e.set_next(state_j, state_k)
    state_f.set_next(state_l, state_m)
    state_g.set_next(state_n, state_o)

    state_b.set_parent(state_a)
    state_c.set_parent(state_a)
    state_d.set_parent(state_b)
    state_e.set_parent(state_b)
    state_f.set_parent(state_c)
    state_g.set_parent(state_c)
    state_h.set_parent(state_d)
    state_i.set_parent(state_d)
    state_j.set_parent(state_e)
    state_k.set_parent(state_e)
    state_l.set_parent(state_f)
    state_m.set_parent(state_f)
    state_n.set_parent(state_g)
    state_o.set_parent(state_g)

    return state_a
