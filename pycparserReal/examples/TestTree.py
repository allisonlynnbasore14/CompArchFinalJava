#------------------------------------------------------------------------------
from __future__ import print_function
import sys

# This is not required if you've installed pycparser into
# your site-packages/ with setup.py
#
sys.path.extend(['.', '..'])

from pycparser import parse_file, c_parser, c_generator


file = open("ExampleOneInC.txt")
ast = file.read()
#ast = parse_file(filename, use_cpp=True)
generator = c_generator.CGenerator()
#st.show()

print(generator.visit(ast))