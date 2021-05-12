import os
import argparse
import yaml
import logging


def read_params(config_path):
    with open(config_path) as yaml_file:
        config= yaml.safe_load(yaml_file)
    return config


def main(config_path, data_source):
    config= read_params(config_path)
    print(config)




if __name__=="__main__":
    ags= argparse.ArgumentParser()
    default_config_file= os.path.join("config", "params.yaml")
    ags.add_argument("--config",default= default_config_file)
    ags.add_argument("--datasource",default=None)

    parsed_args= ags.parse_args()
    main(config_path= parsed_args.config, data_source= parsed_args.datasource)


