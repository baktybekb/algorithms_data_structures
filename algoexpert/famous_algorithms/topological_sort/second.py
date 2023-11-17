# https://www.algoexpert.io/questions/topological-sort

# O(j + d) time | O(j + d) space
def topologicalSort(jobs, deps):
    graph = create_graph(jobs, deps)
    return get_ordered_jobs(graph)


def create_graph(jobs, deps):
    graph = Graph(jobs)
    for job, dep in deps:
        graph.add_dep(job, dep)
    return graph


def get_ordered_jobs(graph):
    ordered = []
    nodes_without_prereqs = list(filter(lambda node: node.num_of_prereqs == 0, graph.nodes))
    while nodes_without_prereqs:
        node = nodes_without_prereqs.pop()
        ordered.append(node.job)
        remove_deps(node, nodes_without_prereqs)
    graph_has_edges = any(node.num_of_prereqs for node in graph.nodes)
    return [] if graph_has_edges else ordered


def remove_deps(node, nodes_without_prereqs):
    while node.deps:
        dep = node.deps.pop()
        dep.num_of_prereqs -= 1
        if dep.num_of_prereqs == 0:
            nodes_without_prereqs.append(dep)


class Graph:
    def __init__(self, jobs):
        self.nodes = []
        self.graph = {}
        for job in jobs:
            self.add_node(job)

    def add_node(self, job):
        self.graph[job] = Node(job)
        self.nodes.append(self.graph[job])

    def add_dep(self, job, dep):
        job_node = self.get_node(job)
        dep_node = self.get_node(dep)
        job_node.deps.append(dep_node)
        dep_node.num_of_prereqs += 1

    def get_node(self, job):
        return self.graph[job]


class Node:
    def __init__(self, job):
        self.job = job
        self.deps = []
        self.num_of_prereqs = 0
