from vr_solver import cvrp_solve
from data_model import create_data_model
from distance_matrix import create_distance_matrix, create_data
from load_address_csv import load_address_csv
from load_key import load_key


def main():
    key = load_key(r'C:\Users\Travis\projects\vehicle-routing-webapp\unimplemented_code\secret.txt')
    addresses = load_address_csv(r'C:\Users\Travis\projects\vehicle-routing-webapp\unimplemented_code\addresses.csv')
    data = create_data(addresses, key)
    distance_matrix = create_distance_matrix(data)
    my_data = create_data_model(distance_matrix, 3)
    cvrp_solve(my_data)


if __name__ == '__main__':
    main()
