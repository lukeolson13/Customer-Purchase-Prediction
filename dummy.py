import pandas as pd
train_data_update = pd.read_pickle('train_data_update.pkl')
dummy_train_data_update = pd.get_dummies(train_data_update.reset_index(), columns=['j', 'i'])
dummy_train_data_update.to_pickle('dummy_train_data_update.pkl')