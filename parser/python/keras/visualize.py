import json
import os
import sys
from pprint import pprint


def add_plots_and_summary(fname="test"):
    """Add plot and summary of the model."""
    return \
        """
        def summarize_diagnostics(history, save_plots):
            # plot loss
            pyplot.subplot(211)
            pyplot.title('Cross Entropy Loss')
            pyplot.plot(history.history['loss'], color='blue', label='train')
            pyplot.plot(history.history['val_loss'],
                        color='orange', label='test')

            # plot accuracy
            pyplot.subplot(212)
            pyplot.title('Classification Accuracy')
            pyplot.plot(history.history['accuracy'],
                        color='blue', label='train')
            pyplot.plot(history.history['val_accuracy'],
                        color='orange', label='test')

            # save plot to file
            if save_plots:
                filename = '{}'
                pyplot.savefig(filename + '_plot.png')
                pyplot.close()
        """.format(fname)


def plot_and_summarize_model(inputs):
    """Plotting the graphs of model accuracy and model loss."""
    if eval(inputs.get('plot', False)):
        return \
            """
            # Plotting graphs and Summarizing Model
            summarize_diagnostics(history, {})
            """.format(eval(inputs.get('save_plots', False)))

    else:
        return ''
