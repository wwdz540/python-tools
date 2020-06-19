"""Command-line tool to validate and pretty-print JSON

Usage::

    $ echo '{"json":"obj"}' | python -m json.tool
    {
        "json": "obj"
    }
    $ echo '{ 1.2:3.4}' | python -m json.tool
    Expecting property name enclosed in double quotes: line 1 column 3 (char 2)

"""
import argparse
import json
import sys


def main():
    prog = 'python -m json.tool'
    description = ('A simple command line interface for json module '
                   'to validate and pretty-print JSON objects.')
    parser = argparse.ArgumentParser(prog=prog, description=description)
    parser.add_argument('infile', nargs='?', type=argparse.FileType(),
                        help='a JSON file to be validated or pretty-printed')
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
                        help='write the output of infile to outfile')
    parser.add_argument('--sort-keys', action='store_true', default=False,
                        help='sort the output of dictionaries alphabetically by key')
    parser.add_argument('--path',
            help='json 对像路径')
    options = parser.parse_args()

    infile = options.infile or sys.stdin
    outfile = options.outfile or sys.stdout
    sort_keys = options.sort_keys
    path = options.path
    with infile:
        try:
            obj = json.load(infile)
        except ValueError as e:
            raise SystemExit(e)
    obj = parse(obj,path)
    with outfile:
#        print(type(obj))
        if isinstance(obj,str):
            outfile.write(obj)
        else:    
            json.dump(obj, outfile, sort_keys=sort_keys, indent=4,ensure_ascii=False)
        outfile.write('\n')

def parse(obj,path):
    if not path :
        return obj
    pathArr = path.split(".")

    for p in pathArr:
        obj = obj[p] 
    return obj




if __name__ == '__main__':
    main()
