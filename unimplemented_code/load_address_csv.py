def load_address_csv(path: str) -> list:
    with open(path) as fh:
        file = fh.read()
        file = file.splitlines()
        file = [line.rstrip(',').replace(' ', '+').replace(',','+') for line in file]
        return file


def _main():
    filep = r'C:\Users\Travis\projects\vehicle-routing-webapp\unimplemented_code\addresses.csv'
    data = load_address_csv(filep)
    print(data)


if __name__ == '__main__':
    _main()
