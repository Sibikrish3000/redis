from configparser import ConfigParser
import os
print(os.getcwd())
def load_config(filename='./instance/database.cfg',section='redis'):
    """
    Load configuration parameters from a specified INI file.

    Parameters:
    filename (str): The name of the INI file to load. Default is '.instance/database.cfg'.
    section (str): The section within the INI file to load. Default is 'redis'.
    """
    config = ConfigParser()
    config.read(filename)
    if config.has_section(section):
        configuration= {key:value for key, value in config.items(section)}
    else:
        raise Exception(f'Section {section} not found in the {filename} file')
    return configuration
# if __name__ == '__main__':
#     config = load_config()
#     print(config)