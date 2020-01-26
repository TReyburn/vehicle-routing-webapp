from vr_solver import vrp_solve
from data_model import create_data_model
from distance_matrix import create_distance_matrix, create_data
from load_address_csv import load_address_csv
from load_key import load_key
from generate_distance_matrix import gen_dist_matrix


def main():
    debug = True
    asym = True
    key = load_key(r'C:\Users\Travis\projects\vehicle-routing-webapp\unimplemented_code\secret.txt')
    addresses = load_address_csv(r'C:\Users\Travis\projects\vehicle-routing-webapp\unimplemented_code\addresses.csv')
    data = create_data(addresses, key)
    if debug and not asym:
        print('1')
        distance_matrix = gen_dist_matrix(50, 15, 900)
    elif debug and asym:
        print('2')
        distance_matrix = gen_dist_matrix(100, 15, 900, asym=True, asym_max=50)
    else:
        print('3')
        distance_matrix = create_distance_matrix(data)
    my_data = create_data_model(distance_matrix, 3)
    output = vrp_solve(my_data)
    print(output)


if __name__ == '__main__':
    main()
