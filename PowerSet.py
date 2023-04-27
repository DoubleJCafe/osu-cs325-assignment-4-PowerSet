# Name: Joshua Jansen
# OSU Email: Jansejos@oregonstate.edu
# Course: CS325
# Assignment: 4

def powerset(inputSet):
    """
    Finds the power set of a given array.
    :param inputSet: Array of integers
    :return: Array with the power set of the given array.
    """
    if not inputSet:
        return [[]]
    results = powerset_helper(len(inputSet) - 1, [], inputSet, [])
    return results


def powerset_helper(pointer, choices_made, inputSet, result):
    """
    Helper function for powerset() which uses recursion to find the power set.
    :param pointer: Pointer for what element is being added to choices_made.
    :param choices_made: Current inputSet of the recursion stack.
    :param inputSet: The initial array.
    :param result: Array that holds the solution each choices_made param makes
    once the pointer reaches less than 0.
    :return: Array with the power set of the given array.
    """
    if pointer < 0:
        return result.append(choices_made[::-1])

    choices_made.append(inputSet[pointer])
    powerset_helper(pointer - 1, choices_made, inputSet, result)
    choices_made.pop()
    powerset_helper(pointer - 1, choices_made, inputSet, result)
    return result
