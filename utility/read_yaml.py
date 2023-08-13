import yaml

# Function to read API keys from the YAML file
def read_api_keys(file_path):
    with open(file_path, 'r') as file:
        api_keys = yaml.safe_load(file)
        return api_keys