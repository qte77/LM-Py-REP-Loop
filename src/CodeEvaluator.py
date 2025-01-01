"""
This module contains the CodeEvaluator class, which evaluates the correctness and efficiency of generated Python code.

The CodeEvaluator class:
- Executes the given code in a Python REPL.
- Captures the output and any errors.
- Returns a dictionary with the execution results, including success status, output, and error messages.
"""

import process

class CodeEvaluator:
    """Evaluates generated Python code for correctness and efficiency."""

    def evaluate_code(self, code):
        """
        Execute the given code in a Python REPL and evaluate its output.

        Args:
            code (str): The Python code to evaluate.

        Returns:
            dict: A dictionary containing:
                - 'success' (bool): Whether the code executed successfully.
                - 'output' (str): The output of the code execution.
                - 'error' (str): Any error messages if the code failed.
        """
        
        try:
            # Execute the code in a Python REPL
            process = subprocess.Popen(['python', '-c', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            return {
                'success': process.returncode == 0,
                'output': stdout.decode('utf-8'),
                'error': stderr.decode('utf-8')
            }
        except Exception as e:
            return {
                'success': False,
                'output': '',
                'error': str(e)
            }
