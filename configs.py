import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", default='large')
    args = parser.parse_args()
    return args
