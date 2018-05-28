import inspect

import tensorflow as tf

models = inspect.getmembers(tf.keras.applications, inspect.isfunction)

for model_name, model_fn in models:
    tf.keras.backend.clear_session()
    model = model_fn()
    model.save(model_name + '.h5', include_optimizer=False)