import requests
from load_address_csv import load_address_csv
from load_key import load_key


def create_data(user_address: list, key: str) -> dict:
    """ Creates the data model from user inputs."""

    data = {'API_key': key, 'addresses': user_address}
    return data


def build_address_str(addresses: list) -> str:
    """ Build a pipe-separated string of addresses from a list."""

    address_str = ''
    for i in range(len(addresses) - 1):
        address_str += addresses[i] + '|'
    address_str += addresses[-1]
    return address_str


def send_request(origin_addresses: list, dest_addresses: list, api_key: str) -> dict:
    """ Build and send request for the given origin and destination addresses."""

    request = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial'
    origin_address_str = build_address_str(origin_addresses)
    dest_address_str = build_address_str(dest_addresses)
    request = request + '&origins=' + origin_address_str + '&destinations=' + dest_address_str + '&key=' + api_key
    json_result = requests.get(request)
    response = json_result.json()
    return response


def build_distance_matrix(response: dict) -> list:
    """ Parses Distance Matrix API response and assembles distance matrix list."""

    distance_matrix = []
    for row in response['rows']:
        row_list = [row['elements'][j]['distance']['value'] for j in range(len(row['elements']))]
        distance_matrix.append(row_list)
    return distance_matrix


def create_distance_matrix(data: dict) -> list:
    """
        Assembles calls for the Distance Matrix API to conform to 100 max elements constraint of API,
        calls the API,
        parses the results from the API,
        then assembles and returns the resulting distance matrix.
    """

    # Establishing required internal data structure from data model.
    addresses = data["addresses"]
    api_key = data["API_key"]

    # Distance Matrix API only accepts 100 elements per request, so get rows in multiple requests.
    max_elements = 100
    # 16 addresses for this example
    num_addresses = len(addresses)

    # Maximum number of rows that can be computed per request (6 in this example).
    max_rows = max_elements // num_addresses

    # num_addresses = q * max_rows + r (q = 2 and r = 4 in this example).
    # q is the whole Quotient and r is the Remainder
    q, r = divmod(num_addresses, max_rows)
    dest_addresses = addresses
    distance_matrix = []

    # Send q requests, returning max_rows rows per request.
    for i in range(q):
        # creating a list slice of address list for each row in q
        # if i = 1, q = 2, and max_rows = 6; our list is sliced as addresses[6:12]
        origin_addresses = addresses[i * max_rows: (i + 1) * max_rows]
        response = send_request(origin_addresses, dest_addresses, api_key)
        distance_matrix += build_distance_matrix(response)

    # Get the remaining remaining r rows, if necessary.
    if r > 0:
        # creating a list slice of address list
        # if q = 2 ,r = 4, and max_rows = 6; our list is sliced as addresses[12:16]
        origin_addresses = addresses[q * max_rows: q * max_rows + r]
        response = send_request(origin_addresses, dest_addresses, api_key)
        distance_matrix += build_distance_matrix(response)
    return distance_matrix


def _main():
    key = load_key(r'C:\Users\Travis\projects\vehicle-routing-webapp\unimplemented_code\secret.txt')
    addresses = load_address_csv(r'C:\Users\Travis\projects\vehicle-routing-webapp\unimplemented_code\addresses.csv')
    data = create_data(addresses, key)
    distance_matrix = create_distance_matrix(data)
    print(distance_matrix)


if __name__ == '__main__':
    _main()
