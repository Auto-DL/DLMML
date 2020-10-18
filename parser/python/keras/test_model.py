import json
import os
import sys
from pprint import pprint

from .imports import get_imports
from .init import init_sequential
from .inputs import image_input
from .layers import parse
from .train_pipeline import compile_model
from .visualize import add_plots_and_summary


def test_compile_model(input_dict):
    """
    input_dict - dictionary of nested json
    """
    try:
        with open('compile_test.py', 'w') as f:
            inputs = input_dict
            f.write(get_imports())
            f.write(add_plots_and_summary())
            f.write(image_input(inputs))
            f.write(init_sequential())
            f.write(parse(inputs))
            f.write(compile_model(inputs))
        import compile_test
        os.system('rm compile_test.py')
        return 0, None
    except Exception as e:
        print("Error - ", e)
        return 1, str(e)
