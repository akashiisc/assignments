import sys
import random
import networkx
import tkinter
import matplotlib.pyplot as plt

def plot_graph(apni_map):
    x_coordinates = []
    y_coordinates = []
    for key in sorted(apni_map):
        x_coordinates.append(key)
        y_coordinates.append(apni_map[key])
    print(x_coordinates)
    print(y_coordinates)
    plt.plot(x_coordinates, y_coordinates) 
    plt.xlabel('Degree')
    plt.ylabel('Probability')
    plt.title('Degree distribution')
    # function to show the plot
    plt.show() 

def generate_probabilistic(apni_map , total):
    probablistic_distrubution = {};
    for key in apni_map:
        probablistic_distrubution[key] = apni_map[key]/total
    return probablistic_distrubution

def convert_nodes_degree_to_degree_counts(map_nodes_degree):
    degree_counts = {}
    print(map_nodes_degree)
    for key in map_nodes_degree:
        value = map_nodes_degree[key]
        if value in degree_counts:
            degree_counts[value] = degree_counts[value] + 1
        else :
            degree_counts[value] = 1
    return degree_counts

def calculate_degree_centrality(map_nodes_degree , no_of_nodes):
    degree_centrality = {}
    for key in map_nodes_degree:
        degree_centrality[key] = map_nodes_degree[key]/(no_of_nodes-1)
    return degree_centrality

def plot_degree_distribution(graph):
    nodes = graph.nodes
    edges = graph.edges
    print(edges)
    #map_degree_nodes_indegree = {}
    #map_degree_nodes_outdegree = {}
    map_degree_nodes = {}
    total_outdegree = 0
    total_indegree = 0
    for i in nodes:
        #map_degree_nodes_indegree[i] = 0
        map_degree_nodes[i] = 0
        #map_degree_nodes_outdegree[i] = 0
    for (i,j) in edges:
        map_degree_nodes[i] = map_degree_nodes[i] + 1
        map_degree_nodes[j] = map_degree_nodes[j] + 1
        #map_degree_nodes_indegree[j] = map_degree_nodes_indegree[j] + 1
        #map_degree_nodes_outdegree[i] = map_degree_nodes_outdegree[i] + 1
        #total_outdegree = total_outdegree + 1
        #total_indegree = total_indegree + 1
    #indegree_distribution_values = convert_nodes_degree_to_degree_counts(map_degree_nodes_indegree)
    #outdegree_distribution_values = convert_nodes_degree_to_degree_counts(map_degree_nodes_outdegree)
    degree_distribution_values = convert_nodes_degree_to_degree_counts(map_degree_nodes)
    #print(indegree_distribution_values)
    #print(outdegree_distribution_values)
    print(degree_distribution_values)
    #sorted(mydict.iteritems(), key=lambda (k,v): (v,k))
    #indegree_probabilistic = generate_probabilistic(indegree_distribution_values , len(nodes))
    #outdegree_probabilistic = generate_probabilistic(outdegree_distribution_values , len(nodes))
    degree_probabilistic = generate_probabilistic(degree_distribution_values , len(nodes))
    plot_graph(degree_probabilistic)
    #print(degree_probabilistic)
    degree_centrality = calculate_degree_centrality(map_degree_nodes , len(nodes))
    print(degree_centrality)
    #print(outdegree_probabilistic)
    #plot_graph(indegree_probabilistic)
    #plot_graph(outdegree_probabilistic)
    #plot_graph(degree_probabilistic)
    exit()

file_name_for_input = sys.argv[1]
print(file_name_for_input)
g = networkx.read_gml(file_name_for_input)
plot_degree_distribution(g);
