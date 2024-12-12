import unittest

# find max
def find_max(arr, low, hi):
    if hi == low: return arr[low]
    
    mid = (hi + low)//2

    max_l = find_max(arr, low, mid)
    max_r = find_max(arr, mid+1, hi)

    return max(max_l, max_r)

# read test case
def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        line = file.readline().strip()  # илүү хоосон зайг устгаж байгаа
        return list(map(int, line.split(',')))  # массив рүү хөрвүүлж байгаа

# unit test
class TestInsertionSortFromFile(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 
        cls.arr = read_numbers_from_file('Algo/lab2/insertion_test_case.txt')

    def test_findmax(self):
        expected = 10  # 5,2,9,7,3,6,10,1
        max = find_max(self.arr, 0, len(self.arr) - 1)    # binary hailtaar
        self.assertEqual(max, expected)

if __name__ == '__main__':
    unittest.main()
