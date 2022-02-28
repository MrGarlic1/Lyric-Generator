import os
import keras
from textgenrnn import textgenrnn

model_cfg = {
    'rnn_size': 256,
    'rnn_layers': 6,
    'rnn_bidirectional': True,
    'max_length': 40,
    'max_words': 10000,
    'dim_embeddings': 100,
    'word_level': False
}

train_cfg = {
    'line_delimited': True,
    'num_epochs': 7,
    'gen_epochs': 2,
    'batch_size': 1024,
    'train_size': 0.8,
    'dropout': 0.0,
    'max_gen_length': 100,
    'validation': False,
    'is_csv': False
}

print('Configured.')

textgen = textgenrnn(name='output_lyrics')

train_function = textgen.train_from_file

train_function(
    file_path='Filtered_Lyrics.txt',
    new_model=True,
    num_epochs=train_cfg['num_epochs'],
    gen_epochs=train_cfg['gen_epochs'],
    batch_size=train_cfg['batch_size'],
    train_size=train_cfg['train_size'],
    dropout=train_cfg['dropout'],
    max_gen_length=train_cfg['max_gen_length'],
    validation=train_cfg['validation'],
    is_csv=train_cfg['is_csv'],
    rnn_layers=model_cfg['rnn_layers'],
    rnn_size=model_cfg['rnn_size']
)

textgen.generate_to_file('Generated_Lyrics.txt', n=100)
