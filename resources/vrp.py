from flask_restful import Resource
from models.generate_distance_matrix import gen_dist_matrix
from models.data_model import create_data_model
from models.vrp import vrp_solve


class VehicleRouting(Resource):

    def __init__(self):
        self.dist_matrix = gen_dist_matrix(75, 15, 800, asym=True, asym_max=15)
        self.data_model = create_data_model(self.dist_matrix, 5)

    def get(self):
        return vrp_solve(self.data_model)
