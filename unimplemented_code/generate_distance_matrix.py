from random import randint


def gen_dist_matrix(length: int, min_value: int, max_value: int,
                    asym: bool = False, asym_max: int = 1):
    """
        Generate random distance matrices based on user inputs in order to test Vehicle Routing Solver.
        This allows us to bypass the need for the (expensive) Distance Matrix API.

    :param length: number of distance matrix nodes
    :param min_value: minimum potential distance between nodes
    :param max_value: maximum potential distance between nodes
    :param asym: kwarg to indicate if reverse route is asymmetrical. (i.e. a -> b has a different length than b -> a).
        Set to False by default
    :param asym_max: kwarg to set maximum potential difference if routes between nodes are asymmetrical.
        Set to 1 by default.
    """
    pass
