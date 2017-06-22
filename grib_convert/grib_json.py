import argparse
import json
import traceback

from eccodes import *

from grib2python import grib2array

VERBOSE = 1  # verbose error reporting


def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("gribfile", type=str, help="the filename of the grib to be converted")

    args = parser.parse_args()
    try:
        structure = grib2array.convert_array(args.gribfile)
        print json.dumps(structure, default=set_default, indent=1, separators=(',', ': '))

    except CodesInternalError as err:
        if VERBOSE:
            traceback.print_exc(file=sys.stderr)
        else:
            sys.stderr.write(err.msg + '\n')

        return 1


if __name__ == "__main__":
    sys.exit(main())

