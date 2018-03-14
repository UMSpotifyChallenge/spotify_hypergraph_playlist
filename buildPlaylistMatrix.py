#!/usr/bin/env python
# Methods to Create Songs x Playlist Incidence Matrix

import os
import numpy as np
import cPickle as pickle

def buildSongPlaylistMatrix(filename):
	# The model requires a map of vertex -> edge labels
	playlist_map = {}
	song_map = {}

	cwd = os.getcwd()
	with open(os.path.join(cwd, filename)) as f:
		for cnt, line in enumerate(f):
			line = line.rstrip().rstrip(",")
			pid, tracks = line.split('\t', 1)
			track_list = [int(t) for t in tracks.split(",")]
			playlist_map[int(pid)] = track_list
			for track in track_list:
				if track not in song_map:
					song_map[track] = []
				song_map[track].append(pid)

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

def makeTrainTestData(filename):
	# Need to split playlist data into train/test
	# Using split 70/30

	playlist_train = []
	playlist_test = []

	cwd = os.getcwd()
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

	input_directory = os.path.join(cwd, "playlist_input")
	if not os.path.exists(input_directory):
		os.mkdir(input_directory)
		print("Made Directory")
	else:
		print("Already Exists")

	training_file = os.path.join(input_directory, "playlist_train.pickle")
	testing_file = os.path.join(input_directory, "playlist_test.pickle")

	# Write a pickle containing a list of all the playlists
	# Model expects input list of lists of vertices representing edges
	with open(training_file, 'w') as f:
		pickle.dump(playlist_train, f)
	f.close()

	# Write a pickle containing a list of all the playlists
	# Model expects input list of lists of vertices representing edges
	with open(testing_file, 'w') as f:
		pickle.dump(playlist_test, f)
	f.close()

	return input_directory





