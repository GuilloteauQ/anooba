def cld(tukeyhsd_result):
    groups = tukeyhsd_result.groupsunique
    from functools import reduce
    import networkx as nx
    letters = "abcdefghijklmnopqrstuvxyz"
    c = 0
    graph = {}
    G = nx.Graph()
    labels = {}
    for g in groups:
        graph[g] = [g]
        labels[g] = ""
        G.add_node(g)
    
    for (i, g1) in enumerate(groups):
        for g2 in groups[i+1:]:
            if not tukeyhsd_result.reject[c]:
                graph[g1].append(g2)
                graph[g2].append(g1)
                G.add_edge(g1, g2)
            c += 1
            
    letter_index = 0
    for (k, v) in graph.items():
        neighbors = reduce(lambda x0, x1: x0.intersection(x1), map(lambda x: set(labels[x]), v))
        if len(neighbors) == 0:
            for n in v:
                labels[n] += letters[letter_index]
            letter_index += 1
    
    
    return labels, G