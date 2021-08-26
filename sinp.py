class coloring:
    G = '\033[92m' #GREEN
    Y = '\033[93m' #YELLOW
    R = '\033[91m' #RED
    W = '\033[0m' #RESET COLOR / WHITE
    P = '\033[35m' # PURPLE

def inp(username="hirusha", projname="Project-Name123", ctx="~"):
    """Create a very nice console user input with Python

    Args:
        username (str, optional): The username, or the part of the project. Defaults to "hirusha".
        projname (str, optional): The projectname, or the Hardware ID. Defaults to "Project-Name123".
        ctx (str, optional): The path, what to enter. Defaults to "~".

    Returns:
        str: The result of the input() in its original form (String)
    """
    x = f"{coloring.G}┌──({coloring.P}{username}{coloring.Y}㉿{coloring.P}{projname}{coloring.G})-[{coloring.Y}{ctx}{coloring.G}]\n└─{coloring.R}${coloring.R}{coloring.W} "
    y = input(x)
    return y
