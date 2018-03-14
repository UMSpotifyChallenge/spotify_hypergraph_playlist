#!/usr/bin/env python2.7

import os
import hypergraph
import evalModel
import buildPlaylistMatrix
import cPickle as pickle

if __name__ == '__main__':
	filename = "hypergraph.txt"
	model_name = os.path.join(os.getcwd(), "base_model.pickle")
	output_file = os.path.join(os.getcwd(), "output_base_model")

	song_playlist_map = buildPlaylistMatrix.buildSongPlaylistMatrix(filename)
	playlist_directory = buildPlaylistMatrix.makeTrainTestData(filename)

	HG = hypergraph.Hypergraph()
	# Very easy to import edges as long as they are of form vertex -> edges
	HG.importEdge(song_playlist_map)

	with open(model_name, 'w') as f:
		pickle.dump({'G': HG}, f)

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
	params['val'] = 0.0

	# Train, Test, and Evaluate the model
	results = evalModel.evaluateModel(params)

	with open(output_file, 'w') as f:
		pickle.dump(results, f)

	f.close()




