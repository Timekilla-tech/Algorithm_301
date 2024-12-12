import unittest

# binary search
def binary_search(arr,low, hi, x):
    if hi < 0: return -1

    mid = (hi + low )// 2

    if arr[mid] == x: return mid
    elif arr[mid] > x: return binary_search(arr,low,mid - 1, x)
    else: return binary_search(arr,mid + 1,hi, x)

# read test case
def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        line = file.readline().strip()  # илүү хоосон зайг устгаж байгаа
        return list(map(int, line.split(',')))  # list рүү хөрвүүлж байгаа

# unit test
class TestInsertionSortFromFile(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 
        cls.arr = read_numbers_from_file('Algo/lab2/insertion_test_case.txt')

    def test_binary_search(self):
        expected = 6  # 5,2,9,7,3,6,10,1
        index = binary_search(self.arr,0,7,10)    # binary hailtaar
        self.assertEqual(index, expected)

if __name__ == '__main__':
    unittest.main()
