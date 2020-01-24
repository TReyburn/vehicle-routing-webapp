def load_address_csv(path):
    with open(path) as fh:
        file = fh.read()
        file = file.splitlines()
        file = [line.rstrip(',').replace(' ', '+').replace(',','+') for line in file]
        return file


def main():
    filep = r'C:\Users\Travis\projects\vehicle-routing-webapp\unimplemented_code\address2.csv'
    data = load_address_csv(filep)
    print(data)


if __name__ == '__main__':
    main()