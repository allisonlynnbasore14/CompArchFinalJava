#------------------------------------------------------------------------------
# pycparser: c-to-c.py
#
# Example of using pycparser.c_generator, serving as a simplistic translator
# from C to AST and back to C.
#
# Eli Bendersky [https://eli.thegreenplace.net/]
# License: BSD
#------------------------------------------------------------------------------
from __future__ import print_function
import sys

# This is not required if you've installed pycparser into
# your site-packages/ with setup.py
#
sys.path.extend(['.', '..'])

from pycparser import parse_file, c_parser, c_generator


def translate_to_c(Newast):
    """ Simply use the c_generator module to emit a parsed AST.
    """
    ast = parse_file('exampleMin.c', use_cpp=True)

    ast.show()
    Newast.show()

    # print(ast.coord)
    # print(Newast.coord)
    # print("----------------------------------")
    # print(ast.ext[0].coord)
    # print(Newast.ext[0].coord)
    # print("----------------------------------")
    # print(ast.ext[0].decl.coord)
    # print(Newast.ext[0].decl.coord)
    # print("----------------------------------")
    print(ast.ext[0].decl.bitsize)
    print(Newast.ext[0].decl.bitsize)
    print("----------------------------------")
    print(ast.ext[0].decl.type.args.coord)
    print(Newast.ext[0].decl.type.args.coord)
    print("----------------------------------")
    print(ast.ext[0].decl.type.args.params)
    print(Newast.ext[0].decl.type.args.params)
    print("----------------------------------")
    print(ast.ext[0].decl.type.args.params[0].coord)
    print(Newast.ext[0].decl.type.args.params[0].coord)
    print("----------------------------------")
    print(ast.ext[0].decl.type.args.params[0].type.coord)
    print(Newast.ext[0].decl.type.args.params[0].type.coord)
    print("----------------------------------")
    print(ast.ext[0].decl.type.args.params[0].type.type.coord)
    print(Newast.ext[0].decl.type.args.params[0].type.type.coord)
    print("----------------------------------")
    print(ast.ext[0].decl.type.args.params[0].type.type.names)
    print(Newast.ext[0].decl.type.args.params[0].type.type.names)
    print("----------------------------------")

    generator = c_generator.CGenerator()
    #ast.show()

    print(generator.visit(ast))


#------------------------------------------------------------------------------
if __name__ == "__main__":
    #_zz_test_translate()
    if len(sys.argv) > 1:
        translate_to_c(sys.argv[1])
    else:
        print("Please provide a filename as argument")
