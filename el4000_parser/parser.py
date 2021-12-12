from functools import partial
import struct
import re


def decimal_to_hex(num):
    """ convert binary decimal number to fixed length hex-code """
    return hex(num)[2:].rjust(2, '0').upper()


def parse_file(path):
    """ parse file as a binary list """
    with open(path, 'rb') as f:
        struct_fmt = '=1B'  # read binary file as unsigned bytes
        struct_len = struct.calcsize(struct_fmt)
        struct_unpack = struct.Struct(struct_fmt).unpack_from
        return [struct_unpack(chunk) for chunk in iter(partial(f.read, struct_len), b'')]


def find_start_codes(bin_list):
    """ searches for E0C5EA hex-code (start-codes) """

    bin_string = ''.join(map(lambda b: str(b[0]), bin_list))
    return [match.span()[0]//3 for match in re.finditer('224197234', bin_string)]


if __name__ == '__main__':
    # parse file
    path = "data/b1c622b2.bin"
    results = parse_file(path)

    # search for start codes
    start_codes = find_start_codes(results)
    print(start_codes)

    # print result
    for index, chunk in enumerate(results[:20]):
        print(index, chunk[0], decimal_to_hex(chunk[0]))
