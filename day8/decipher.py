def decipher(filename: str) -> int:
    points = []
    with open(filename, "r") as file:
        for line in file:
            if line.strip():
                points.append([int(num) for num in line.strip().split(",")])

    num_points = len(points)
    
    edges = []
    for i in range(num_points):
        for j in range(i + 1, num_points):
            p1 = points[i]
            p2 = points[j]
            
            dist_sq = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2
            distance = dist_sq ** 0.5
            
            edges.append((distance, i, j))

    edges.sort(key=lambda x: x[0])

    parent = list(range(num_points))
    num_circuits = num_points

    def find_root(p):
        path = []
        while p != parent[p]:
            path.append(p)
            p = parent[p]
        for node in path:
            parent[node] = p
        return p

    for _, idx_a, idx_b in edges:
        root_a = find_root(idx_a)
        root_b = find_root(idx_b)

        if root_a != root_b:
            parent[root_a] = root_b
            num_circuits -= 1

            if num_circuits == 1:
                x1 = points[idx_a][0]
                x2 = points[idx_b][0]
                
                print(f"Final connection between index {idx_a} (X={x1}) and index {idx_b} (X={x2})")
                return x1 * x2

    return 0

if __name__ == '__main__':
    result = decipher('input.txt')
    print(f"The result is {result}")
