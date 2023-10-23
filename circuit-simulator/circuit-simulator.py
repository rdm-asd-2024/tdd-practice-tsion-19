class Input:
    def __init__(self):
        self.value = None

    def set_value(self, value):
        self.value = value

class And:
    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    def evaluate(self):
        return self.input1.evaluate() and self.input2.evaluate()

class Or:
    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    def evaluate(self):
        return self.input1.evaluate() or self.input2.evaluate()

class Not:
    def __init__(self, input_gate):
        self.input_gate = input_gate

    def evaluate(self):
        return not self.input_gate.evaluate()

class Output:
    def __init__(self, input_gate):
        self.input_gate = input_gate

    def evaluate(self):
        return self.input_gate.evaluate()

# Function to parse and build the circuit from a file
def parse_circuit(filename):
    gates = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            gate_name = parts[0]
            if gate_name == 'Input':
                gates[parts[2]] = Input()
            elif gate_name == 'And':
                gates[parts[0]] = And(gates[parts[2]], gates[parts[4]])
            elif gate_name == 'Or':
                gates[parts[0]] = Or(gates[parts[2]], gates[parts[4]])
            elif gate_name == 'Not':
                gates[parts[0]] = Not(gates[parts[2]])
            elif gate_name == 'Output':
                gates[parts[0]] = Output(gates[parts[2]])

    return gates

# Function to evaluate the circuit
def evaluate_circuit(circuit, input_values):
    for key, value in input_values.items():
        circuit[key].set_value(value)

    output_gates = [key for key, gate in circuit.items() if isinstance(gate, Output)]
    results = {}
    for output_gate in output_gates:
        results[output_gate] = circuit[output_gate].evaluate()

    return results

# Example usage
if __name__ == "__main__":
    circuit_file = "your_circuit_description.txt"
    circuit = parse_circuit(circuit_file)
    
    # Define input values (0 or 1) as a dictionary
    input_values = {
        'x_0': 1,
        'x_1': 0,
    }
    
    results = evaluate_circuit(circuit, input_values)
    
    for key, value in results.items():
        print(f"{key} = {value}")
ss