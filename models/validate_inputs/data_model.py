from tests.errors.errors import UnitTypeError, UnitValueError


def _validate_inputs(user_data: list, num_vehicle: int, depot_loc: int = 0) -> bool:

    if type(user_data) is not list:
        raise UnitTypeError('User data must be a list')
    if type(num_vehicle) is not int:
        raise UnitTypeError('num_vehicles must be a integers')
    if type(depot_loc) is not int:
        raise UnitTypeError('depot_loc must be a integers')
    if len(user_data) == 0:
        raise UnitValueError('user_data list cannot be empty')
    if num_vehicle <= 0:
        raise UnitValueError('num_vehicles must be greater than 0')
    if depot_loc < 0:
        raise UnitValueError('depot_loc cannot be less than 0')
    if depot_loc >= len(user_data):
        raise UnitValueError(f'depot_loc of {depot_loc} is outside the bounds of data array')
    for sub_list in user_data:
        if type(sub_list) is not list:
            raise UnitTypeError('user_data must be a list of list of ints')
        if len(sub_list) != len(user_data):
            raise UnitValueError('Length of each sub-list should be equal to length of matrix')
        for value in sub_list:
            if type(value) is not int:
                raise UnitTypeError('user_data must be a list of list of ints')
    for indx, sub_list in enumerate(user_data):
        for indx2, value in enumerate(sub_list):
            if indx == indx2 and value != 0:
                raise UnitValueError('value must be 0 where dest and orig node are the same node')
            if indx != indx2 and value == 0:
                raise UnitValueError('value can only be 0 where dest and orig node are the same node')

    return True