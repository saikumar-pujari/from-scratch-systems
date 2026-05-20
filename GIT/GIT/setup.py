
from setuptools import setup

"""
μgit (ugit) is a small implementation of a Git-like version control system (VCS). It's top goal is simplicity and educational value.
we created a setup.py file that describes the ugit executable. The executable calls the main() function in cli.py once invoked.
"""

setup(name='ugit',
      version='1.0',
      packages=['ugit'],
      entry_points={
           'console_scripts': [
               'ugit = ugit.cli:main',
               'ugit-test = ugit.cli:test'
           ]}
      )

# everytime we add a entrypoint we have a run the terminal to update the package as (pip install -e .) then ugit
# inside the ugit.egg-info/entry_points.txt file we can see the entry points that we have added.
