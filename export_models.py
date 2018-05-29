import os
import inspect
import tempfile
import multiprocessing

import tensorflow as tf
import tensorflowjs as tfjs


def convert(model_name, model_fn):
    model = model_fn()
    output_path = os.path.join('models', model_name)
    # TODO Fix FailedPreconditionError
    #tfjs.converters.save_keras_model(model, output_path)
    with tempfile.NamedTemporaryFile() as f:
        model.save(f.name, include_optimizer=False)
        cmd = f'tensorflowjs_converter --input_format keras {f.name} {output_path}'
        os.system(cmd)


models = inspect.getmembers(tf.keras.applications, inspect.isfunction)
with multiprocessing.Pool() as pool:
    pool.starmap(convert, models)