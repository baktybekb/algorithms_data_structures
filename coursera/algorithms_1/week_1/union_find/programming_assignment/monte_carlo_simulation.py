"""
Problem:
Monte Carlo simulation. To estimate the percolation threshold, consider the following computational experiment:

Initialize all sites to be blocked.
Repeat the following until the system percolates:
Choose a site uniformly at random among all blocked sites.
Open the site.
The fraction of sites that are opened when the system percolates provides an estimate of the percolation threshold.
For example, if sites are opened in a 20-by-20 lattice according to the snapshots below, then our estimate of
the percolation threshold is 204/400 = 0.51 because the system percolates when the 204th site is opened.

By repeating this computation experiment T times and averaging the results, we obtain a more accurate estimate of the
percolation threshold. Let xt be the fraction of open sites in computational experiment t. The sample mean x⎯⎯⎯
 provides an estimate of the percolation threshold; the sample standard deviation s; measures the sharpness of the
 threshold.

x⎯⎯⎯=x1+x2+⋯+xTT,s2=(x1−x⎯⎯⎯)2+(x2−x⎯⎯⎯)2+⋯+(xT−x⎯⎯⎯)2T−1
Assuming T is sufficiently large (say, at least 30), the following provides a 95% confidence interval for the
percolation threshold:
[x⎯⎯⎯−1.96sT‾‾√,x⎯⎯⎯+1.96sT‾‾√]
To perform a series of computational experiments, create a data type PercolationStats with the following API.

public class PercolationStats {

    // perform independent trials on an n-by-n grid
    public PercolationStats(int n, int trials)

    // sample mean of percolation threshold
    public double mean()

    // sample standard deviation of percolation threshold
    public double stddev()

    // low endpoint of 95% confidence interval
    public double confidenceLo()

    // high endpoint of 95% confidence interval
    public double confidenceHi()

   // test client (see below)
   public static void main(String[] args)

}

Throw an IllegalArgumentException in the constructor if either n ≤ 0 or trials ≤ 0.
Also, include a main() method that takes two command-line arguments n and T, performs T independent computational
experiments (discussed above) on an n-by-n grid, and prints the sample mean, sample standard deviation, and the 95%
confidence interval for the percolation threshold. Use StdRandom to generate random numbers; use StdStats to compute
the sample mean and sample standard deviation.
"""

import random
import math


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x]) # Path compression
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root != y_root:
            if self.rank[x_root] < self.rank[y_root]:
                x_root, y_root = y_root, x_root  # Ensure x_root is root of larger rank
            self.parent[y_root] = x_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1  # Increase rank if both subtrees have same rank


class PercolationStats:
    def __init__(self, n, trials):
        self.n = n
        self.trials = trials
        self.results = []
        for _ in range(trials):
            self.results.append(self.percolation_experiment())

    def percolation_experiment(self):
        grid = [0]*(self.n*self.n)
        uf = UnionFind(self.n*self.n + 2)  # include two virtual nodes
        opens = 0
        while uf.find(self.n*self.n) != uf.find(self.n*self.n+1):  # top is connected to bottom
            i = random.randint(0, self.n*self.n-1)
            if grid[i] == 0:
                grid[i] = 1
                opens += 1
                x, y = divmod(i, self.n)
                # Check all neighbors
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.n and 0 <= ny < self.n and grid[nx*self.n+ny] == 1:
                        uf.union(i, nx*self.n + ny)
                if x == 0:
                    uf.union(i, self.n*self.n) # connect to virtual top
                if x == self.n-1:
                    uf.union(i, self.n*self.n+1) # connect to virtual bottom
        return opens / (self.n*self.n)

    def mean(self):
        return sum(self.results) / self.trials

    def stddev(self):
        mean = self.mean()
        return math.sqrt(sum((x-mean)**2 for x in self.results) / (self.trials - 1))

    def confidenceLo(self):
        return self.mean() - 1.96*self.stddev()/math.sqrt(self.trials)

    def confidenceHi(self):
        return self.mean() + 1.96*self.stddev()/math.sqrt(self.trials)

    def main(self, n, trials):
        ps = PercolationStats(n, trials)
        print("mean = ", ps.mean())
        print("stddev = ", ps.stddev())
        print(f"95% confidence interval = [{ps.confidenceLo()}, {ps.confidenceHi()}]")
