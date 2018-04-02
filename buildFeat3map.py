#!/usr/bin/env python
'''
Drew

- Take in a txt (or database) file that shows relationsships between songs and a single feature
- Each row in this file will have format: [song_ID]\t[feat_cat0]
- # colums = # tracks
- Create a python map of song -> feature category
- Save pick of map to feat3.pickle?
Construct a song=>LIST of feature 3 categories

Usage:
./buildFeat3map.py output.pickle input_feature.txt
python2.7 buildFeat3map.py feat3map.pickle Feature3_hypergraph.txt

'''

import sys
import numpy
import cPickle as pickle


def getFeat3Map(feature_file):

    X = {}

    for line in feature_file:
        line = line.rstrip()
        song_id, feat_cat = line.split('\t',1) # split the song ID and the feature category
        ## currently have no song set to use to check for song existance
        #if song_id not in songs:
        #    continue
        X[song_id] = feat_cat.split(',')
        pass
    return X


if __name__ == '__main__':
    #songs = loadSongs(sys.argv[2])
    with open(sys.argv[2]) as feature_file:
        feat3map = getFeat3Map(feature_file)
        pass
    with open(sys.argv[1], 'w') as f:
        ## for unkown reasons OG author pickled a map that has key 'X' which returns value of the entire map we have of this feature
        pickle.dump({'X': feat3map}, f) # save map to pickle
        pass
    pass
