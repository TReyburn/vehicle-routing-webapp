from models.data_model import create_data_model


def test_data_model() -> bool:

    bad_lists = [None, True, [], [[[[[]]]]], [[None]], [[1, 2, 3], [1, 2, 3], [1, 2]], [[1, 2, 3], [1, 2, 3]],
                 [[1, 2, 3], [1, 2, 3], [1, 2, 'a']], [[1, 2, 3], [1, 2, 3], [1, 2, None]],
                 [[1, 2, 3], [1, 2, 3], [1.1, 2.2, 3.3]]]

    bad_num_vehicles = [None, True, -1, 0, -100, 'A', 1.1, [], {}]

    bad_depot_lot = [None, True, -1, 2000000, 2.2, 'A', [], (), {}]

    # impliment unit tests here

    return True
