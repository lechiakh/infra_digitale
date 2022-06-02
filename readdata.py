import yaml

with open('data.yml') as f:

    data = yaml.load_all(f, Loader=yaml.FullLoader)
    for doc in data: