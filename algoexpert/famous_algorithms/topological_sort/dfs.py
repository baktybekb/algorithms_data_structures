# https://www.algoexpert.io/questions/topological-sort

# O(j + d) time | O(j + d) space
def topologicalSort(jobs, deps):
    graph = create_graph(jobs, deps)
    return get_ordered_jobs(graph)


def create_graph(jobs, deps):
    graph = Graph(jobs)
    for prereq, job in deps:
        graph.add_prereq(job, prereq)
    return graph


def get_ordered_jobs(graph):
    ordered = []
    nodes = graph.nodes
    while nodes:
        node = nodes.pop()
        contains_cycle = dfs(node, ordered)
        if contains_cycle:
            return []
    return ordered


def dfs(node, ordered):
    if node.visited:
        return False
    node.visiting = True
    for prereq in node.prereqs:
        if prereq.visiting or dfs(prereq, ordered):
            return True
    node.visited = True
    node.visiting = False
    ordered.append(node.job)
    return False


class Graph:
    def __init__(self, jobs):
        self.nodes = []
        self.graph = {}
        for job in jobs:
            self.add_node(job)

    def add_node(self, job):
        self.graph[job] = Node(job)
        self.nodes.append(self.graph[job])

    def add_prereq(self, job, prereq):
        job_node = self.get_node(job)
        prereq_node = self.get_node(prereq)
        job_node.prereqs.append(prereq_node)

    def get_node(self, job):
        return self.graph[job]


class Node:
    def __init__(self, job):
        self.job = job
        self.prereqs = []
        self.visited = False
        self.visiting = False
