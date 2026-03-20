import configparser
import os
def test_read_config():
    config_path = os.path.join(os.path.dirname(__file__), '../config.ini')
    config = configparser.ConfigParser(allow_no_value=True)
    config.optionxform = str  # Preserve case sensitivity for keys
    config.read(config_path)

    print(f"Config path: {config_path}")
    print(f"Sections: {config.sections()}")

    base_url = config.get('QA', 'url')
    username = config.get('QA', 'username')
    password = config.get('QA', 'password')
    print(f"Base URL: {base_url}")
    print(f"Username: {username}")
    print(f"Password: {password}")
