from model.state import State

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

    # Fifth level.
    state_p = State("p")
    state_q = State("q")
    state_r = State("r")
    state_s = State("s")
    state_t = State("t")
    state_u = State("u")
    state_v = State("v")
    state_w = State("w")
    state_x = State("x")
    state_y = State("y")
    state_z = State("z")

    # Define links.
    state_a.set_next(state_b, state_c)
    state_b.set_next(state_d, state_e)
    state_c.set_next(state_f, state_g)
    state_d.set_next(state_h, state_i)
    state_e.set_next(state_j, state_k)
    state_f.set_next(state_l, state_m)
    state_g.set_next(state_n, state_o)
    state_h.set_next(state_p, state_q)
    state_i.set_next(state_r, state_s)
    state_j.set_next(state_t, state_u)
    state_k.set_next(state_v, state_w)
    state_l.set_next(state_x, state_y)
    state_m.set_next(state_z)
    
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
    state_p.set_parent(state_h)
    state_q.set_parent(state_h)
    state_r.set_parent(state_i)
    state_s.set_parent(state_i)
    state_t.set_parent(state_j)
    state_u.set_parent(state_j)
    state_v.set_parent(state_k)
    state_w.set_parent(state_j)
    state_x.set_parent(state_l)
    state_y.set_parent(state_l)
    state_z.set_parent(state_m)

    return state_a
