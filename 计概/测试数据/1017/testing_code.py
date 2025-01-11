import subprocess
import difflib
import os
import sys


def test_code(script_path, infile, outfile):
    command = ["python", script_path]  
    with open(infile, 'r') as fin, open(outfile, 'r') as fout:
        expected_output = fout.read().strip()
        process = subprocess.Popen(command, stdin=fin, stdout=subprocess.PIPE)
        actual_output, _ = process.communicate()
        if actual_output.decode().strip() == expected_output:
            return True
        else:
            print(f"Output differs for {infile}:")
            diff = difflib.unified_diff(
                expected_output.splitlines(),
                actual_output.decode().splitlines(),
                fromfile='Expected', tofile='Actual', lineterm=''
            )
            print('\n'.join(diff))
            return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python testing_code.py <filename>")
        sys.exit(1)

    script_path = sys.argv[1]
    #script_path = "e1.py"  
    #test_cases = ["d.in"]  
    #expected_outputs = ["d.out"]  
    files = os.listdir('.')

    test_cases = [f for f in files if f.endswith('.in')]
    expected_outputs = [f for f in files if f.endswith('.out')]

    for infile, outfile in zip(test_cases, expected_outputs):
        if not test_code(script_path, infile, outfile):
            break
