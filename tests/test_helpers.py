from docfx_yaml.extension import extract_keyword
from docfx_yaml.extension import indent_code_left
from docfx_yaml.extension import convert_cross_references
from docfx_yaml.extension import search_cross_references

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


    def test_extract_keyword(self):
        # Check that keyword properly gets processed.
        keyword_want = "attribute"

        keyword_line = ".. attribute:: "
        keyword_got = extract_keyword(keyword_line)

        self.assertEqual(keyword_got, keyword_want)

        # Check that keyword is not retrieved for bad formats.
        keyword_line = ".. attribute:"

        # Should raise an exception..
        with self.assertRaises(ValueError):
            keyword_got = extract_keyword(keyword_line)


    def test_convert_cross_references(self):
        # Check that entries correctly turns into cross references.
        keyword_map = {
            "google.cloud.bigquery_storage_v1.types.SplitReadStreamResponse": "",
        }
        current_name = "SplitRepsonse"
        long_name_want = "<xref uid=\"google.cloud.bigquery_storage_v1.types.SplitReadStreamResponse\">google.cloud.bigquery_storage_v1.types.SplitReadStreamResponse</xref>"

        long_name = "google.cloud.bigquery_storage_v1.types.SplitReadStreamResponse"
        long_name_got = convert_cross_references(long_name, current_name, keyword_map)
        self.assertEqual(long_name_got, long_name_want)

        # This should not get processed.
        short_content = "Response message for SplitReadStreamResponse."
        short_content_got = convert_cross_references(short_content, current_name, keyword_map)
        self.assertEqual(short_content_got, short_content)

        long_content_want = "Response message for <xref uid=\"google.cloud.bigquery_storage_v1.types.SplitReadStreamResponse\">google.cloud.bigquery_storage_v1.types.SplitReadStreamResponse</xref>."
        long_content = "Response message for google.cloud.bigquery_storage_v1.types.SplitReadStreamResponse."
        long_content_got = convert_cross_references(long_content, current_name, keyword_map)
        self.assertEqual(long_content_got, long_content_want)

        # Make sure that same entries are not processed twice.
        # The output should not be different.
        current_want = long_content_want
        current = long_content_got
        current_got = convert_cross_references(current, long_name, keyword_map)
        self.assertEqual(current_want, current_got)

        # If shorter version of the current name exists, it should not interfere
        # unless strictly necessary.
        keyword_map["google.cloud.bigquery_storage_v1.types"] = ""
        long_name_got = convert_cross_references(long_name, current_name, keyword_map)
        self.assertEqual(long_name_got, long_name_want)

        shorter_name_want = "<xref uid=\"google.cloud.bigquery_storage_v1.types\">google.cloud.bigquery_storage_v1.types</xref>"
        shorter_name = "google.cloud.bigquery_storage_v1.types"
        shorter_name_got = convert_cross_references(shorter_name, current_name, keyword_map)
        self.assertEqual(shorter_name_got, shorter_name_want)


if __name__ == '__main__':
    unittest.main()
