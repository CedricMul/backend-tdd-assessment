#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "Cedric Mulvihill"


import sys
import argparse

'''Test'''
def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--upper', help='convert to uppercase')
    parser.add_argument('-l', '--lower', help='convert to lowercase')
    parser.add_argument('-t', '--title', help='convert to titlecase')
    
    parser.add_argument('text', help='text to be entered')
    return parser


def main(args):
    """Implementation of echo"""
    if not args:
        print(args.usage)
    parser = create_parser()
    args = parser.parse_args(args)
    if args.upper:
        return(args.upper.upper())
    elif args.lower:
        return(args.lower.lower())
    elif args.title:
        print(args.title.title())
        return(args.title.title())
    #print(text)


if __name__ == '__main__':
    main(sys.argv[1:])
