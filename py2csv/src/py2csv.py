import ast
import csv
import sys


class Py2Csv:
    def __init__(self):
        self.output = []

    # Public instance methods.
    # To use: myPy2CsvInstance = Py2Csv()
    # myPy2CsvInstance.convert("../test/resources/test_input_lists.txt", "/tmp/test.txt", ['header1', 'header2'])
    def convert(self, infile, outfile, header=None, mode='w+', fields=None):
        if infile is None or outfile is None:
            raise Exception('Both an input file and output file are required')

        # We have to clear the stored output from the Py2Csv instance each time. Otherwise subsequent calls will write
        # the previous data out as well the new stuff
        self.output.clear()

        # FIXME: This will crash if the input contains both Dicts and lists/tuples
        self._read_file(infile)
        if type(self.output[0]) is dict:
            if fields is None:
                raise Exception("Dict conversion requires field names")
            self._write_dict_file(outfile, header, mode, fields)
        else:
            self._write_file(outfile, header, mode)

    # private methods
    def _read_file(self, infile):
        with open(infile) as f:
            for line in f:
                self.output.append(ast.literal_eval(line))

    def _write_file(self, outfile, header, mode):
        with open(outfile, mode) as out:
            writer = csv.writer(out)
            if header is not None and mode == 'w+':
                writer.writerow(header)
            for i in self.output:
                writer.writerow(i)

    def _write_dict_file(self, outfile, header, mode, fields):
        with open(outfile, mode) as out:
            writer = csv.DictWriter(out, fieldnames=fields)
            if header is not None:
                writer.writerow(header)
            for i in self.output:
                writer.writerow(i)

    # Reading all of the input file into memory and then writing it out is wasteful and may not work for large files.
    # This will both read and write one line at a time
    # Static methods don't require a Class instance, so they can be called directly like so:
    # Py2Csv.convert2("../test/resources/test_input_lists.txt", "/tmp/test.txt", ['header1', 'header2'])
    @staticmethod
    def read_and_write_file(infile, outfile, header=None, mode='w+', fields=None):
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
