def create_data_model(user_data: list, num_vehicle: int) -> dict:
    """Establishes data model for use in ortools vehicle routing solver."""

    data = {'distance_matrix': user_data, 'num_vehicles': num_vehicle, 'depot': 0}
    return data