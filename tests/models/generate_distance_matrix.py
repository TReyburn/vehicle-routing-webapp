from models.generate_distance_matrix import gen_dist_matrix


def test_gen_dist_matrix() -> bool:

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

    return True
