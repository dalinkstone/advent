def decipher(filename: str) -> int:
    points = []
    with open(filename, "r") as file:
        for line in file:
            if line.strip():
                points.append([int(num) for num in line.strip().split(",")])

    pairs = []
    num_points = len(points)
    
    for i in range(num_points):
        for j in range(i + 1, num_points):
            p1 = points[i]
            p2 = points[j]
            
            dist_sq = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2
            distance = dist_sq ** 0.5
            
            pairs.append((distance, i, j))

    pairs.sort(key=lambda x: x[0])

    parent = list(range(num_points))

    def find_root(p):
        path = []
        while p != parent[p]:
            path.append(p)
            p = parent[p]
        for node in path:
            parent[node] = p
        return p

    limit = 1000
    for k in range(min(limit, len(pairs))):
        _, idx_a, idx_b = pairs[k]
        
        root_a = find_root(idx_a)
        root_b = find_root(idx_b)
        
        if root_a != root_b:
            parent[root_a] = root_b

    circuit_sizes = {}
    for i in range(num_points):
        root = find_root(i)
        if root in circuit_sizes:
            circuit_sizes[root] += 1
        else:
            circuit_sizes[root] = 1

    sizes = sorted(circuit_sizes.values(), reverse=True)
    
    if len(sizes) >= 3:
        result = sizes[0] * sizes[1] * sizes[2]
    else:
        result = 1
        for s in sizes:
            result *= s

    return result

if __name__ == '__main__':
    result = decipher('input.txt')
    print(f"The result is {result}")
