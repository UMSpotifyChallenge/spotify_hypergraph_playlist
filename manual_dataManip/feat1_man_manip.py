## need the edges to have unique edge_labels
## by default hey just have int from 0-5 or something
## but should have string name

## for the sake of human understandability:
##          feat1 represents decade


with open("Feature1_hypergraph.txt", 'r') as inFile, open("id_to_feat1.txt", 'w') as outFile:
    for line in inFile:
        line = line.strip()
        songID, edgeFeatNum = line.split('\t')
        if edgeFeatNum == '0':
            edgeName = "60s"
        elif edgeFeatNum == '1':
            edgeName = "70s"
        elif edgeFeatNum == '2':
            edgeName = "80s"
        elif edgeFeatNum == '3':
            edgeName = "90s"
        outFile.write(songID +'\t' + edgeName + '\n')
        pass
    pass
