import json
from jsonschema import validate, ValidationError

def match_schema(response_data, schema_path):
    with open(schema_path, 'r', encoding='utf-8') as schema_file:
        schema = json.load(schema_file)
    try:
        validate(instance=response_data, schema=schema)
        return True
    except ValidationError as e:
        print(f"Schema validation error: {e.message}")
        return False
