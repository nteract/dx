# dx Design Concepts

## Use cases

- Store a chart view
- Load a stored chart into a notebook
- Save chart settings as a template
- Programmatic creation of a chart

## JSON Schema for data-explorer

Update the current schema files for data-explorer as they currently fail
when trying to convert to a Python model

## Convert JSON Schema to Python model

Use **datamodel-code-generator** to convert JSON, JSON Schema or OpenAPI to
Python model.

## Store the Python model for programmatic use

## Workflow

- Create a notebook
- Display a chart
- Save the notebook
- Extract the chart cell's metadata
- Create a second notebook for programmatic execution
- Pass the cell's metadata converted to Python code
- Render the chart from the Python code in a notebook
