import os
import hashlib


# its like .git but we are calling it .ugit and we will store all the git data in that directory
# na me of the directory where the git data will be stored,you can name anything!
GIT_DIR = '.ugit'


def init():
    os.makedirs(GIT_DIR, exist_ok=True)
    os.makedirs(f'{GIT_DIR}/objects', exist_ok=True)


# def hash_object(data):
#     oid = hashlib.sha1(data).hexdigest()
#     with open(f'{GIT_DIR}/objects/{oid}', 'wb') as out:
#         out.write(data)
#     return oid

# def get_object(oid):
#     with open(f'{GIT_DIR}/objects/{oid}', 'rb') as f:
#         return f.read()
def hash_object (data, type_='blob'):
    obj = type_.encode () + b'\x00' + data
    oid = hashlib.sha1 (obj).hexdigest ()
    with open (f'{GIT_DIR}/objects/{oid}', 'wb') as out:
        out.write (obj)
    return oid


def get_object (oid, expected='blob'):
    with open (f'{GIT_DIR}/objects/{oid}', 'rb') as f:
        obj = f.read ()
    type_, _, content = obj.partition (b'\x00')
    type_ = type_.decode ()
    if expected is not None:
        assert type_ == expected, f'Expected {expected}, got {type_}'
    return content
