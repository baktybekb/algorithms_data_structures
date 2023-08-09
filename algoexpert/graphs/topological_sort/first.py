# O(j + d) time | O(j + d) space
# j --> jobs == vertexes
# d --> dependencies == edges
def topologicalSort(jobs, deps):
    job_graph = create_graph(jobs, deps)
    return get_ordered_jobs(job_graph)


def create_graph(jobs, deps):
    graph = JobGraph(jobs)
    for prereq, job in deps:
        graph.add_prereq(job, prereq)
    return graph


def get_ordered_jobs(graph):
    ordered_jobs = []
    while graph.nodes:
        job_node = graph.nodes.pop()
        contains_cycle = depth_first_traverse(job_node, ordered_jobs)
        if contains_cycle:
            return []
    return ordered_jobs


def depth_first_traverse(node, ordered_jobs):
    if node.visited:
        return False
    if node.visiting:
        return True
    node.visiting = True
    for prereq in node.prereqs:
        contains_cycle = depth_first_traverse(prereq, ordered_jobs)
        if contains_cycle:
            return True
    node.visited = True
    node.visiting = False
    ordered_jobs.append(node.job)
    return False


class JobGraph:
    def __init__(self, jobs):
        self.nodes = []
        self.graph = {}
        for job in jobs:
            self.add_node(job)

    def add_node(self, job):
        self.graph[job] = JobNode(job)
        self.nodes.append(self.graph[job])

    def add_prereq(self, job, prereq):
        job_node = self.get_node(job)
        prereq_node = self.get_node(prereq)
        job_node.prereqs.append(prereq_node)

    def get_node(self, job):
        return self.graph[job]


class JobNode:
    def __init__(self, job):
        self.job = job
        self.prereqs = []
        self.visited = False
        self.visiting = False

