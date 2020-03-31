import yaml

def loadYAMLfile(filename: str) -> str:
    with open(filename, "r") as stream:
        try:
            filecontent = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print("LOADYAMLFILE ERROR " + exc)
            raise exc
    return filecontent