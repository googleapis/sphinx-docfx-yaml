from docfx_yaml.extension import extract_keyword
from docfx_yaml.extension import indent_code_left
from docfx_yaml.extension import is_python_code


import unittest

from yaml import load, Loader

class TestGenerate(unittest.TestCase):
    def test_indent_code_left(self):
        # Check that the code indents to left based on first line.
        code_want = \
"""def foo():
    print('test function for indent')
    return ('left-indented-code')
"""

        code = \
"""    def foo():
        print('test function for indent')
        return ('left-indented-code')
"""
        code = indent_code_left(code)
        self.assertEqual(code, code_want)

        # Check that if there's no whitespace, it does not indent
        code_want = \
"""
print('test function for no impact indent')
for i in range(10):
    print(i)
    if i%5 == 0:
        i += 1
    else:
        continue
"""

        code_got = indent_code_left(code_want)
        # Confirm that nothing changes.
        self.assertEqual(code_got, code_want)


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

        # Check on indented code. Should pass.
        indented_code = \
"""    def foo(arg1, arg2):
        print(arg1 in arg2)
        for i in range (10):
            print (i in arg1 or i in arg2)
"""
        self.assertTrue(is_python_code(indented_code))

        # Check on single line of indented code. Should pass.
        single_indented_code = "     print('lots of trailing whitespace')"
        self.assertTrue(is_python_code(single_indented_code))

        # Check on syntax errors. Should fail.
        syntax_error = "print hello"
        self.assertFalse(is_python_code(syntax_error))


    def test_extract_keyword(self):
        # Check that keyword properly gets processed.
        keyword_want = "attribute"

        keyword_line = ".. attribute:: "
        keyword_got = extract_keyword(keyword_line)

        self.assertEqual(keyword_got, keyword_want)

        # Check that keyword is not retrieved for bad formats.
        keyword_line = ".. attribute:"
        keyword_got = extract_keyword(keyword_line)

        # Keyword should not be attribute.
        self.assertNotEqual(keyword_want, keyword_got)


if __name__ == '__main__':
    unittest.main()
