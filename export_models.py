import os
import inspect

import tensorflow as tf
import tensorflowjs as tfjs

models = inspect.getmembers(tf.keras.applications, inspect.isfunction)
for model_name, model_fn in models:
    try:
        tf.keras.backend.clear_session()
        model = model_fn()
        model.compile('sgd', 'categorical_crossentropy')
        output_path = os.path.join('models', model_name)
        tfjs.converters.save_keras_model(model, output_path)
    except Exception as ex:
        print(f'{model_name} could not be converted.', ex)
