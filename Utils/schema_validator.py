import json
from jsonschema import validate

def validate_schema(response_body, schema_path):
    """ Validates the response against the provided JSON schema.            
    Args:
        response_body (dict): The response body to validate.
        schema_path (str): The path to the JSON schema file.        
    Raises:
        jsonschema.exceptions.ValidationError: If the response does not conform to the schema.
    """

    with open(schema_path) as f:
        schema = json.load(f)

    validate(instance=response_body, schema=schema)