find . -name '*.h5' | parallel 'tensorflowjs_converter --input_format keras {} models/`basename {} .h5`'
ls models > models.csv