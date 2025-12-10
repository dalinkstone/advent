import sys

def solve_largest_rectangle(filename):
    poly = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) == 2:
                poly.append((int(parts[0]), int(parts[1])))

    edges = []
    n = len(poly)
    for i in range(n):
        p1 = poly[i]
        p2 = poly[(i + 1) % n]
        edges.append((p1[0], p1[1], p2[0], p2[1]))

    def is_point_inside(x, y):
        inside = False
        for x1, y1, x2, y2 in edges:
            if (y1 > y) != (y2 > y):
                intersect_x = (x2 - x1) * (y - y1) / (y2 - y1) + x1
                if x < intersect_x:
                    inside = not inside
        return inside

    def does_edge_cut_rect(rx_min, rx_max, ry_min, ry_max):
        for x1, y1, x2, y2 in edges:
            if x1 == x2: 
                if rx_min < x1 < rx_max:
                    edge_y_min, edge_y_max = min(y1, y2), max(y1, y2)
                    if max(ry_min, edge_y_min) < min(ry_max, edge_y_max):
                        return True
            
            else:
                if ry_min < y1 < ry_max:
                    edge_x_min, edge_x_max = min(x1, x2), max(x1, x2)
                    if max(rx_min, edge_x_min) < min(rx_max, edge_x_max):
                        return True
        return False

    max_area = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            p1 = poly[i]
            p2 = poly[j]
            
            x1, y1 = p1
            x2, y2 = p2
            
            rx_min, rx_max = min(x1, x2), max(x1, x2)
            ry_min, ry_max = min(y1, y2), max(y1, y2)
            
            width = rx_max - rx_min + 1
            height = ry_max - ry_min + 1
            area = width * height
            
            if area <= max_area:
                continue

            if does_edge_cut_rect(rx_min, rx_max, ry_min, ry_max):
                continue

            mid_x = (rx_min + rx_max) / 2
            mid_y = (ry_min + ry_max) / 2
            
            if not is_point_inside(mid_x, mid_y):
                continue

            max_area = area

    return max_area

if __name__ == "__main__":
    result = solve_largest_rectangle("input.txt")
    print(f"The largest valid rectangle area is: {result}")
