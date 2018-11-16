import configparser
import pkg_resources
import os


PROJECT_NAME = 'uveb'
CONFIG_FILE = r'/etc/uveb/uveb.conf'


class Config:
    @staticmethod
    def read():
        Config.config_parser = configparser.RawConfigParser()
        Config.config_parser.read(CONFIG_FILE)
        
        Config._db_username = Config.config_parser.get('Database', 'username')
        Config._db_password = Config.config_parser.get('Database', 'password')

        if os.environ['FLASK_ENV'] == 'development':
            Config._version = 'DEV'
        else:
            Config._version = pkg_resources.require('uveb')[0].version

        Config._static_server = Config.config_parser.get('Static', 'location')

    @staticmethod
    def get_db_username(reread=False):
        if reread:
            Config._db_username = Config.config_parser.get('Database',
                    'username')
        
        return Config._db_username

    @staticmethod
    def get_db_password(reread=False):
        if reread:
            Config._db_password = Config.config_parser.get('Database',
                    'password')

        return Config._db_password

    @staticmethod
    def get_version():
        return Config._version

    @staticmethod
    def get_static_server(reread=False):
        if reread:
            Config._static_server = Config.config_parser.get('Static',
                    'location')

        return Config._static_server
