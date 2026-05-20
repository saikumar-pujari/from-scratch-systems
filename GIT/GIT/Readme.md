to install the ugit package, run the following command in your terminal:

```bash
pip install setuptools
``` 


>After installing setuptools, you can install the ugit package by running

remember to be in the setup.py directory when you run the following command:

```bash
pip install -e .
```
it will genrate the ugit package called ugit.egg-info in the same directory as setup.py. You can then import the ugit package in your Python code and use its functionality.

"""
to test the hash-object,create a file with ugit not inside of it and use the following command in the terminal:

```bash
ugit init
ugit hash-object <filename>
```
it will print the hash of the file to the console. 
"""