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

from pycparser import parse_file, c_parser, c_generator, c_ast


def translate_to_c(Newast):
    """ Simply use the c_generator module to emit a parsed AST.
    """
    ast = parse_file('exampleMin.c', use_cpp=True)

    ast.show()
    #print("newast: ", Newast.ext[0].decl.type.args.params[0].type.type==ast.ext[0].decl.type.args.params[0].type.type)
    #print("newast2: ", Newast.ext[0].decl.type.args.params[0].type.type.coord)
    #print("ast2: ", ast.ext[0].decl.type.args.params[0].type.type.coord)

    #Newast.show()
    
    # print(ast.ext[0].decl.bitsize)
    # print(Newast.ext[0].decl.bitsize)
    # print("----------------------------------")
    # print(ast.ext[0].decl.type.args.coord)
    # print(Newast.ext[0].decl.type.args.coord)
    # print("----------------------------------")
    # print(ast.ext[0].decl.type.args.params)
    # print(Newast.ext[0].decl.type.args.params)
    # print("----------------------------------")
    # print(ast.ext[0].decl.type.args.params[0])
    # print(Newast.ext[0].decl.type.args.params[0])
    # print("----------------------------------")
    # print(ast.ext[0].decl.type.args.params[0].type)
    # print(Newast.ext[0].decl.type.args.params[0].type)
    # print("----------------------------------")
    # print(ast.ext[0].decl.type.args.params[0].type.type)
    # print(Newast.ext[0].decl.type.args.params[0].type.type)
    # print("----------------------------------")
    # print(ast.ext[0].decl.type.args.params[0].type.type.names)
    # print(Newast.ext[0].decl.type.args.params[0].type.type.names)
    # print("----------------------------------")

    generator = c_generator.CGenerator()
    #ast.show()

      # tracing the generator for debugging
    # import trace
    # tr = trace.Trace(countcallers=1)
    # tr.runfunc(generator.visit, Newast)
    # tr.results().write_results()

    print(generator.visit(Newast))


#------------------------------------------------------------------------------
if __name__ == "__main__":
    #_zz_test_translate()
    if len(sys.argv) > 1:
        translate_to_c(sys.argv[1])
    else:
        print("Please provide a filename as argument")
