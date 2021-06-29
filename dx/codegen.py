"""Generate python pydantic models from JSON Schema files."""
from pathlib import Path
from tempfile import TemporaryDirectory

from datamodel_code_generator import InputFileType, generate


# TODO convert to file later
json_schema: str = """{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Person",
  "type": "object",
  "properties": {
    "firstName": {
      "type": "string",
      "description": "The person's first name."
    },
    "lastName": {
      "type": "string",
      "description": "The person's last name."
    },
    "age": {
      "description": "Age in years which must be equal to or greater than zero.",
      "type": "integer",
      "minimum": 0
    },
    "friends": {
      "type": "array"
    },
    "comment": {
      "type": "null"
    }
  }
}
"""

with TemporaryDirectory() as temporary_directory_name:
    temporary_directory = Path(temporary_directory_name)
    output = Path(temporary_directory / 'model.py')
    generate(
        json_schema,
        input_file_type=InputFileType.JsonSchema,
        input_filename="example.json",
        output=output,
    )
    model: str = output.read_text()
print(model)


