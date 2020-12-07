from typing import Iterator
import networkx as nx


def parse_line(line: str) -> dict[str, dict[str, int]]:
    parts = line.split("contain")
    name = parts[0].strip()
    parts = parts[1].strip()
    if parts == "no other bags.":
        return {name: {}}
    parts = [part.strip() for part in parts.split(",")]
    # Get rid of the period that ends the sentence on the last rule
    parts[-1] = parts[-1][0:-1]
    parts = [rule.split() for rule in parts]
    parts = [[int(rule[0]), " ".join(rule[1:])] for rule in parts]
    parts = [[count, name + "s" if not name.endswith("s") else name] for (count, name) in parts]
    return {name: {rule[1]: rule[0] for rule in parts}}


def parse_lines(lines: Iterator[str]) -> dict[str, dict[str, int]]:
    result_dict = dict()
    for line in lines:
        result_dict |= parse_line(line)
    return result_dict


def can_contain(graph: nx.DiGraph, target: str = "shiny gold bags", ) -> set[str]:
    reversed_graph = graph.reverse(copy=True)
    connected_node_gen = nx.dfs_preorder_nodes(reversed_graph, source=target)
    connected_nodes = set(connected_node_gen)
    connected_nodes.remove(target)
    return connected_nodes


def contained_by(graph: nx.DiGraph, target: str = "shiny gold bags", contained_bags: int = 0) -> int:
    contained_bags += sum(
        attributes["weight"] + (attributes["weight"] * contained_by(graph, child)) for child, attributes in
        graph[target].items())
    return contained_bags


if __name__ == "__main__":
    data = open("Day 7 Data.txt").readlines()
    data = parse_lines(data)
    G = nx.DiGraph()
    G.add_nodes_from(data.keys())
    for kind, rules in data.items():
        for held_kind, count in rules.items():
            G.add_edge(kind, held_kind, weight=count)

    held_bags = contained_by(G)
    print(held_bags)
