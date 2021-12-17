import argparse
from os.path import basename, splitext

from voltcraft_el_parser.binary_parser import parse_file
from voltcraft_el_parser.writer import export_csv


def run():
    """ run argparse cli-application """
    parser = argparse.ArgumentParser(description="A parser for EL3500/EL4000 binary files",
                                     prog="python -m voltcraft_el_parser")
    parser.add_argument("binary_path", type=str, help="path to the input binary file")
    parser.add_argument("out_path", nargs='?', type=str, help="path for output .csv file (optional)")
    args = vars(parser.parse_args())

    # determine output path
    out_path = args['out_path']
    if not out_path:
        out_path = splitext(basename(args['binary_path']))[0] + '.csv'

    # export to csv
    export_csv(parse_file(args['binary_path']), out_path)
    print(out_path, 'was sucessfully created!')
