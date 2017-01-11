from pykwalify.core import Core
import os

here = os.path.dirname(os.path.realpath(__file__))

schema_file = os.path.join(here, 'schema.yml')
data_file = os.path.join(here, 'data.yml')
extension = os.path.join(here, 'validate.py')

c = Core(source_file=data_file, schema_files=[schema_file], extensions=[extension])
c.validate()