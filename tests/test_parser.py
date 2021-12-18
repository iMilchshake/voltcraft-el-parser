import filecmp
import os
import pathlib

from voltcraft_el_parser.binary_parser import parse_file
from voltcraft_el_parser.writer import export_csv


def test_parser():
    """ simple test-case that tests the parsing against a pre-parsed file """

    data_directory = pathlib.Path(__file__).parent / 'data'

    # get relative directories
    file_in = data_directory / 'b1c622b2.bin'
    file_out = data_directory / 'tmp.csv'
    file_compare = data_directory / 'expected.csv'

    # parse binary file
    export_csv(parse_file(file_in), file_out)
    filecmp.clear_cache()
    result = filecmp.cmp(file_compare, file_out, shallow=False)

    # cleanup
    os.remove(file_out)

    # compare parsed file to expected file
    assert result, 'parsed file is not equal to expected file'
