import argparse

def argsParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c','--command',help='john command')
    return parser.parse_args()
