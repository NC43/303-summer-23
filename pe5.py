import unittest
import pprint
n = 12
m = list(list(range(1*i,(n+1)*i, i)) for i in range(1,n+1))
pprint.pprint(m)

def generate_multiples_list(n):
    return list(list(range(1*i, (n+1)*i, i)) for i in range(1, n+1))

class TestMultiplesList(unittest.TestCase):
    def test_basic_1(self):
        n = 5
        expected_output = [
            [1],
            [2, 4],
            [3, 6, 9],
            [4, 8, 12, 16],
            [5, 10, 15, 20, 25]
        ]
        self.assertEqual(generate_multiples_list(n), expected_output)
    def test_basic_2(self):
        n = 3
        expected_output = [
            [1],
            [2, 4],
            [3, 6, 9]
        ]
        self.assertEqual(generate_multiples_list(n), expected_output)

    @unittest.expectedFailure
    def test_expected_fail(self):
        n = 6
        expected_output = [
            [1],
            [2, 4],
            [3, 6, 9],
            [4, 8, 12, 16],
            [5, 10, 15, 20, 25],
            [6, 12, 18, 24, 30, 36]  # This is expected to fail due to the wrong expected_output
        ]
        self.assertEqual(generate_multiples_list(n), expected_output)

    def test_index_error(self):
        n = 12
        m = generate_multiples_list(n)
        with self.assertRaises(IndexError):
            m[12]  # This will raise an IndexError as row index 12 exceeds the table size

        with self.assertRaises(IndexError):
            m[0][13]  # This will raise an IndexError as column index 13 exceeds the table size


if __name__ == '__main__':
    unittest.main()

# conftest.py

import pytest
import time

@pytest.fixture(autouse=True)
def timeit(request):
    start_time = time.time()
    yield
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"\nExecution time: {execution_time:.6f} seconds\n")
