from docfx_yaml.extension import extract_keyword
from docfx_yaml.extension import indent_code_left
from docfx_yaml.extension import convert_cross_references
from docfx_yaml.extension import search_cross_references

import unittest
from parameterized import parameterized

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


    cross_references_testdata = [
        # Testing for normal input.
        [
            "<xref uid=\"google.cloud.bigquery_storage_v1.types.SplitReadStreamResponse\">google.cloud.bigquery_storage_v1.types.SplitReadStreamResponse</xref>",
            "google.cloud.bigquery_storage_v1.types.SplitReadStreamResponse"
        ],
        # Testing for no cross references to convert.
        [
            "Response message for SplitReadStreamResponse.",
            "Response message for SplitReadStreamResponse."
        ],
        # Testing for cross references to convert within longer content.
        [
            "Response message for <xref uid=\"google.cloud.bigquery_storage_v1.types.SplitReadStreamResponse\">google.cloud.bigquery_storage_v1.types.SplitReadStreamResponse</xref>.",
            "Response message for google.cloud.bigquery_storage_v1.types.SplitReadStreamResponse."
        ],
    ]
    @parameterized.expand(cross_references_testdata)
    def test_convert_cross_references(self, content_want, content):
        # Check that entries correctly turns into cross references.
        keyword_map = {
            "google.cloud.bigquery_storage_v1.types.SplitReadStreamResponse": "",
        }
        current_name = "SplitRepsonse"

        content_got = convert_cross_references(content, current_name, keyword_map)
        self.assertEqual(content_got, content_want)


    # Test data used to test for processing already-processed cross references.
    cross_references_short_testdata = [
        [
            "Response message for <xref uid=\"google.cloud.bigquery_storage_v1.types.SplitReadStreamResponse\">google.cloud.bigquery_storage_v1.types.SplitReadStreamResponse</xref>.",
            "Response message for google.cloud.bigquery_storage_v1.types.SplitReadStreamResponse."
        ],
    ]
    @parameterized.expand(cross_references_short_testdata)
    def test_convert_cross_references_twice(self, content_want, content):
        keyword_map = {
            "google.cloud.bigquery_storage_v1.types.SplitReadStreamResponse": "",
        }
        current_name = "SplitRepsonse"

        content_got = convert_cross_references(content, current_name, keyword_map)

        # Make sure that same entries are not processed twice.
        # The output should not be different.
        current = content_got
        current_got = convert_cross_references(current, content, keyword_map)
        self.assertEqual(content_want, current_got)

        # If shorter version of the current name exists, it should not interfere
        # unless strictly necessary.
        keyword_map["google.cloud.bigquery_storage_v1.types"] = ""
        long_name_got = convert_cross_references(content, current_name, keyword_map)
        self.assertEqual(long_name_got, content_want)

        shorter_name_want = "<xref uid=\"google.cloud.bigquery_storage_v1.types\">google.cloud.bigquery_storage_v1.types</xref>"
        shorter_name = "google.cloud.bigquery_storage_v1.types"
        shorter_name_got = convert_cross_references(shorter_name, current_name, keyword_map)
        self.assertEqual(shorter_name_got, shorter_name_want)


if __name__ == '__main__':
    unittest.main()
