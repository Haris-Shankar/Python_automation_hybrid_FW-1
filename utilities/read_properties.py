import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\config.ini")

class ReadData:
    @staticmethod
    def get_url():
        return config.get('basic_info','url')

    @staticmethod
    def get_username():
        return config.get('basic_info', 'username')

    @staticmethod
    def get_pwd():
        return config.get('basic_info', 'pwd')