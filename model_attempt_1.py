#!/usr/bin/env python2.7

import os
import hypergraph
import evalModel
import buildPlaylistMatrix
import cPickle as pickle

def constructHypergraph(params):

	HG = hypergraph.Hypergraph()

	## at this point, import all sperate edge sets from different features into this one large hypergraph
	# for all song -> feature  maps that we have pickled
	with open("feat1map.pickle", 'r') as f:
		#print(pickle.load(f)['X'])
		HG.importEdge(pickle.load(f)['X']) # notice you are importing the value of key 'X', which is put in there inside build files for unknown reasons
		pass
	# pass

	# TODO: prune edges if edge is less than min edge size

	# TODO: Use quadratic edge expansion?

	return HG


if __name__ == '__main__':
	filename = "Track_playlistList.txt"
	model_name = os.path.join(os.getcwd(), "pickled_HG.pickle")
	output_file = os.path.join(os.getcwd(), "output_base_model")

	song_playlist_map = buildPlaylistMatrix.buildSongPlaylistMatrix(filename)
	playlist_directory = buildPlaylistMatrix.makeTrainTestData(filename)

	# Model Params... Just using default values given in model
	params = {}
	params['model_in'] = model_name
	params['playlist_dir'] = playlist_directory
	params['results_out'] = output_file
	params['weighted'] = True
	params['markov'] = True
	params['a'] = 1.0
	params['lam'] = 1e0
	params['DEBUG'] = -1
	params['m'] = 30
	params['val'] = 0.1

	HG = constructHypergraph(params)

	with open(model_name, 'w') as f:
		pickle.dump({'G': HG}, f)

	# Train, Test, and Evaluate the model
	# TODO: call evalModel.processArguments() to automatically handle args
	results = evalModel.evaluateModel(params)

	with open(output_file, 'w') as f:
		pickle.dump(results, f)

	f.close()
