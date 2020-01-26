def _validate_inputs(user_data: list, num_vehicle: int, depot_loc: int = 0) -> bool:

    if type(user_data) is not list:
        raise TypeError('User data must be a list')
    if type(num_vehicle) or type(depot_loc) is not int:
        raise TypeError('num_vehicles and depot_loc must be a integers')
    if len(user_data) == 0:
        raise ValueError('user_data list cannot be empty')
    if num_vehicle <= 0:
        raise ValueError('num_vehicles must be greater than 0')
    if depot_loc < 0:
        raise ValueError('depot_loc cannot be less than 0')
    if depot_loc >= len(user_data):
        raise ValueError(f'depot_loc of {depot_loc} is outside the bounds of data array')
    for sub_list in user_data:
        if type(sub_list) is not list:
            raise TypeError('user_data must be a list of list of ints')
        for value in sub_list:
            if type(value) is not int:
                raise TypeError('user_data must be a list of list of ints')

    return True


def create_data_model(user_data: list, num_vehicle: int, depot_loc: int = 0) -> dict or None:
    """Establishes data model for use in ortools vehicle routing solver."""

    if _validate_inputs(user_data, num_vehicle, depot_loc):
        return None

    data = {'distance_matrix': user_data, 'num_vehicles': num_vehicle, 'depot': depot_loc}
    return data
