import struct
import re
from functools import partial
from datetime import datetime, timedelta


def decimal_to_hex(num):
    """ convert binary decimal number to fixed length hex-code """
    return hex(num)[2:].rjust(2, '0').upper()


def read_binary_file(path):
    """ read file as a binary list """
    with open(path, 'rb') as f:
        struct_fmt = '=1B'  # read binary file as unsigned bytes
        struct_len = struct.calcsize(struct_fmt)
        struct_unpack = struct.Struct(struct_fmt).unpack_from
        return list(map(lambda b: b[0],
                        [struct_unpack(chunk) for chunk in iter(partial(f.read, struct_len),
                                                                b'')]))


def find_start_codes(bin_list):
    """ searches for E0C5EA hex-codes (start-codes) """

    bin_string = ''.join(map(lambda b: str(b).rjust(3, '0'), bin_list))
    return [match.span()[0]//3 for match in re.finditer('224197234', bin_string)]


def slice(bin_list):
    """ slice a given binary list into chunks at the start-codes """
    markers = find_start_codes(bin_list) + [len(bin_list)-4]

    for (index, chunk_index) in enumerate(markers[:-1]):
        start_index, next_index = chunk_index, markers[index + 1]
        chunk = bin_list[start_index+3: next_index]
        assert (len(chunk)-5) % 5 == 0, "invalid chunk size"
        yield chunk


def parse_chunk(chunk):
    """ parse a given chunk and yield each data row """

    # get chunk date (5 Byte)
    date = datetime(month=chunk[0], day=chunk[1],
                    year=2000+chunk[2], hour=chunk[3], minute=chunk[4])

    # get data rows (5Byte each)
    for data_index in range(0, (len(chunk)-5)//5):
        data = chunk[(5*data_index)+5: (5*data_index)+10]

        # calculate "true" values
        voltage = int(decimal_to_hex(data[0])+decimal_to_hex(data[1]), 16)/10
        ampere = int(decimal_to_hex(data[2])+decimal_to_hex(data[3]), 16)/1000
        power_factor = data[4]/100
        time = date + timedelta(minutes=data_index)
        yield time, voltage, ampere, power_factor


def parse_file(path):
    """ read and parse a given file """
    data = list()
    for chunk in slice(read_binary_file(path)):
        data += parse_chunk(chunk)
    return data
