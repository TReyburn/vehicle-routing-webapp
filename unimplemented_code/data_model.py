def create_data_model(user_data: list, num_vehicle: int) -> dict:
    """Stores the data for the problem."""
    data = {'distance_matrix': user_data, 'num_vehicles': num_vehicle, 'depot': 0}
    return data
