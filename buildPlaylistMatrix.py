#!/usr/bin/env python
# Methods to Create Songs x Playlist Incidence Matrix

import os
import numpy as np
import cPickle as pickle
import random


## returns list of all songs in all playlist indluded in ids?
def getLists(P, ids):

    lists = []

    for x in ids: # for each playlist ID
        #for y in P[x]: # for each song ID? <- This doesnt make sense if we want many lists in lists
        	#lists.append(y)
		lists.append(P[x])
    return lists


def buildSongPlaylistMatrix(filename):
	# The model requires a map of vertex -> edge labels
	playlist_map = {} # playlist ID -> list of songs
	song_map = {} # song ID -> list of playlists

	cwd = os.getcwd()
	with open(os.path.join(cwd, filename)) as f:
		for cnt, line in enumerate(f):
			line = line.rstrip().rstrip(",") # unknown what this does

			try:
				song_id, plists = line.split('\t', 1)
				list_of_plists = [int(t) for t in plists.split(",")]
			except ValueError:
				list_of_plists = ['']


			if len(list_of_plists) == 1 and list_of_plists[0] == '':
				song_map[int(song_id)] = []
				continue
			for p in list_of_plists:
				if p not in playlist_map:
					playlist_map[p] = []
				playlist_map[p].append(int(song_id))
			song_map[int(song_id)] = list_of_plists
		## above code may show more about how data is stored in original code

	all_songs = song_map.keys()
	min_song_number = min(all_songs)
	max_song_number = max(all_songs)
	num_playlists = len(playlist_map.keys())
	num_songs = max_song_number - min_song_number + 1

	song_playlist_matrix = np.zeros([num_songs,num_playlists])

	for pl in playlist_map.keys():
		for s in playlist_map[pl]:
			song_playlist_matrix[s,pl] = 1

	return song_map

"""
Input: txt file of songs IDs -> list of playlists
Output: pickle of fold # X playlist ID X songs (1 for train and 1 for test)
"""
def makeTrainTestData(filename, train_ratio = 0.7, nFolds = 10):
	# Need to split playlist data into train/test
	# Using split 70/30
	# save data as list with index = fold number. Value = map of playlist -> song

	cwd = os.getcwd()
	P = {} # P is map of playlist_id -> list of song_ids

	with open(os.path.join(cwd, filename)) as f:
		for line in f:
			song_id, playlists_str = line.split('\t')
			playlist_list = playlists_str.split(',')
			for plist in playlist_list:
				if plist not in P:
					P[plist] = []
				P[plist].append(song_id)

	lists_train = []
	lists_test = []

	## each fold has its own full set of training and testing data, randomly suffled/split
	for i in xrange(nFolds): # for each fold
		#print("allocating fold i out of i", i, nFolds)
		ids         = P.keys() # playlist IDs?
		random.shuffle(ids)

		n           = len(ids)
		numtrain    = int(n * train_ratio)
		#print("n = , numtrain =",n,numtrain)

		lists_train.append(getLists(P, ids[:numtrain]))
		lists_test.append(getLists(P, ids[numtrain:]))

        pass

	#print(lists_train)

	'''
	with open(os.path.join(cwd, filename)) as f:
		file_length = sum(1 for _ in f)
		train_length = int(0.7 * float(file_length))
		test_length = file_length - train_length

	f.close()

	with open(os.path.join(cwd, filename)) as f:
		for cnt, line in enumerate(f):
			line = line.rstrip().rstrip(",")
			pid, tracks = line.split('\t', 1)
			track_list = [int(t) for t in tracks.split(",")]
			if cnt < train_length:
				playlist_train.append(track_list)
			else:
				playlist_test.append(track_list)

	f.close()
	'''

	input_directory = os.path.join(cwd, "playlist_input")
	if not os.path.exists(input_directory):
		os.mkdir(input_directory)
		print("Made Directory")
	else:
		print("Input directory already exists")

	training_file = os.path.join(input_directory, "playlist_train.pickle")
	testing_file = os.path.join(input_directory, "playlist_test.pickle")

	# Write a pickle containing a list of all the playlists
	# Model expects input list of lists of vertices representing edges
	with open(training_file, 'w') as f:
		pickle.dump(lists_train, f)
	f.close()

	# Write a pickle containing a list of all the playlists
	# Model expects input list of lists of vertices representing edges
	with open(testing_file, 'w') as f:
		pickle.dump(lists_test, f)
	f.close()

	return input_directory
