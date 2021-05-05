import jxty

import sys

# from https://stackoverflow.com/questions/9027028/argparse-argument-order
import argparse
class CustomAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if not 'ordered_args' in namespace:
            setattr(namespace, 'ordered_args', [])
        previous = namespace.ordered_args
        previous.append((self.dest, values or "-"))
        setattr(namespace, 'ordered_args', previous)

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--json', '-j', action=CustomAction, nargs='?')
    parser.add_argument('--xml',  '-x', action=CustomAction, nargs='?')
    parser.add_argument('--toml', '-t', action=CustomAction, nargs='?')
    parser.add_argument('--yaml', '-y', action=CustomAction, nargs='?')

    args = parser.parse_args()
    io_list = args.ordered_args

    if len(io_list) !=2:
        assert("invalid arg number. you must set 2 args")

    in_fmt,  in_name  = io_list[0]
    in_file = open(in_name, mode="r") if in_name != "-" else sys.stdin
    out_fmt, out_name = io_list[1]
    out_file = open(out_name, mode="w") if out_name != "-" else sys.stdout

    obj = jxty.load(in_fmt, in_file)
    jxty.dump(obj, out_fmt, out_file)

if __name__ == "__main__" :
    main()