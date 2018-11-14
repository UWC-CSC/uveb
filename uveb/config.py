import configparser

CONFIG_FILE = r'/etc/uveb/uveb.conf'


class Config:
    @staticmethod
    def read():
        Config.config_parser = configparser.RawConfigParser()
        Config.config_parser.read(CONFIG_FILE)
        
        Config._db_username = Config.config_parser.get('Database', 'username')
        Config._db_password = Config.config_parser.get('Database', 'password')

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
