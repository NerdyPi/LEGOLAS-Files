"""
General process of LEGOLAS operation

Experiment creation --> Measurement --> Analysis --> New experiment

This process will be handled by the student in two parts

Part 1) LEGOLAS experiment dispatch
# This segment is defined in the function "experiment"
# the function accepts a "LegolasUnit", which is a representation
# of a physical LEGOLAS kit.
#
# This function will be run in parallel for every connected LEGOLAS unit.
# The function should handle logic for performing experiments
# supplied by the optimization process, and should be able to 
# pass results to a shared python object for later use

Part 2) 
# This segment is defined in the function "analysis"
# the function has no parameters, but should be able to
# access the data in whatever way the student deems fit, and
# perform an optimization routine. 
#
# Once the next experiments are calculated, the function
# should be able to supply the 'experiment' functions
# with a new list of needed experiments

Ultimately, the code structure should contain:
- 'experiment' definition
- 'analysis' definition
- shared 'results'
- shared 'experiments'

The groupManager object is then used to run the experiments in parallel

See below for an example
"""

from groupManager import GroupManager, LegolasUnit

"""
Local variables can be used by students to store information

Usage:
Students should implement a way to store experiments that LEGOLAS units
should perform (ex. a task queue)

Students should store data acquired from these experiments for
analysis, which will then generate new experiments to perform
"""
data = [] # Example for a list of results
tasks = [] # Example for a list of tasks

# The specific implementation of these systems can be largely
# up to the student


# Part 1 'experiment' function definition
def experiment(unit: LegolasUnit): 
    # From the 'unit' variable passed in, the student can call
    # LEGOLAS functionality

    # ex.
    # unit.stage.move_to_cell(row=0,col=0) # Move the stage to pos (0,0)

    pass

def analysis():
    # Perform an optimization process

    pass

demoGroup = GroupManager("config/conf6.yaml") # example config location

# Passing in relevant functions
demoGroup.executeAnalysis(analysis)
demoGroup.executeExperiment(experiment)

# User is free to define end conditions and plot results
while input() != "q":
    pass