import re
import matplotlib.pyplot as plt


def main():
    grid_dimensions = (101, 103) # wide, tall

    infile = open('data/14.txt', 'r')

    final_coords = []
    for robot in infile:
        robot = robot.strip()
        robot = re.split(r' |,', robot) 
        pos_x, pos_y, dir_x, dir_y = [int(re.sub(r'p|v|=', r'', bit)) for bit in robot]
        for i in range(100):
            pos_x, pos_y = walk_robot(grid_dimensions, pos_x, pos_y, dir_x, dir_y)
        final_coords.append((pos_x, pos_y))
    # print(final_coords)

    safety_factor = calculate_safety_factor(grid_dimensions, final_coords)

    print(f'Final Safety Factor: {safety_factor}')


def calculate_safety_factor(grid_dimensions, final_coords):
    x_half = int((grid_dimensions[0] - 1)/2)
    y_half = int((grid_dimensions[1] - 1)/2)

    quad_1, quad_2, quad_3, quad_4 = 0, 0, 0, 0

    for final_coord in final_coords:
        if final_coord[0] < x_half and final_coord[1] < y_half:
            quad_1 += 1
        elif final_coord[0] < x_half and final_coord[1] > y_half:
            quad_2 += 1
        elif final_coord[0] > x_half and final_coord[1] > y_half:
            quad_3 += 1
        elif final_coord[0] > x_half and final_coord[1] < y_half:
            quad_4 += 1    

    return quad_1 * quad_2 * quad_3 * quad_4        


def walk_robot(grid_dimensions, pos_x, pos_y, dir_x, dir_y):
    new_x = pos_x + dir_x
    new_y = pos_y + dir_y

    if new_x >= grid_dimensions[0]:
        new_x = new_x - grid_dimensions[0]
    elif new_x < 0:
        new_x = grid_dimensions[0] + new_x

    if new_y >= grid_dimensions[1]:
        new_y = new_y - grid_dimensions[1]
    elif new_y < 0:
        new_y = grid_dimensions[1] + new_y

    return new_x, new_y


if __name__ == '__main__':
    main()