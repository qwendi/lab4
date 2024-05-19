import unittest
from main import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()


    def test_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)


    def test_most_frequent_word(self):
        file = open('test.txt', 'w')
        file.write('cat dog cat')
        file.close()

        with open('test.txt', 'rb') as f:
            response = self.app.post('/', data=dict(file=(f, 'test.txt')))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, b'Слово, которое часто встречается "cat" количество: 2.')


    def test_no_words_found(self):
        file = open('test.txt', 'w')
        file.write('123')
        file.close()

        with open('test.txt', 'rb') as f:
            response = self.app.post('/', data=dict(file=(f, 'test.txt')))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, b'Слова не найдены в файле.')


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()