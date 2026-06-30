import pickle
import pprint

data = [{'a': 'A', 'b': 2, 'c': 3.0}]
print('DATA:', end=' ')
# DATA: [{'a': 'A', 'b': 2, 'c': 3.0}]
pprint.pprint(data)
print("-" *20)
print(data)
print("-" *20)
data_string = pickle.dumps(data)
print('PICKLE: {!r}'.format(data_string))
# By default, the pickle will be written in a binary format
# PICKLE: b'\x80\x04\x95#\x00\x00\x00\x00\x00\x00\x00]\x94}\x94(\x8c\x01a\x94\x8c\x01A\x94\x8c\x01b\x94K\x02\x8c\x01c\x94G@\x08\x00\x00\x00\x00\x00\x00ua.'
# This byte string is the serialized, binary representation of the object that can be saved to a file or transmitted over a network.