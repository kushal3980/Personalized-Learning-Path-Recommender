import networkx as nx
from skill_graph import build_skill_graph

def recommend_path(current_skills, target_skill):
    G = build_skill_graph()
    paths = []

    for skill in current_skills:
        try:
            path = nx.shortest_path(G, source=skill, target=target_skill)
            paths.append(path)
        except nx.NetworkXNoPath:
            continue
        except nx.NodeNotFound:
            continue

    if paths:
        # Return the shortest path found
        return min(paths, key=len)
    else:
        return [target_skill]  # Fallback: just show the target skill
