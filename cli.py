import ruamel.yaml as yaml
from utils import get_class

def workflow(config_path):
    with open(config_path) as fp:
        config = yaml.safe_load(fp)
        f = get_class(config['func'])
        print(f.run())


if __name__ == "__main__":
    #run()
    path = "C:/projects/try-py-reflection/test.yaml"
    workflow(path)
