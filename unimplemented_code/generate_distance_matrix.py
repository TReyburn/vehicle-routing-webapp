from random import randint


def gen_dist_matrix(m_length: int, min_value: int, max_value: int,
                    asym: bool = False, asym_max: int = 1) -> list:
    """
        Generate random distance matrices based on user inputs in order to test Vehicle Routing Solver.
        This allows us to bypass the need for the (expensive) Distance Matrix API.

    :param m_length: number of distance matrix nodes
    :param min_value: minimum potential distance between nodes
    :param max_value: maximum potential distance between nodes
    :param asym: kwarg to indicate if reverse route is asymmetrical. (i.e. a -> b has a different length than b -> a).
        Set to False by default
    :param asym_max: kwarg to set maximum potential difference if routes between nodes are asymmetrical.
        Set to 1 by default.
    """

    # Quick unit test of user inputs
    for key, value in {'m_length': m_length, 'min_value': min_value,
                       'max_value': max_value, 'asym_max': asym_max}.items():
        if type(value) is not int:
            raise TypeError(f'{key} is not an integer.')
        if value <= 0:
            raise ValueError(f'{key} must be greater than 0.')
        if key == 'm_length' and value == 1:
            raise ValueError(f'{key} must be greater than 1.')
    if type(asym) is not bool:
        raise TypeError(f'{asym} is not a boolean.')
    if min_value >= max_value:
        raise ValueError('Min Value must be less than Max Value')

    dist_matrix = []

    # orig_node will represent each origin node position
    for orig_node in range(m_length):
        node_dist_list = []
        # dest_node represents the destination node position
        for dest_node in range(m_length):
            # If the destination node is the origin node then distance to itself is 0
            if dest_node == orig_node:
                node_dist_list.append(0)
            # If node pair has already been calculated, check if asymmetrical or not, and return appropriate result
            elif dest_node <= len(dist_matrix):
                # if asymmetrical - take previous distance and subtract random value between (-)asym_max and (+)asym_max
                # as long as that value is >= min_value - otherwise default to min_value
                if asym:
                    node_dist_list.append(max(
                                            dist_matrix[dest_node][orig_node] + randint(asym_max * -1, asym_max),
                                            min_value
                                          ))
                # if symmetrical - return previously calculated value
                else:
                    node_dist_list.append(dist_matrix[dest_node][orig_node])
            # If node pair hasn't been calculated yet - generate a random value within user specified constraints
            else:
                node_dist_list.append(randint(min_value, max_value))
        dist_matrix.append(node_dist_list)
    return dist_matrix


