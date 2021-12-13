from functools import partial
import struct
import re


def decimal_to_hex(num):
    """ convert binary decimal number to fixed length hex-code """
    return hex(num)[2:].rjust(2, '0').upper()


def read_binary_file(path):
    """ read file as a binary list """
    with open(path, 'rb') as f:
        struct_fmt = '=1B'  # read binary file as unsigned bytes
        struct_len = struct.calcsize(struct_fmt)
        struct_unpack = struct.Struct(struct_fmt).unpack_from
        return [struct_unpack(chunk) for chunk in iter(partial(f.read, struct_len), b'')]


def find_start_codes(bin_list):
    """ searches for E0C5EA hex-codes (start-codes) """

    bin_string = ''.join(map(lambda b: str(b[0]).rjust(3, '0'), bin_list))
    return [match.span()[0]//3 for match in re.finditer('224197234', bin_string)]


def slice(bin_list):
    """ slice a given binary list into chunks at the start-codes """
    markers = find_start_codes(bin_list) + [len(bin_list)-4]

    for (index, chunk_index) in enumerate(markers[:-1]):
        start_index, next_index = chunk_index, markers[index + 1]
        chunk = bin_list[start_index+3: next_index]
        assert (len(chunk)-5) % 5 == 0, "invalid chunk size"
        yield chunk


if __name__ == '__main__':
    # parse file
    path = "data/b1c622b2.bin"
    binary = read_binary_file(path)

    # slice binary list into chunks for each start-code
    for chunk_id, chunk in enumerate(slice(binary)):
        print(chunk_id, len(chunk))

    # print result
    # for index, chunk in enumerate(binary[4945:]):
    #     print(index, chunk[0], decimal_to_hex(chunk[0]))
