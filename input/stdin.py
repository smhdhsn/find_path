def read_stdin(msg: str) -> str:
    """
    Responsible for reading an input from /dev/stdin.

    Returns:
        str: The input from stdin.
    """
    inp = input(msg)

    return str(inp)