def _main():
    length = 10
    minimum_value = 20
    maximum_value = 5000
    asymmetry_value = 150
    matrix = gen_dist_matrix(length, minimum_value, maximum_value)
    asym_matrix = gen_dist_matrix(length, minimum_value, maximum_value, asym=True, asym_max=asymmetry_value)

    # unit test case: symmetric: value is 0 for all instances where origin node = destination node
    for idx, row in enumerate(matrix):
        assert row[idx] == 0

    # unit test case: symmetric: length of matrix is equal to user specified length
    assert len(matrix) == length

    # unit test case: symmetric: function returns a list
    assert type(gen_dist_matrix(length, minimum_value, maximum_value)) is list

    # unit test case: asymmetric: function returns a list
    assert type(gen_dist_matrix(length, minimum_value, maximum_value, asym=True, asym_max=asymmetry_value)) is list

    # unit test case: symmetric: smallest non-zero value in matrix is >= minimum_value
    for row in matrix:
        for value in row:
            if value is not 0:
                assert value >= minimum_value

    # unit test case: symmetric: number of 0's in matrix should equal the length/node count of matrix
    sym_zero_count = 0
    for row in matrix:
        for value in row:
            if value is 0:
                sym_zero_count += 1
    assert sym_zero_count == length

    # unit test case: symmetric: largest value in matrix is <= maximum_value
    for row in matrix:
        for value in row:
            assert value <= maximum_value

    # unit test case: asymmetric: value is 0 for all instances where origin node = destination node
    for idx, row in enumerate(asym_matrix):
        assert row[idx] == 0

    # unit test case: asymmetric: length of matrix is equal to user specified length
    assert len(asym_matrix) == length

    # unit test case: asymmetric: smallest non-zero value in matrix is >= minimum_value
    for row in asym_matrix:
        for value in row:
            if value is not 0:
                assert value >= minimum_value

    # unit test case: symmetric: number of 0's in matrix should equal the length/node count of matrix
    asym_zero_count = 0
    for row in asym_matrix:
        for value in row:
            if value is 0:
                asym_zero_count += 1
    assert asym_zero_count == length

    # unit test case: asymmetric: largest value in matrix is <= maximum_value
    for row in asym_matrix:
        for value in row:
            assert value <= maximum_value + asymmetry_value

    # unit test case: symmetric & asymmetric: negative/bad/zero values in inputs should raise ValueError
    bad_values = [-1, 0, -5, -123]
    for bad in bad_values:
        try:
            gen_dist_matrix(bad, minimum_value, maximum_value)
            raise AssertionError(f'{bad} was a bad length value and should have raised a ValueError')
        except ValueError:
            pass
        try:
            gen_dist_matrix(length, bad, maximum_value)
            raise AssertionError(f'{bad} was a bad min_value value and should have raised a ValueError')
        except ValueError:
            pass
        try:
            gen_dist_matrix(length, minimum_value, bad)
            raise AssertionError(f'{bad} was a bad max_value value and should have raised a ValueError')
        except ValueError:
            pass
        try:
            gen_dist_matrix(bad, minimum_value, maximum_value, asym=True, asym_max=asymmetry_value)
            raise AssertionError(f'{bad} was a bad length value and should have raised a ValueError')
        except ValueError:
            pass
        try:
            gen_dist_matrix(length, bad, maximum_value, asym=True, asym_max=asymmetry_value)
            raise AssertionError(f'{bad} was a bad min_value value and should have raised a ValueError')
        except ValueError:
            pass
        try:
            gen_dist_matrix(length, minimum_value, bad, asym=True, asym_max=asymmetry_value)
            raise AssertionError(f'{bad} was a bad max_value value and should have raised a ValueError')
        except ValueError:
            pass
        try:
            gen_dist_matrix(length, minimum_value, maximum_value, asym=True, asym_max=bad)
            raise AssertionError(f'{bad} was a bad asym_max value and should have raised a ValueError')
        except ValueError:
            pass

    # unit test case: symmetric & asymmetric: bad types should throw type error
    bad_types = [True, False, [], (), {}, None, 'A', 8.8, 19.0901, range(15), [1, 2, 3], {'a': 'b'}, (1, 2, 3,),
                 {1, 2, 'a'}, object]
    for bad in bad_types:
        try:
            gen_dist_matrix(bad, minimum_value, maximum_value)
            raise AssertionError(f'{bad} was a bad length type and should have raised a TypeError')
        except TypeError:
            pass
        try:
            gen_dist_matrix(length, bad, maximum_value)
            raise AssertionError(f'{bad} was a bad min_value type and should have raised a TypeError')
        except TypeError:
            pass
        try:
            gen_dist_matrix(length, maximum_value, bad)
            raise AssertionError(f'{bad} was a bad max_value type and should have raised a TypeError')
        except TypeError:
            pass
        try:
            gen_dist_matrix(bad, minimum_value, maximum_value, asym=True, asym_max=asymmetry_value)
            raise AssertionError(f'{bad} was a bad length type and should have raised a TypeError')
        except TypeError:
            pass
        try:
            gen_dist_matrix(length, bad, maximum_value, asym=True, asym_max=asymmetry_value)
            raise AssertionError(f'{bad} was a bad min_value type and should have raised a TypeError')
        except TypeError:
            pass
        try:
            gen_dist_matrix(length, minimum_value, bad, asym=True, asym_max=asymmetry_value)
            raise AssertionError(f'{bad} was a bad max_value type and should have raised a TypeError')
        except TypeError:
            pass
        try:
            gen_dist_matrix(length, minimum_value, maximum_value, asym=True, asym_max=bad)
            raise AssertionError(f'{bad} was a bad asym_max type and should have raised a TypeError')
        except TypeError:
            pass
    for bad in bad_types[2:]:
        try:
            gen_dist_matrix(length, minimum_value, maximum_value, asym=bad, asym_max=asymmetry_value)
            raise AssertionError(f'{bad} was a bad asym type and should have raised a TypeError')
        except TypeError:
            pass

    # unit test case: symmetric & asymmetric: min value must be less than max value
    test_min = 10
    test_max = 1
    try:
        gen_dist_matrix(length, test_min, test_max)
        raise AssertionError('Min value must be less than max value')
    except ValueError:
        pass
    try:
        gen_dist_matrix(length, test_min, test_min)
        raise AssertionError('Min value must be less than max value')
    except ValueError:
        pass
    try:
        gen_dist_matrix(length, test_min, test_max, asym=True, asym_max=asymmetry_value)
        raise AssertionError('Min value must be less than max value')
    except ValueError:
        pass
    try:
        gen_dist_matrix(length, test_min, test_min, asym=True, asym_max=asymmetry_value)
        raise AssertionError('Min value must be less than max value')
    except ValueError:
        pass


if __name__ == '__main__':
    _main()
