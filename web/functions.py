from web import app
import networkx as nx
import simplejson as json
import networkx.readwrite as json_graph
import os

filepath = os.path.join(app.config['UPLOADS_DEFAULT_DEST']+ 'graph'+ session['filename'][1])

def gmlToNetxOBJ(path, fileName):
    filepath = path + "/" + fileName

    try:
        graph = nx.read_gml(filepath + fileName, label='id')

    except KeyError:

        try:
            graph = nx.read_gml(filepath + fileName)
        except KeyError:
            return -1

    return graph;


def netxObjToJson(graph):
    jsonobj = json_graph.node_link_data(graph)

    return jsonobj


def rewriteFileAsJson(filename, jsonOBj):
    with open(filename, 'w') as fp:
        json.dumps(jsonOBj, fp)

    return


