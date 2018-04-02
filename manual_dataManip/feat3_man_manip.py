## need the edges to have unique edge_labels
## by default hey just have int from 0-2
## but should have string name

## for the sake of human understandability:
##          feat1 represents popularity


with open("Feature3_hypergraph.txt", 'r') as inFile, open("id_to_feat3.txt", 'w') as outFile:
    for line in inFile:
        line = line.strip()
        songID, edgeFeatNum = line.split('\t')
        if edgeFeatNum == '0':
            edgeName = "NOTpopular"
        elif edgeFeatNum == '1':
            edgeName = "LOWpopular"
        elif edgeFeatNum == '2':
            edgeName = "MIDpopular"
        elif edgeFeatNum == '3':
            edgeName = "HIGHpopular"
        outFile.write(songID +'\t' + edgeName + '\n')
        pass
    pass
