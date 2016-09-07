#!/usr/bin/env python3

__author__ = 'cjm'

import argparse
import logging
import requests
import sys
import os
import rdflib
from rdflib import Namespace
from rdflib.namespace import RDF
from contextlib import closing
from SPARQLWrapper import SPARQLWrapper, JSON
from json import dumps
import yaml


DCTYPES = Namespace('http://purl.org/dc/dcmitype/')



def main():

    parser = argparse.ArgumentParser(description='Datasets ttl to yaml'
                                                 'Helper utils',
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-f', '--format', type=str, required=False, default='turtle',
                        help='Ontology name')

    parser.add_argument('files',nargs='*')


    args = parser.parse_args()

    g = rdflib.Graph()
    for file in args.files:
        g.parse(file, format=args.format)

    process_graph(g, args)
        

def process_graph(g, args):
    for dataset in g.subjects(RDF.type, DCTYPES.Dataset):
        print(str(dataset))
        obj = { 'id' : str(dataset) }
        for (s,p,o) in g.triples(dataset,Null,Null):
            print(str((s,p,o)))
        print(dumps(obj, sort_keys=True, indent=4, separators=(',', ': ')))
            

        

if __name__ == "__main__":
    main()

    
    
