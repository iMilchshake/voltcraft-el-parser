import argparse
from energylogger_parser.writer import csv_string, export_data
from energylogger_parser.binary_parser import parse_file


def run():
    parser = argparse.ArgumentParser(description="A parser for EL3500/EL4000 binary files", prefix_chars="-",
                                     prog="python -m energylogger_parser")
    parser.add_argument("binary_path", type=str, help="path to the input binary file")
    parser.add_argument("out_path", type=str, help="path to create an output .csv file")
    args = vars(parser.parse_args())

    export_data(csv_string(parse_file(args['binary_path'])), args['out_path'])
    print(args['out_path'], 'was sucessfully created!')