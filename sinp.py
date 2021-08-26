class coloring:
    G = '\033[92m' #GREEN
    Y = '\033[93m' #YELLOW
    R = '\033[91m' #RED
    W = '\033[0m' #RESET COLOR / WHITE
    P = '\033[35m' # PURPLE

def inp(username="hirusha", projname="Project-Name123", ctx="~"):
    x = f"{coloring.G}┌──({coloring.P}{username}{coloring.Y}㉿{coloring.P}{projname}{coloring.G})-[{coloring.Y}{ctx}{coloring.G}]\n└─{coloring.R}${coloring.R}{coloring.W} "
    y = input(x)
    return y

inp()
