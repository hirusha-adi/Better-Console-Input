# Make sure to have the sinp.py in the project folder before doing this import
from sinp import inp

# This is how to use it
query = inp("root", "project-name", "~")
print(query)

# Passing with keyword arguments
querykwarg = inp(username="root", projname="project-name", ctx="~")
print(querykwarg)



