import os
import argparse
import _yaml
import logging




if __name__=="__main__":
    ags= argparse.ArgumentParser()
    ags.add_argument("..config",default= "default")
    ags.add_argument("..data source",default=None)

    parsed_args= ags.parse_args()


