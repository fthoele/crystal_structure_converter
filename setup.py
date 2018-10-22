from distutils.core import setup

setup(name='Crystal Structure Converter',      
      install_requires = ["ase"],
      scripts = ['convert_structure.py'],
      version='0.1',
      )