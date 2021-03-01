symbol_table = {
    # layers
    'Conv2D': 'model.add(Conv2D())',
    'MaxPooling2D': 'model.add(MaxPooling2D())',
    'Dense': 'model.add(Dense())',
    'Flatten': 'model.add(Flatten())',
    'Dropout': 'model.add(Dropout())',
    'SimpleRNN': 'model.add(SimpleRNN())',
    'ZeroPadding2D': 'model.add(ZeroPadding2D())',
    'AveragePooling2D': 'model.add(AveragePooling2D())',
    'LSTM': 'model.add(LSTM())',
    # optimizers
    'sgd': 'opt = SGD(lr=0.001, momentum=0.9)',
    'rmsprop': 'opt = RMSprop(learning_rate=0.1)',
    'adam': 'opt = Adam(learning_rate=0.1)',
    'adagrad': 'opt = Adagrad(learning_rate=0.001, initial_accumulator_value=0.1, epsilon=1e-07, name="Adagrad")',
    'adadelta': 'opt = Adadelta(learning_rate=0.001, rho=0.95, epsilon=1e-07, name="Adadelta")',
}
