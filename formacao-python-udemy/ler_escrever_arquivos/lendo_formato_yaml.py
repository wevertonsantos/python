import yaml
with open("config.yaml") as file:
    data = yaml.load(file, Loader=yaml.FullLoader) # carregando todo arquivo de configuração yaml
    print(data['database']['name']) # pegando database do yaml