from models.data_model import create_data_model
from tests.errors.errors import UnitTypeError, UnitValueError
from models.validate_inputs.data_model import _validate_inputs


def test_data_model() -> bool:
    bad_list_types = [None, True, [[[[[]]]]], [[None]], [[1, 2, 3], [1, 2, 3], [1, 2, 'a']],
                      [[1, 2, 3], [1, 2, 3], [1, 2, None]], [[1, 2, 3], [1, 2, 3], [1.1, 2.2, 3.3]], object]

    bad_list_values = [[], [[1, 2, 3], [1, 2, 3], [1, 2]], [[1, 2, 3], [1, 2, 3]],
                       [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 0, 3], [0, 1, 3], [1, 2, 0]],
                       [[0, 2, 5], [2, 0, 8], [0, 8, 0]], [[0, 2, 5], [2, 1, 8], [5, 8, 0]]]

    bad_num_vehicles_types = [None, True, 'A', 1.1, [], {}, object]

    bad_num_vehicles_values = [-1, 0, -100]

    bad_depot_loc_types = [None, True, 2.2, 'A', [], (), {}, object]

    bad_depot_loc_values = [-1, 2000000, 3]

    good_list = [[0, 2, 5], [2, 0, 8], [5, 8, 0]]

    good_num_vehicle = 2

    good_depot_loc = 0

    for bad in bad_list_types:
        try:
            _validate_inputs(bad, good_num_vehicle, good_depot_loc)
            raise AssertionError(f'{bad} should cause unit type error for list input')
        except UnitTypeError:
            pass

    for bad in bad_list_values:
        try:
            _validate_inputs(bad, good_num_vehicle, good_depot_loc)
            raise AssertionError(f'{bad} should cause UnitValueError for list input')
        except UnitValueError:
            pass

    for bad in bad_num_vehicles_types:
        try:
            _validate_inputs(good_list, bad, good_depot_loc)
            raise AssertionError(f'{bad} should cause unit type error for num_vehicle input')
        except UnitTypeError:
            pass

    for bad in bad_num_vehicles_values:
        try:
            _validate_inputs(good_list, bad, good_depot_loc)
            raise AssertionError(f'{bad} should cause UnitValueError for num_vehicle input')
        except UnitValueError:
            pass

    for bad in bad_depot_loc_types:
        try:
            _validate_inputs(good_list, good_num_vehicle, bad)
            raise AssertionError(f'{bad} should cause unit type error for depot_loc input')
        except UnitTypeError:
            pass

    for bad in bad_depot_loc_values:
        try:
            _validate_inputs(good_list, good_num_vehicle, bad)
            raise AssertionError(f'{bad} should cause UnitValueError for depot_loc input')
        except UnitValueError:
            pass

    """
        Need to add unit tests which test the output of the create_data_model function
        
        Also need to add tests which proves a failure of the validate_inputs func in create_data_model returns None
    """

    return True
