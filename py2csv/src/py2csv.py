import ast
import csv
import sys


class Py2Csv:

    @staticmethod
    def convert(infile, outfile, header=None, mode='w+', fields=None):
        """Py2Csv.convert2("../test/resources/test_input_lists.txt", "/tmp/test.txt", ['header1', 'header2'])"""
        if infile is None or outfile is None:
            raise Exception('Both an input file and output file are required')

        with open(infile) as i, open(outfile, mode) as o:
            writer = csv.writer(o)
            dict_writer = csv.DictWriter(o, fieldnames=fields)
            # only write the header once, if there is one
            if header is not None and mode == 'w+':
                writer.writerow(header)
            for line in i:
                # Read the line as literal Python code
                r = ast.literal_eval(line)
                # Dicts require a special writer
                if type(r) is dict:
                    if fields is None:
                        raise Exception("Dict conversion requires field names")
                    else:
                        dict_writer.writerow(r)
                # Tuples and Lists use the default writer
                else:
                    writer.writerow(r)


if __name__ == '__main__':
    # TODO: use argparse for better command line argument handling:
    # https://docs.python.org/3/library/argparse.html#module-argparse
    # Run with python Py2Csv.py infile outfile
    try:
        # Input file
        input_file = sys.argv[1]
        # Output file
        output_file = sys.argv[2]
    except:
        raise Exception('Both an input file and output file are required')
    # TODO: handle optional argument for DictWriter fieldnames
    try:
        headers = sys.argv[3]
    except:
        headers = None
    p = Py2Csv()
    p.convert(input_file, output_file, headers)
