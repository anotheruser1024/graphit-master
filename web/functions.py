from web import app
import networkx as nx
import simplejson as json #https://simplejson.readthedocs.io/en/latest/#basic-usage
import networkx.readwrite as json_graph
from networkx.exception import NetworkXError
import os

filepath = os.path.join(app.config['UPLOADS_DEFAULT_DEST']+ 'graph'+ session['filename'][1])

def gmlToNetxOBJ(path, fileName):
    filepath = path + "/" + fileName

    try:
        graph = nx.read_gml(filepath + fileName, label='id')
        return graph

    except NetworkXError:
        print({{NetworkXError}})
        try:
            graph = nx.read_gml(filepath + '/' + fileName)
            return graph
        except NetworkXError:
            print([{NetworkXError}])



def netxObjToJson(graph):
    try:
        jsonobj = json_graph.node_link_data(graph)
        return jsonobj
    except NetworkXError:
        print({ NetworkXError})
        return -1



def rewriteFileAsJson(filename, jsonOBj):
    with open(filename, 'w') as fp:
        json.dumps(jsonOBj, fp)

    return


