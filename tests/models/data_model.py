from models.data_model import create_data_model
from tests.errors.errors import UnitTypeError, UnitValueError


def test_data_model() -> bool:
    bad_list_types = [None, True, [[[[[]]]]], [[None]], [[1, 2, 3], [1, 2, 3], [1, 2, 'a']],
                      [[1, 2, 3], [1, 2, 3], [1, 2, None]], [[1, 2, 3], [1, 2, 3], [1.1, 2.2, 3.3]]]

    bad_list_values = [[], [[1, 2, 3], [1, 2, 3], [1, 2]], [[1, 2, 3], [1, 2, 3]],
                       [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 0, 3], [0, 1, 3], [1, 2, 0]],
                       [[0, 2, 5], [2, 0, 8], [0, 8, 0]], [[0, 2, 5], [2, 1, 8], [5, 8, 0]]]

    bad_num_vehicles_types = [None, True, 'A', 1.1, [], {}]

    bad_num_vehicles_values = [-1, 0, -100]

    bad_depot_loc_types = [None, True, 2.2, 'A', [], (), {}]

    bad_depot_loc_values = [-1, 2000000]

    good_list = [[0, 2, 5], [2, 0, 8], [5, 8, 0]]

    good_num_vehicle = 2

    good_depot_loc = 0

    for bad in bad_list_types:
        try:
            create_data_model(bad, good_num_vehicle, good_depot_loc)
            raise AssertionError(f'{bad} should cause unit type error for list input')
        except UnitTypeError:
            pass

    for bad in bad_list_values:
        try:
            create_data_model(bad, good_num_vehicle, good_depot_loc)
            raise AssertionError(f'{bad} should cause UnitValueError for list input')
        except UnitValueError:
            pass

    return True
