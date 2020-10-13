import json
import os
import sys
from pprint import pprint


def init_sequential():
    """initialize the model."""
    try:
        return \
            '\nmodel = Sequential()\n'

    except Exception as e:
        print(e)
