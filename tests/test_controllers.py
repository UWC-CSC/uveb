import unittest
import mysql.connector
from uveb import controllers
from uveb import credentials

class TestCVideoFetcherConnection(unittest.TestCase):
    def test_init_valid_connection(self):
        self.valid_connection = mysql.connector.connect(
                host='localhost',
                user=credentials.SQL_USERNAME,
                passwd=credentials.SQL_PASSWORD,
                database='uveb'
        )

        try:
            controllers.CVideoFetcher.init(self.valid_connection)
        except ExceptionType:
            self.fail('init() raised ExceptionType unexpectedly.')

        self.valid_connection.close()

    def test_init_invalid_connection(self):
        self.invalid_connection = mysql.connector.connect(
                host='localhost',
                user='uveb',
                passwd='password',
                database='uveb'
        )

        self.assertRaises(Exception, controllers.CVideoFetcher.init,
            self.invalid_connection)

        self.invalid_connection.close()

class TestCVideoFetcher(unittest.TestCase):
    def setUp(self):
        self.valid_connection = mysql.connector.connect(
                host='localhost',
                user=credentials.SQL_USERNAME,
                passwd=credentials.SQL_PASSWORD,
                database='uveb'
        )
        controllers.CVideoFetcher.init(self.valid_connection)

    def test_fetch_by_id(self):
        controllers.CVideoFetcher.fetch_by_id(1)
