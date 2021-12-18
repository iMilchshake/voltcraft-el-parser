def csv_string(data: iter):
    """ convert data to a csv-string. Expects data from parse_file() or parse_chunk() """

    out = 'datetime,voltage,ampere,power_factor\n'
    for time, voltage, ampere, power_factor in data:
        out += f'{time},{voltage},{ampere},{power_factor}\n'
    return out


def export_data(data_string: str, path: str):
    """ write a given string to a file """
    with open(path, 'w') as f:
        f.write(data_string)


def export_csv(data: iter, path: str):
    """ write given data to a csv-file """
    export_data(csv_string(data), path)
