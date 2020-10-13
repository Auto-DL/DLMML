import json
import os
import sys
from pprint import pprint


def image_input(inputs):
    """
    request in input json.

    dataset-path -> path to dataset
    image-augment -> parameters for image augmentation if required
    params -> parameters for building generator
    """
    base = inputs['dataset']['path']
    test_dir = os.path.join(base, 'test')
    train_dir = os.path.join(base, 'train')

    paths = \
        """
        base = '{}'
        train_dir = os.path.join(base, 'train')
        test_dir = os.path.join(base, 'test')
        """.format(inputs['dataset']['path'])

    generators = \
        """
        augment = {}
        kwargs = {}

        train_datagen = ImageDataGenerator(**augment)
        test_datagen = ImageDataGenerator(**augment)
        train_generator = train_datagen.flow_from_directory(train_dir,
                                                            **kwargs)
        test_generator = test_datagen.flow_from_directory(test_dir, **kwargs)

        """.format(inputs['image']['augment'], inputs['image']['params'])

    return paths+generators
