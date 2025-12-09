from itertools import combinations

with open('2025/data/9.txt', 'r') as infile:
    vertices = [tuple(map(int, line.split(','))) for line in infile]

edges = list(zip(vertices, vertices[1:]+[vertices[0]]))
vertical_edges = [(x0, *sorted((y0,y1))) 
                  for (x0,y0), (x1,y1) 
                  in edges 
                  if x0==x1]
horizontal_edges = [(y0, *sorted((x0,x1))) 
                    for (x0,y0), (x1,y1) 
                    in edges 
                    if y0==y1]

max_area = 0
for (x0, y0), (x1, y1) in combinations(vertices, 2): 
    min_x, min_y, max_x, max_y = min(x0, x1)+0.5, min(y0, y1)+0.5, max(x0, x1)-0.5, max(y0, y1)-0.5
    if not any(
        (min_x <= v_x <= max_x 
         and (min_v_y <= min_y <= max_v_y 
              or min_v_y <= max_y <= max_v_y)) or 
        (min_y <= h_y <= max_y 
         and (min_h_x <= min_x <= max_h_x 
              or min_h_x <= max_x <= max_h_x))
        for (v_x, min_v_y, max_v_y), (h_y, min_h_x, max_h_x) 
        in zip(vertical_edges, horizontal_edges)
    ):
        max_area = max(max_area, (abs(x0-x1)+1)*(abs(y0-y1)+1))

print(max_area)