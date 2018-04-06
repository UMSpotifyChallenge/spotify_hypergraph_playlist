#!/usr/bin/env python
'''
Drew

- Take in a txt (or database) file that shows relationsships between songs and a single feature
- Each row in this file will have format: [song_ID]\t[feat_cat0]
- # colums = # tracks
- Create a python map of song -> feature category
- Save pick of map to feat1.pickle?
Construct a song=>LIST of feature 1 categories

Usage:
./buildFeat1map.py output.pickle input_feature.txt
python2.7 buildFeat1map.py feat1map.pickle Feature1_hypergraph.txt

'''

import sys
import numpy
import cPickle as pickle


def getFeat1Map(feature_file):

    X = {}

    for line in feature_file:
        line = line.rstrip()
        song_id, feat_cat = line.split('\t',1) # split the song ID and the feature category
        ## currently have no song set to use to check for song existance
        #if song_id not in songs:
        #    continue
        X[song_id] = feat_cat.split(',')
        pass
    return X # map of songID (vertex) -> list of vertex edges inside this cat


if __name__ == '__main__':
    #songs = loadSongs(sys.argv[2])
    with open(sys.argv[2]) as feature_file:
        feat1map = getFeat1Map(feature_file)
        pass
    with open(sys.argv[1], 'w') as f:
        ## for unkown reasons OG author pickled a map that has key 'X' which returns value of the entire map we have of this feature
        pickle.dump({'X': feat1map}, f) # save map to pickle
        pass
    pass
