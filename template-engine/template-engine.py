import re
import json
def parse_template(template):
    # Use regular expressions to find placeholder tokens
    placeholders = re.findall(r'{\$(\w+)}', template)
    return placeholders

json_file = "parameters.json"
def load_parameters_from_json(json_file):
    with open(json_file, 'r') as file:
        parameters = json.load(file)
    return parameters
def generate_text(template, parameters):
    texts = []
    for param_set in parameters:
        text = template
        for key, value in param_set.items():
            placeholder = "{$" + key + "}"
            text = text.replace(placeholder, str(value))
        texts.append(text)
    return texts

template = "Hey {$name}! You've won a prize!"
parameters = load_parameters_from_json("parameters.json")

generated_texts = generate_text(template, parameters)
for text in generated_texts:
    print(text)



