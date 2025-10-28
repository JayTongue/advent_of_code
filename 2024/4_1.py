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
	
	xmas = np.array(['X', 'M', 'A', 'S'])
	samx = np.array(['S', 'A', 'M', 'X'])
	count = 0
	
	# iterate through columns
	for col in range(data.shape[1]):
		data_col = data[:, col]
		#print(data_col)
		count = search_vert(data_col, count, xmas, samx)
	#iterate through rows
	for row in range(data.shape[0]):
		data_row = data[row, :]
		#print(data_row)
		count = search_horiz(data_row, count, xmas, samx)
	# iterate through every item
	for index, element in np.ndenumerate(data):
		#print(index, element)
		data_window = data[index[0]:index[0]+4, index[1]:index[1]+4]
		if data_window.shape != (4,4):
			continue
		#print(data_window)
		count = search_diag(data_window, count, xmas, samx)
		
	print(count)


def search_vert(data_window, count, xmas, samx):
	for i in range(len(data_window) - 3):
		data_chunk = np.array([data_window[i + j] for j in range(4)])
		#print(i, data_chunk)
		if ((data_chunk == xmas).all()) or ((data_chunk == samx).all()):
			count += 1
	return count
		
		
def search_horiz(data_window, count, xmas, samx):
	for i in range(len(data_window) - 3):
		data_chunk = np.array([data_window[i + j] for j in range(4)])
		#print(i, data_chunk)
		if ((data_chunk == xmas).all()) or ((data_chunk == samx).all()):
			count += 1
	return count
	

def search_diag(data_window, count, xmas, samx):
	right_diag = [(0,0), (1,1), (2,2), (3,3)]
	left_diag = [(0,3), (1,2), (2,1), (3,0)]
	
	for diag in [right_diag, left_diag]:
		if ((np.array([data_window[j, h] for j, h in diag]) == xmas).all()) or ((np.array([data_window[j, h] for j, h in diag]) == samx).all()):
			count += 1
	return count


if __name__ == '__main__':
    main()