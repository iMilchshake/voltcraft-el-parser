import argparse

from voltcraft_el_parser.binary_parser import parse_file
from voltcraft_el_parser.writer import export_csv


def run():
    """ run argparse cli-application """
    parser = argparse.ArgumentParser(description="A parser for EL3500/EL4000 binary files",
                                     prog="python -m voltcraft_el_parser")
    parser.add_argument("binary_path", type=str, help="path to the input binary file")
    parser.add_argument("out_path", type=str, help="path to create an output .csv file")
    args = vars(parser.parse_args())

    export_csv(parse_file(args['binary_path']), args['out_path'])
    print(args['out_path'], 'was sucessfully created!')
