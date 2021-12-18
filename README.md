Voltcraft Energy Logger - Parser
---

A python parse script for Voltcraft's Energy-Loggers. Tested with binary files from the versions 3500 and 4000, might work with more.
The implementation is based on [Voltcraft's documentation](https://forums.futura-sciences.com/attachments/technologies/345569d1499860464-calcul-de-consommation-electrique-kwh-aide-1voltcraft-data-protokoll_sd.pdf). The project doesn't have any additional dependencies.

## CLI-Application

```text
usage: python -m voltcraft_el_parser [-h] binary_path [out_path]

A parser for EL3500/EL4000 binary files

positional arguments:
  binary_path  path to the input binary file
  out_path     path for output .csv file (optional)

optional arguments:
  -h, --help   show this help message and exit
```

#### Examples:

- `python -m voltcraft_el_parser binfile.bin out.csv` > will export to out.csv
- `python -m voltcraft_el_parser binfile.bin` > will export to binfile.csv

## Usage in Python scripts


```python
from voltcraft_el_parser.binary_parser import parse_file

path_in = 'tests/data/b1c622b2.bin'
data = parse_file(path_in)

for time, voltage, ampere, power_factor in data:
    print(f'{time},{voltage},{ampere},{power_factor}')
```

