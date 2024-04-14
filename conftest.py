import yaml
import pytest

@pytest.fixture(scope="module")
def access_token():
    try:
        # Load access token from config.yaml file this can be .env file as well
        with open("config.yaml", "r") as file:
            config = yaml.safe_load(file)
            token = config.get("ACCESS_TOKEN")
            assert token, "ACCESS_TOKEN is not specified in config.yaml"
            return token
    except FileNotFoundError:
        pytest.fail("config.yaml file not found")
    except yaml.YAMLError as e:
        pytest.fail(f"Error parsing YAML file: {e}")

