from vr_solver import cvrp_solve
from data_model import create_data_model

my_data = create_data_model(1)

cvrp_solve(my_data)