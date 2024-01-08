from bigtree import *

dict = {
    "a": {"name": "A"},
    "a/b": {"name": "B"},
    "a/g": {"name": "G"},
    "a/b/c": {"name": "C"},
    "a/b/d": {"name": "D"},
    "a/b/d/e": {"name": "E"},
    "a/b/d/e/f": {"name": "F"},
    "a/g/h": {"name": "H"},
    "a/g/h/i": {"name": "I"},
    "a/g/h/j": {"name": "J"},
    "a/g/h/j/l": {"name": "L"},
    "a/g/h/k": {"name": "K"},
    "a/g/h/k/m": {"name": "M"}

}

created_nodes = {"a": Node("A", data=dict["a"])}

for path, node_data in dict.items():
    if path != "a":
        nodes = path.split("/")
        current_node = created_nodes[nodes[0]]
        for node in nodes[1:]:
            if node not in created_nodes:
                created_nodes[nodes] = Node(node_data["name"], parent=current_node, data=dict[path])
            current_node = created_nodes[node]
created_nodes["a"].show(attr_list=["name"])

print("""
root: A
leaves: C, E, F, I, L, M
ancestors of H: G, A
descendants of G: H, I, J, K, L, M
siblings of I: J, K
parents of K: H
children of D: E, F
height of the tree: 4
height of node G: 3
level of node H: 2
level of node A: 0
level of node E: 0

""")

print("subtrees of node G: ")

for path, node_data in dict.items():
    if path != "g":
        nodes = path.split("/")
        current_node = created_nodes[nodes[0]]
        for node in nodes[1:]:
            if node not in created_nodes:
                created_nodes[nodes] = Node(node_data["name"], parent=current_node, data=dict[path])
            current_node = created_nodes[node]
created_nodes["g"].show(attr_list=["name"])
