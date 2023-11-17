# O(j + d) | O(j + d)
# j --> jobs == vertexes
# d --> dependencies == edges
def topologicalSort(jobs, deps):
    graph = create_graph(jobs, deps)
    return get_ordered_jobs(graph)


def create_graph(jobs, deps):
    graph = JobGraph(jobs)
    for job, dep in deps:
        graph.add_dep(job, dep)
    return graph


def get_ordered_jobs(graph):
    ordered_jobs = []
    nodes_with_no_prereqs = list(filter(lambda node: node.num_of_deps == 0, graph.nodes))
    while nodes_with_no_prereqs:
        node = nodes_with_no_prereqs.pop()
        ordered_jobs.append(node.job)
        remove_deps(node, nodes_with_no_prereqs)
    graph_has_cycle = any(node.num_of_deps for node in graph.nodes)
    return [] if graph_has_cycle else ordered_jobs


def remove_deps(node, nodes_with_no_prereqs):
    while node.deps:
        dep_node = node.deps.pop()
        dep_node.num_of_deps -= 1
        if dep_node.num_of_deps == 0:
            nodes_with_no_prereqs.append(dep_node)


class JobGraph:
    def __init__(self, jobs):
        self.nodes = []
        self.graph = {}
        for job in jobs:
            self.add_node(job)

    def add_node(self, job):
        self.graph[job] = JobNode(job)
        self.nodes.append(self.graph[job])

    def add_dep(self, job, dep):
        job_node = self.get_node(job)
        dep_node = self.get_node(dep)
        job_node.deps.append(dep_node)
        dep_node.num_of_deps += 1

    def get_node(self, job):
        if job not in self.graph:
            self.add_node(job)
        return self.graph[job]


class JobNode:
    def __init__(self, job):
        self.job = job
        self.deps = []
        self.num_of_prereqs = 0
