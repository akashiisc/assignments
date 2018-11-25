import sys
import random
import networkx
import tkinter
import matplotlib
import matplotlib.pyplot as plt
import queue as queue
import math
import numpy

#from eigen_values_vector  import *
from myqr import * 
from helping_functions import *

def plot_graph(apni_map , toFile , filePath):
    x_coordinates = []
    y_coordinates = []
    for key in sorted(apni_map):
        x_coordinates.append(key)
        y_coordinates.append(apni_map[key])
    # print(x_coordinates)
    # print(y_coordinates)
    plt.figure()
    plt.plot(x_coordinates, y_coordinates) 
    plt.xlabel('Degree')
    plt.ylabel('Probability')
    plt.title('Degree distribution')
    # function to show the plot
    if True == toFile:
        plt.savefig(filePath)
    else :
        plt.show() 

def plot_histogram(distibution_values , toFile , filePath):
    x = []
    for i in distibution_values:
        for j in range(distibution_values[i]):
            x.append(i)
    plt.hist(x)
    plt.ylabel("Frequency")
    plt.ylabel("Degree Centrality")
    if True == toFile:
        plt.savefig(filePath)
    else:
        plt.show()


def generate_probabilistic(apni_map , total):
    probablistic_distrubution = {};
    for key in apni_map:
        probablistic_distrubution[key] = apni_map[key]/total
    return probablistic_distrubution

def convert_nodes_degree_to_degree_counts(map_nodes_degree):
    degree_counts = {}
    # print(map_nodes_degree)
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
                if t not in shortest_path_length:
                    shortest_path_length[t] = shortest_path_length[x] + 1
                    q.append(t)
                    for u in shortest_paths[x]:
                        m = u.copy()
                        m.append(t)
                        shortest_paths[t].append(m)
                elif shortest_path_length[t] == shortest_path_length[x] + 1:
                    for u in shortest_paths[x]:
                        m = u.copy()
                        m.append(t)
                        shortest_paths[t].append(m)
            # elif True == visited[t] and (shortest_path_length[t] == (shortest_path_length[x] + 1)):
            #     for u in shortest_paths[x]:
            #         m = u.copy()
            #         m.append(t)
            #         shortest_paths[t].append(m)
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

def create_eigen_value_eigen_matrix_pair(eigen_values , eigen_vectors):
    eigen_vectors_transpose = np.array(eigen_vectors).transpose()
    dictOfEigenValues = { i : eigen_values[i] for i in range(0, len(eigen_values) ) }
    dictOfEigenVectors = { i : eigen_vectors_transpose[i].transpose() for i in range(0, len(eigen_vectors_transpose) ) }
    return dictOfEigenValues , dictOfEigenVectors


def clusterize_by_second_min_eigen_vector(vector):
    cluster1 = []
    cluster2 = []
    for i in range(len(vector)):
        if(vector[i]>0) : 
            cluster1.append(str(i+1))
        else :
            cluster2.append(str(i+1))
    return cluster1 , cluster2
def plot_coloured_graph(G , cluster1 , cluster2 , write_to_file , filePath):
    #networkx.draw(G)
    plt.figure()
    pos = networkx.spring_layout(G)
    networkx.draw_networkx_nodes(G,pos,
                       nodelist=cluster1,
                       node_color='r',
                       node_size=500,
                   alpha=0.8)
    networkx.draw_networkx_nodes(G,pos,
                       nodelist=cluster2,
                       node_color='b',
                       node_size=500,
                   alpha=0.8)
    networkx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)

    if True == write_to_file :
        plt.savefig(filePath)
    else :
        plt.show()

def variance_of_clusters(second_min_eigen_vector , cluster1 , cluster2):
    sum_cluster_1 = 0
    for x in cluster1:
        sum_cluster_1 = sum_cluster_1 + second_min_eigen_vector[int(x) - 1]
    mean_cluster_1 = sum_cluster_1 / len(cluster1)
    sum_cluster_2 = 0
    for x in cluster2:
        sum_cluster_2 = sum_cluster_2 + second_min_eigen_vector[int(x) - 1]
    mean_cluster_2 = sum_cluster_2 / len(cluster2)

    sum_square_mean_cluster_1 = 0
    for x in cluster1:
        sum_square_mean_cluster_1 = sum_square_mean_cluster_1 + (second_min_eigen_vector[int(x) - 1] - mean_cluster_1)**2
    variance_cluster_1 = sum_square_mean_cluster_1 / len(cluster1)

    sum_square_mean_cluster_2 = 0
    for x in cluster2:
        sum_square_mean_cluster_2 = sum_square_mean_cluster_2 + (
                    second_min_eigen_vector[int(x) - 1] - mean_cluster_2) ** 2
    variance_cluster_2 = sum_square_mean_cluster_2 / len(cluster2)

    return variance_cluster_1 , variance_cluster_2

