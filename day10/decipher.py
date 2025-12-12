import re
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

def solve_machine_joltage(line: str) -> int:
    target_match = re.search(r'\{([\d,]+)\}', line)
    if not target_match:
        return 0
    targets = np.array([int(x) for x in target_match.group(1).split(',')])
    
    raw_buttons = re.findall(r'\(([\d,]+)\)', line)
    buttons = []
    n_counters = len(targets)
    
    for b_str in raw_buttons:
        vec = np.zeros(n_counters)
        parts = b_str.split(',')
        valid_button = True
        for p in parts:
            if not p.strip(): continue
            idx = int(p.strip())
            if idx < n_counters:
                vec[idx] = 1
        buttons.append(vec)
            
    if not buttons:
        return 0

    A = np.array(buttons).T 
    c = np.ones(len(buttons))

    constraints = LinearConstraint(A, lb=targets, ub=targets)
    
    integrality = np.ones(len(buttons))
    
    bounds = Bounds(lb=0, ub=np.inf)
    
    res = milp(c=c, constraints=constraints, integrality=integrality, bounds=bounds)
    
    if res.success:
        return int(round(res.fun))
    else:
        print(f"Warning: Could not solve for line: {line.strip()}")
        return 0

def decipher_joltage(filename: str) -> int:
    total_presses = 0
    with open(filename, 'r') as f:
        for line in f:
            if '{' in line and '}' in line:
                total_presses += solve_machine_joltage(line)
    return total_presses

if __name__ == "__main__":
    result = decipher_joltage("input.txt")
    print(f"The fewest total presses required is: {result}")
