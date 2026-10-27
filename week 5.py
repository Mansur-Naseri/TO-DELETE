"""
list_tasks.py

Stores a list of basic instructions for navigating through a maze.
"""


def directions():
    """
    Create and return a list of maze navigation instructions.

    Returns:
        list: The list named steps containing the four basic directions.
    """
    # Create an empty list to hold the instructions
    steps = []

    # Populate the list with each navigation instruction
    steps.append("Move Forward")
    steps.append("Move Backward")
    steps.append("Turn Left")
    steps.append("Turn Right")

    # Return the completed list to the caller
    return steps


def run_task1():
    """
    Call the directions function and display the list it returns.
    """
    # Get the list of steps from the directions function
    steps = directions()

    # Display the list
    print(steps)


# Only run run_task1 when this file is executed directly,
# not when it is imported into another module
if __name__ == "__main__":
    run_task1()