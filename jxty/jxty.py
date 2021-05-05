import json
import xmltodict
import toml
import yaml

def load(fmt, file):
    load = {
        "json": json.load,
        "xml":  lambda file: xmltodict.parse(file.read()),
        "toml": toml.load,
        "yaml": yaml.safe_load
    }

    return load[fmt](file)

def dump(obj, fmt, file):
    dump = {
        "json": json.dump,
        "xml":  lambda obj, file: xmltodict.unparse(obj, file, pretty=True, full_document=False),
        "toml": toml.dump,
        "yaml": yaml.dump
    }

    return dump[fmt](obj, file)