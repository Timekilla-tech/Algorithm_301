import unittest

# insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(arr)

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

    def test_insertion_sort(self):
        expected = sorted(self.arr)  # shuud sortloj bgaa
        insertion_sort(self.arr)     # insertion sortoor 
        self.assertEqual(self.arr, expected)

if __name__ == '__main__':
    unittest.main()
