import json
import h5py
from tensorflow import keras as keras

f = h5py.File('C:/Users/durve/OneDrive/Desktop/Mini Project/Model/keras_model.h5', 'r')


model = keras.models.load_model('C:/Users/durve/OneDrive/Desktop/Mini Project/Model/keras_model.h5')
model.summary()


weights = model.get_weights()

for w in weights:
    print(w.shape)


input_shape = model.layers[0].input_shape
num_inputs = input_shape[1] if isinstance(input_shape, tuple) else input_shape[0]
print(f'Number of inputs: {num_inputs}')



with h5py.File('C:/Users/durve/OneDrive/Desktop/Mini Project/Model/keras_model.h5', 'r') as f:
    model_config = f.attrs.get('model_config')
    if model_config is None:
        raise ValueError('No model found in h5 file.')
    else:
        model_config = json.loads(model_config)
        layer_configs = model_config['config']['layers']

    for layer in layer_configs:
        # Get layer name, or use a default name if not present
        layer_name = layer.get('name', f'{layer["class_name"]}_{layer.get("batch_input_shape", layer.get("batch_shape"))}')

        layer_type = layer['class_name']
        layer_config = layer['config']
        
        # Print layer name, type, and config
        print(f'Layer name: {layer_name}')
        print(f'Layer type: {layer_type}')
        print(f'Layer config: {layer_config}')
