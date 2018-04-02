## need the edges to have unique edge_labels
## by default hey just have int from 0-2
## but should have string name

## for the sake of human understandability:
##          featALL represents all songs (they are all inside of one edge)


with open("FeatureALL_hypergraph.txt", 'r') as inFile, open("id_to_featALL.txt", 'w') as outFile:
    songSet = set()
    for line in inFile:
        line = line.strip()
        songID, edgeFeatNum = line.split('\t')
        if songID not in songSet:
            songSet.add(songID)
            edgeName = "AnySong"
            outFile.write(songID +'\t' + edgeName + '\n')
            pass
    pass
