import numpy as np

def main():
    with open('data/4.txt', 'r') as file:
        data = [list(line.strip()) for line in file]
    data = np.array(data, dtype=str)
    data = data.squeeze()
    # print(data)

    count = 0
    find_xmas(data)


def find_xmas(data):
	
	xmas = np.array(['M', 'A', 'S'])
	samx = np.array(['S', 'A', 'M'])
	count = 0
	
	for index, element in np.ndenumerate(data):
		#print(index, element)
		data_window = data[index[0]:index[0]+3, index[1]:index[1]+3]
		if data_window.shape != (3,3):
			continue
		#print(data_window)
		count = search_diag(data_window, count, xmas, samx)
		
	print(count)


def search_diag(data_window, count, xmas, samx):
	right_diag = [(0,0), (1,1), (2,2)]
	left_diag = [(0,2), (1,1), (2,0)]
	
	window_right = np.array([data_window[j, h] for j, h in right_diag])
	window_left =  np.array([data_window[j, h] for j, h in left_diag]) 
	
	if ((window_right == xmas).all() or (window_right == samx).all()) and ((window_left == xmas).all() or (window_left == samx).all()):
		count += 1
			
		
	return count


if __name__ == '__main__':
    main()