import unittest

# merge sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        l = arr[:mid]
        r = arr[mid:]
        print("Left", l, " Right", r)
        merge_sort(l)
        merge_sort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i +=1
            else:
                arr[k] = r[j]
                j += 1
            k +=1
        
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            arr[k] = r[j]
            j+=1
            k +=1
        

# read test case
def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        line = file.readline().strip()  # илүү хоосон зайг устгаж байгаа
        return list(map(int, line.split(',')))  # list рүү хөрвүүлж байгаа

# unit test
class TestMergeSortFromFile(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        
        cls.arr = read_numbers_from_file('Algo/lab2/insertion_test_case.txt')

    def test_insertion_sort(self):
        expected = sorted(self.arr)  # shuud sortloj bgaa
        merge_sort(self.arr)     # insertion sortoor 
        self.assertEqual(self.arr, expected)

if __name__ == '__main__':
    unittest.main()
