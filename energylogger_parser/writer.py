from typing import Generator

from energylogger_parser.binary_parser import parse_file


def csv_string(data: Generator):
    """ convert data to a csv-string
        expects data from parse_file() or parse_chunk() """

    out = 'datetime,voltage,ampere,power_factor\n'
    for time, voltage, ampere, power_factor in data:
        out += f'{time},{voltage},{ampere},{power_factor}\n'
    return out


def export_data(data_string: str, path: str):
    """ write a given string to a file """
    with open(path, 'w') as f:
        f.write(data_string)
