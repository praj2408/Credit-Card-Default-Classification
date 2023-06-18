# read params
# process
# return dataframe


# %%
import pandas as pd
import yaml
import os
import argparse


#%%
def read_params(config_path):
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
        return config


def get_data(config_path):
    config = read_params(config_path)
    data_path = config["data_source"]["s3_source"]
    df = pd.read_csv(data_path)
    return df



if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='params.yaml')
    parsed_args = args.parse_args()
    get_data(config_path=parsed_args.config)
# %%
