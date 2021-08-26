
# DEPREACTED: no longer needed for the plugin.
# Check if the given lines of code are Python code or not.
def is_python_code(lines):
    import ast

    # Try pasing the code normally.
    try:
        ast.parse(lines)
        return True
    except SyntaxError:
        # Try parsing more if it fails.
        pass

    # Try parsing with all the leading spaces stripped.
    try:
        parts = [part.lstrip(' ') for part in lines.split("\n")]
        ast.parse("\n".join(parts))
        return True
    except SyntaxError:
        pass

    # Try parsing by removing tab_space on all lines.
    try:
        parts = indent_code_left(lines)
        ast.parse(parts)
        return True
    except SyntaxError as e:
        # Either malformed Python code or just not code, return False.
        print(f"failed to parse on \n{lines}\nAttempted to parse \n{parts}\n", e)
        return False

    def test_is_python_code(self):
        # Check that the function correctly determines if a snippet is Python
        # code. Should pass.
        python_code = \
"""
# A const variable comment.
CONST = "some constant value"

def foo(arg1, arg2):
    if arg1 in arg2:
        do_something(arg1) # Inline comment
    elif arg2 in arg1:
        '''
          ast.parse only checks that this is a valid Python looking code,
          doesn't guarantee that it will actually run but it could.
        '''
        maybe_do_something( arg2 )
    else:
        try:
            if arg1 == arg2:
                raise ValueError
            return arg1+arg2
        except ValueError:
            return arg2+arg1

    return (arg1 in arg2)
"""
        self.assertTrue(is_python_code(python_code))

        # Check that it does not work on a string. Should fail.
        not_code = "This is just a simple text."
        self.assertFalse(is_python_code(not_code))


        # Check that it wrong formats are also not considered Python code.
        # Should fail.
        bad_indentation = \
"""
def foo(arg1, arg2):
return arg1 in arg2
"""
        self.assertFalse(is_python_code(not_code))

        # Check on weird indentation formats. Should fail.
        weird_indentation = \
"""
  def foo(arg1, arg2):
return arg1 in arg2
"""
        self.assertFalse(is_python_code(weird_indentation))
