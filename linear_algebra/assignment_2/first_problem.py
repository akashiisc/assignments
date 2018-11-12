import sys
import random
import networkx
import tkinter
import matplotlib.pyplot as plt
import queue as queue
import math
from eigen_values_vector  import *


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

def bfs_modified(adj_list , i , nodes):
    shortest_paths = {}
    shortest_path_length = {}
    for j in nodes:
        shortest_paths[j] = []
    shortest_paths[i] = [[i]]
    shortest_path_length[i] = 0
    #q = queue.Queue()
    q = []
    #q.put(i)
    q.append(i)
    visited = {}
    visited_from = {}
    for k in g.nodes:
        visited[k] = False
    while len(q) != 0 :
        #x = q.get()
        x = q[0]
        q.pop(0)
        visited[x] = True
        for t in adj_list[x]:
            if False == visited[t]:
                #q.put(t)
                q.append(t)
                if t not in shortest_path_length:
                    shortest_path_length[t] = shortest_path_length[x] + 1
                    for u in shortest_paths[x]:
                        m = u.copy()
                        m.append(t)
                        shortest_paths[t].append(m)
            elif True == visited[t] and (shortest_path_length[t] == (shortest_path_length[x] + 1)):
                for u in shortest_paths[x]:
                    m = u.copy()
                    m.append(t)
                    shortest_paths[t].append(m)
    return shortest_paths

def calculate_edge_centrality(g):
    edge_centrality = {}
    adj_list = {}
    for i in g.nodes:
        adj_list[i] = []
    for (i,j) in g.edges:
        adj_list[i].append(j)
        adj_list[j].append(i)
    shortest_paths = {}
    for i in g.nodes:
        shortest_paths[i] = bfs_modified(adj_list , i , g.nodes)
    for key in shortest_paths:
        for key_destination in shortest_paths[key]:
            for x in shortest_paths[key][key_destination]:
                prev_path = -1
                for y in x:
                    if prev_path != -1:
                        key_elem = [prev_path , y]
                        key_elem.sort()
                        ele_1 = key_elem[0]
                        ele_2 = key_elem[1]
                        key_elemen_generated = str(ele_1) + "-" + str(ele_2)
                        if key_elemen_generated in edge_centrality:
                            edge_centrality[key_elemen_generated] = edge_centrality[key_elemen_generated] + 1
                        else :
                            edge_centrality[key_elemen_generated] = 1
                    prev_path = y
    return edge_centrality

def get_most_central_edge(edge_centrality):
    max_element = 0
    central_edge = "";
    for x in edge_centrality:
        if edge_centrality[x] > max_element:
            max_element = edge_centrality[x]
            central_edge = x;
    return [ int(x) for x in central_edge.split("-")]

def create_adjacency_matrix(g):
    # Initialize AM
    am = []
    for x in g.nodes:
        am_row = []
        for x in g.nodes:
            am_row.append(0)
        am.append(am_row)
    ###############
    # Put values  #
    ###############
    for (i,j) in g.edges:
        am[int(i)-1][int(j)-1] = 1
        am[int(j)-1][int(i)-1] = 1
    return am

def create_degree_matrix( g , degree_map) :
    dm = []
    for i in g.nodes():
        dm_row = []
        for i in g.nodes():
            dm_row.append(0)
        dm.append(dm_row)
    for i in degree_map:
        dm[int(i)-1][int(i)-1]=degree_map[i]
    return dm

def create_laplacian_matrix(adjacency_matrix , degree_matrix):
    lm = []
    for i in range(len(adjacency_matrix)):
        lm_row = []
        for j in range(len(adjacency_matrix)):
            lm_row.append(degree_matrix[i][j] - adjacency_matrix[i][j])
        lm.append(lm_row)
    return lm
            
def create_normalized_laplacian_matrix(map_degree_nodes , adjacency_matrix):
    nlm = []
    for i in range(len(adjacency_matrix)):
        nlm_row = []
        for j in range(len(adjacency_matrix)):
            if i==j and map_degree_nodes[str(i+1)] != 0 :
                nlm_row.append(1)
            elif i!=j and adjacency_matrix[i][j] == 1:
                nlm_row.append(-1/math.sqrt(map_degree_nodes[str(i+1)]*map_degree_nodes[str(j+1)]))
            else:
                nlm_row.append(0)
        nlm.append(nlm_row)
    return nlm

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
    edge_centrality = calculate_edge_centrality(g)
    print(edge_centrality)
    most_central_edge = get_most_central_edge(edge_centrality)
    print(most_central_edge)
    adjacency_matrix = create_adjacency_matrix(g)
    print(adjacency_matrix)
    laplacian_matrix = create_laplacian_matrix(adjacency_matrix , create_degree_matrix(g , map_degree_nodes))
    print(laplacian_matrix)
    normalized_laplacian_matrix = create_normalized_laplacian_matrix(map_degree_nodes , adjacency_matrix)
    print(normalized_laplacian_matrix)
    eigen_values = find_eigen_values(laplacian_matrix)
    print(eigen_values)
    eigen_vectors = find_eigen_vectors(laplacian_matrix , eigen_values)
    print(eigen_vectors)    
    #print(outdegree_probabilistic)
    #plot_graph(indegree_probabilistic)
    #plot_graph(outdegree_probabilistic)
    #plot_graph(degree_probabilistic)
    exit()

file_name_for_input = sys.argv[1]
print(file_name_for_input)
g = networkx.read_gml(file_name_for_input)
plot_degree_distribution(g);
