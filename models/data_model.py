from tests.errors.errors import UnitTypeError, UnitValueError
from models.validate_inputs.data_model import _validate_inputs


def create_data_model(user_data: list, num_vehicle: int, depot_loc: int = 0) -> dict or None:
    """Establishes data model for use in ortools vehicle routing solver."""

    try:
        _validate_inputs(user_data, num_vehicle, depot_loc)
    except UnitTypeError or UnitValueError:
        return None

    data = {'distance_matrix': user_data, 'num_vehicles': num_vehicle, 'depot': depot_loc}
    return data