def carry_out_works(graph):
    file_to_write = open(output_file_path , 'w')
    nodes = graph.nodes
    edges = graph.edges
    #print(edges)
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
    #print(degree_distribution_values)
    plot_histogram(degree_distribution_values , True , output_plot_dir+"problem_1_task_2.png")
    #print(indegree_distribution_values)
    #print(outdegree_distribution_values)
    #print(degree_distribution_values)
    #sorted(mydict.iteritems(), key=lambda (k,v): (v,k))
    #indegree_probabilistic = generate_probabilistic(indegree_distribution_values , len(nodes))
    #outdegree_probabilistic = generate_probabilistic(outdegree_distribution_values , len(nodes))
    degree_probabilistic = generate_probabilistic(degree_distribution_values , len(nodes))
    plot_graph(degree_probabilistic , True , output_plot_dir+"problem_1_task_1.png")
    #print(degree_probabilistic)
    degree_centrality = calculate_degree_centrality(map_degree_nodes , len(nodes))
    #print(degree_centrality)
    edge_centrality = calculate_edge_centrality(g)
    #print(edge_centrality)
    print_beautifully(edge_centrality , 'Edge Centrality' , 'Edge' , 'Centrality' , True , file_to_write , "map")
    x = [(k, edge_centrality[k]) for k in sorted(edge_centrality, key=edge_centrality.get)]
    #print(x)
    most_central_edge = get_most_central_edge(edge_centrality)
    file_to_write.write("Most Central Edge : (" +  str(most_central_edge[0]) + " , " + str(most_central_edge[1]) + ") \n") 
    print_barrier(file_to_write)
    # print(networkx.edge_betweenness_centrality(graph))
    # print(graph.edges)
    adjacency_matrix = create_adjacency_matrix(g)
    #print(adjacency_matrix)
    laplacian_matrix = create_laplacian_matrix(adjacency_matrix , create_degree_matrix(g , map_degree_nodes))
    print_beautifully_matrix(laplacian_matrix , file_to_write , "Laplacian matrix")
    #print(laplacian_matrix)
    normalized_laplacian_matrix = create_normalized_laplacian_matrix(map_degree_nodes , adjacency_matrix)
    print_beautifully_matrix(normalized_laplacian_matrix , file_to_write , "Normalized Laplacian matrix")
    #print(normalized_laplacian_matrix)
    #eigen_values = find_eigen_values(laplacian_matrix)
    #print(eigen_values)
    # eigen_values , eigen_vector = numpy.linalg.eig(laplacian_matrix)
    # print("Numpy eigen values")
    # print(eigen_values)
    # print(eigen_vector)
    eigen_values_my , eigen_vector_my = eig_by_qr(laplacian_matrix)
    no_of_complex_entries = check_complex(eigen_values_my)
    print_barrier(file_to_write)
    if no_of_complex_entries == 0 :
        file_to_write.write("No Complex Eigen Values found\n")
    else : 
        file_to_write.write(str(no_of_complex_entries) + "Complex Eigen Values found\n")
    print_barrier(file_to_write)
    print_beautifully(eigen_values_my , 'Eigen Values' , '' , '' , True , file_to_write , "list")
    print_beautifully(eigen_vector_my , 'Eigen Vectors' , '' , '' , True , file_to_write , "list_of_list")
    
    eigen_value_map , eigen_vector_map = create_eigen_value_eigen_matrix_pair(eigen_values_my , eigen_vector_my)
    eigen_value_map_sorted = [(k, eigen_value_map[k]) for k in sorted(eigen_value_map, key=eigen_value_map.get)]
    min_eigen_val = eigen_value_map_sorted[0]
    min_eigen_vector = eigen_vector_map[min_eigen_val[0]]
    second_min_eigen_val = eigen_value_map_sorted[1]
    second_min_eigen_vector = eigen_vector_map[second_min_eigen_val[0]]
    print_beautifully(min_eigen_val[1] , 'Min Eigen Value' , '' , '' , True , file_to_write , "string")
    print_beautifully(min_eigen_vector , 'Min Eigen Vector' , '' , '' , True , file_to_write , "list")
    print_beautifully(second_min_eigen_val[1] , 'Second Min Eigen Value' , '' , '' , True , file_to_write , "string")
    print_beautifully(second_min_eigen_vector , 'Second Min Eigen Vector' , '' , '' , True , file_to_write , "list")
    
    # print(min_eigen_val)
    # print(second_min_eigen_val)
    # print(min_eigen_vector)
    # print(second_min_eigen_vector)

    cluster1 , cluster2 = clusterize_by_second_min_eigen_vector(second_min_eigen_vector)
    plot_coloured_graph(graph , cluster1 , cluster2 , True , output_plot_dir+"problem_1_task_6.png")

    print_vspace(file_to_write)
    print_barrier(file_to_write)
    write_string_to_file(file_to_write, "Task VII")
    print_barrier(file_to_write)
    var_cluster_1 , var_cluster_2 = variance_of_clusters(second_min_eigen_vector , cluster1 , cluster2)
    if var_cluster_1 > var_cluster_2 :
        write_string_to_file(file_to_write , "Red house would be chosen to make friends with.")
    else :
        write_string_to_file(file_to_write, "Blue house would be chosen to make friends with.")
    print_barrier(file_to_write)


    # carry_out_works_using_numpy #
    eigen_values_np , eigen_vectors_np = np.linalg.eig(laplacian_matrix)
    print_vspace(file_to_write)
    print_barrier(file_to_write)
    file_to_write.write("Bonus 1\n")
    print_barrier(file_to_write)
    eigen_value_map , eigen_vector_map = create_eigen_value_eigen_matrix_pair(eigen_values_np , eigen_vectors_np)
    eigen_value_map_sorted = [(k, eigen_value_map[k]) for k in sorted(eigen_value_map, key=eigen_value_map.get)]
    min_eigen_val = eigen_value_map_sorted[0]
    min_eigen_vector = eigen_vector_map[min_eigen_val[0]]
    second_min_eigen_val = eigen_value_map_sorted[1]
    second_min_eigen_vector = eigen_vector_map[second_min_eigen_val[0]]
    print_beautifully(min_eigen_val[1] , 'Min Eigen Value' , '' , '' , True , file_to_write , "string")
    print_beautifully(min_eigen_vector , 'Min Eigen Vector' , '' , '' , True , file_to_write , "list")
    print_beautifully(second_min_eigen_val[1] , 'Second Min Eigen Value' , '' , '' , True , file_to_write , "string")
    print_beautifully(second_min_eigen_vector , 'Second Min Eigen Vector' , '' , '' , True , file_to_write , "list")
    print_barrier(file_to_write)
    cluster1 , cluster2 = clusterize_by_second_min_eigen_vector(second_min_eigen_vector)
    plot_coloured_graph(graph , cluster1 , cluster2 , True , output_plot_dir+"problem_1_bonus_1.png")    
    print_vspace(file_to_write)
    print_barrier(file_to_write)
    file_to_write.write("Bonus 3\n")
    print_barrier(file_to_write)
    print_barrier(file_to_write)
    eigen_value_map , eigen_vector_map = create_eigen_value_eigen_matrix_pair(eigen_values_np , eigen_vectors_np)
    eigen_value_map_sorted = [(k, eigen_value_map[k]) for k in sorted(eigen_value_map, key=eigen_value_map.get , reverse=True)]
    max_eigen_val = eigen_value_map_sorted[0]
    max_eigen_vector = eigen_vector_map[max_eigen_val[0]]
    second_max_eigen_val = eigen_value_map_sorted[1]
    second_max_eigen_vector = eigen_vector_map[second_max_eigen_val[0]]
    print_beautifully(max_eigen_val[1] , 'Max Eigen Value' , '' , '' , True , file_to_write , "string")
    print_beautifully(max_eigen_vector , 'Max Eigen Vector' , '' , '' , True , file_to_write , "list")
    print_beautifully(second_max_eigen_val[1] , 'Second Max Eigen Value' , '' , '' , True , file_to_write , "string")
    print_beautifully(second_max_eigen_vector , 'Second Max Eigen Vector' , '' , '' , True , file_to_write , "list")
    print_barrier(file_to_write)
    cluster1 , cluster2 = clusterize_by_second_min_eigen_vector(second_max_eigen_vector)
    plot_coloured_graph(graph , cluster1 , cluster2 , True , output_plot_dir+"problem_1_bonus_3.png") 
    exit()

output_plot_dir = "./output_plots/"
output_file_path = "./output_data/output_problem1.txt"
file_name_for_input = sys.argv[1]
print(file_name_for_input)
g = networkx.read_gml(file_name_for_input)
carry_out_works(g);
