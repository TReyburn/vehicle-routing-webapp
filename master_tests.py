from tests.models.generate_distance_matrix import test_gen_dist_matrix
from tests.models.data_model import test_data_model

if test_gen_dist_matrix():
    print('gen_dist_matrix() tests: success')

if test_data_model():
    print('create_data_model() tests: success')
