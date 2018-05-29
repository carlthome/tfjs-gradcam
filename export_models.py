import os
import inspect
import tempfile

import tensorflow as tf
import tensorflowjs as tfjs

models = inspect.getmembers(tf.keras.applications, inspect.isfunction)

for model_name, model_fn in models:
    tf.keras.backend.clear_session()
    model = model_fn()
    output_path = os.path.join('models', model_name)
    # TODO Fix FailedPreconditionError
    #tfjs.converters.save_keras_model(model, output_path)
    with tempfile.NamedTemporaryFile() as f:
        model.save(f.name, include_optimizer=False)
        cmd = f'tensorflowjs_converter --input_format keras {f.name} {output_path}'
        os.system(cmd)
