## need the edges to have unique edge_labels
## by default hey just have int from 0-2
## but should have string name

## for the sake of human understandability:
##          feat1 represents dancebility


with open("Feature2_hypergraph.txt", 'r') as inFile, open("id_to_feat2.txt", 'w') as outFile:
    for line in inFile:
        line = line.strip()
        songID, edgeFeatNum = line.split('\t')
        if edgeFeatNum == '0':
            edgeName = "dance_lvl_1"
        elif edgeFeatNum == '1':
            edgeName = "dance_lvl_2"
        elif edgeFeatNum == '2':
            edgeName = "dance_lvl_3"
        outFile.write(songID +'\t' + edgeName + '\n')
        pass
    pass
