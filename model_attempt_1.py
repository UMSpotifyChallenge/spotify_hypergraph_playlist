#!/usr/bin/env python2.7

import os
import hypergraph
import evalModel
import buildPlaylistMatrix
import cPickle as pickle

def constructHypergraph(params):

	HG = hypergraph.Hypergraph()

	'''
	## at this point, import all sperate edge sets from different features into this one large hypergraph
	# for all song -> feature  maps that we have pickled
	print("edgelist: ");print(HG.pub_edges)
	with open("feat1map.pickle", 'r') as f:
		print("Adding feature 1 edges...")
		HG.importEdge(pickle.load(f)['X']) # notice you are importing the value of key 'X', which is put in there inside build files for unknown reasons
		pass
	# pass
	print("edgelist: ");print(HG.pub_edges)

	with open("feat2map.pickle", 'r') as f:
		print("Adding feature 2 edges...")
		HG.importEdge(pickle.load(f)['X']) # notice you are importing the value of key 'X', which is put in there inside build files for unknown reasons
		pass
	# pass
	print("edgelist: ");print(HG.pub_edges)

	with open("feat3map.pickle", 'r') as f:
		print("Adding feature 3 edges...")
		HG.importEdge(pickle.load(f)['X']) # notice you are importing the value of key 'X', which is put in there inside build files for unknown reasons
		pass
	# pass
	print("edgelist: ");print(HG.pub_edges)
	'''

	## use this as worst baseline (all songs in 1 edge)
	with open("featALLmap.pickle", 'r') as f:
		print("Adding all songs to 1 edge (anyEdge)...")
		HG.importEdge(pickle.load(f)['X']) # notice you are importing the value of key 'X', which is put in there inside build files for unknown reasons
		pass
	# pass
	print("edgelist: ");print(HG.pub_edges)

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
	params['markov'] = False # def = True
	params['a'] = 0.8 # def = 1.0
	params['lam'] = 1e0 # def = 1e0
	params['DEBUG'] = 0 # def = -1
	params['m'] = 30
	params['val'] = 0.1

	HG = constructHypergraph(params)

	with open(model_name, 'w') as f:
		pickle.dump({'G': HG}, f)

	# Train, Test, and Evaluate the model
	# TODO: call evalModel.processArguments() to automatically handle args
	results = evalModel.evaluateModel(params)
	print(results)

	with open(output_file, 'w') as f:
		pickle.dump(results, f)

	f.close()
