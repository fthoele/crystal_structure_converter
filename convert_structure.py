"""Convert between crystal structure formats using ASE.
For a list of supported formats, see 
https://wiki.fysik.dtu.dk/ase/ase/io/io.html.

Among the supported formats:
- espresso-in: Quantum ESPRESSO input files
- xsf: xcrysden 
- cif
- xyz
"""

import sys

def check_ase_is_installed():
    try:
        import ase.io
    except ModuleNotFoundError:
        print("Error importing ASE. You can install it by running the following command:")
        print("$ pip install ase")
        exit()

if __name__ == "__main__":    
    check_ase_is_installed()

    import argparse
    parser = argparse.ArgumentParser(description=__doc__, 
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-i', '--in', help='Filename of input', required=True, dest="input")
    parser.add_argument('-o', '--out', help='Filename to write the output to. If not given, print to stdout')
    parser.add_argument('-f', '--from-format', help='Format of input file', required=True)
    parser.add_argument('-t', '--to-format', help='Format of output', required=True)
    args = parser.parse_args()    

    import ase.io
    structure = ase.io.read(args.input, format=args.from_format)
    
    if args.out:
        filename = args.out
        ase.io.write(filename, structure, format=args.to_format)
    else:
        import io
        output_stream = io.StringIO()
        ase.io.write(output_stream, structure, format=args.to_format)
        content = output_stream.getvalue()
        print(content)

    
    