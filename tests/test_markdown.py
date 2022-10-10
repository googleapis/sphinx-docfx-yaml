from docfx_yaml.markdown_utils import reformat_markdown_to_html
from docfx_yaml.markdown_utils import _parse_markdown_header
from docfx_yaml.markdown_utils import _extract_header_from_markdown
from docfx_yaml.markdown_utils import _highlight_md_codeblocks
from docfx_yaml.markdown_utils import _clean_image_links
from docfx_yaml.markdown_utils import _prepend_markdown_header


import unittest
from parameterized import parameterized

from yaml import load, Loader

import tempfile

class TestGenerate(unittest.TestCase):
    # Filenames to test markdown syntax highlight with.
    test_markdown_filenames = [
        [
            "tests/markdown_syntax_highlight.md",
            "tests/markdown_syntax_highlight_want.md"
        ],
        [
            "tests/markdown_no_highlight.md",
            "tests/markdown_no_highlight_want.md"
        ],
        [
            "tests/markdown_mixed_highlight.md",
            "tests/markdown_mixed_highlight_want.md"
        ],
    ]
    @parameterized.expand(test_markdown_filenames)
    def test_highlight_md_codeblocks(self, base_filename, want_filename):
        # Test to ensure codeblocks in markdown files are correctly highlighted.

        # Copy the base file we'll need to test.
        with tempfile.NamedTemporaryFile(mode='r+', delete=False) as test_file:
            with open(base_filename) as base_file:
                test_file.write(base_file.read())
                test_file.flush()

            _highlight_md_codeblocks(test_file.name)
            test_file.seek(0)

            with open(want_filename) as mdfile_want:
                self.assertEqual(test_file.read(), mdfile_want.read())


    # Filenames to test prepending Markdown title..
    test_markdown_filenames = [
        [
            "tests/markdown_example_bad_header.md",
            "tests/markdown_example_bad_header_want.md"
        ],
        [
            "tests/markdown_example_h2.md",
            "tests/markdown_example_h2_want.md"
        ],
        [
            "tests/markdown_example_alternate_bad.md",
            "tests/markdown_example_alternate_bad_want.md"
        ],
    ]
    @parameterized.expand(test_markdown_filenames)
    def test_prepend_markdown_header(self, base_filename, want_filename):
        # Ensure markdown titles are correctly prepended.

        # Copy the base file we'll need to test.
        with tempfile.NamedTemporaryFile(mode='r+', delete=False) as test_file:
            with open(base_filename) as base_file:
                # Use same file name extraction as original code.
                file_name = base_file.name.split("/")[-1].split(".")[0].capitalize()
                test_file.write(base_file.read())
                test_file.flush()
                test_file.seek(0)

            _prepend_markdown_header(file_name, test_file)
            test_file.seek(0)

            with open(want_filename) as mdfile_want:
                self.assertEqual(test_file.read(), mdfile_want.read())


    # Filenames to test cleaning up markdown image links.
    test_markdown_filenames = [
        [
            "tests/markdown_example_bad_image_links.md",
            "tests/markdown_example_bad_image_links_want.md"
        ],
    ]
    @parameterized.expand(test_markdown_filenames)
    def test_clean_image_links(self, base_filename, want_filename):
        # Ensure image links are well formed in markdown files.

        # Copy the base file we'll need to test.
        with tempfile.NamedTemporaryFile(mode='r+', delete=False) as test_file:
            with open(base_filename) as base_file:
                # Use same file name extraction as original code.
                file_name = base_file.name.split("/")[-1].split(".")[0].capitalize()
                test_file.write(base_file.read())
                test_file.flush()
                test_file.seek(0)

            _clean_image_links(test_file.name)
            test_file.seek(0)

            with open(want_filename) as mdfile_want:
                self.assertEqual(test_file.read(), mdfile_want.read())


    test_markdown_content = [
        [
            """The resource name or `None`

if no Cloud KMS key was used, or the blob's resource has not been loaded from the server.

For example:
```
    kms_key_name: ID
```
            """,
            """The resource name or <code>None</code>

if no Cloud KMS key was used, or the blob's resource has not been loaded from the server.

For example:
<pre>
    kms_key_name: ID
</pre>
            """,
        ],
    ]
    @parameterized.expand(test_markdown_content)
    def test_reformat_markdown_to_html(self, content, content_want):
        content_got = reformat_markdown_to_html(content)
        self.assertEqual(content_want, content_got)


    test_markdown_content = [
      [
          # Test for simple header_line.
          "# Test header",
          "Test header",
          "",
      ],
      [
          # Test for invalid input.
          "#Test header",
          "",
          "",
      ],
      [
          # Test for invalid input.
          "#  Test header",
          "",
          "",
      ],
      [
          # Test for no header.
          "-->",
          "",
          "limitations under the license.\n",
      ],
      [
          # Test for simple alternate header.
          "============\n",
          "Test header",
          "Test header",
      ],
      [
          # Test for no header.
          "============\n",
          "",
          "",
      ],
      [
          # Test for shorter divider.
          "======\n",
          "Test header",
          "Test header",
      ],
    ]
    @parameterized.expand(test_markdown_content)
    def test_parse_markdown_header(self, header_line, header_line_want, prev_line):
        header_line_got = _parse_markdown_header(header_line, prev_line)

        self.assertEqual(header_line_got, header_line_want)


    test_markdown_filenames = [
        [
            # Check the header for a normal markdown file.
            "tests/markdown_example.md"
        ],
        [
            # The header should be the same even with the license header.
            "tests/markdown_example_header.md"
        ],
    ]
    @parameterized.expand(test_markdown_filenames)
    def test_extract_header_from_markdown(self, markdown_filename):
        # Check the header for markdown files.
        header_line_want = "Test header for a simple markdown file."

        with open(markdown_filename, 'r') as mdfile:
            header_line_got = _extract_header_from_markdown(mdfile)

        self.assertEqual(header_line_got, header_line_want)


    test_markdown_filenames = [
        [
            # Check the header for an alternate header style.
            "tests/markdown_example_alternate.md"
        ],
        [
            # The header should be the same even with the license header.
            "tests/markdown_example_alternate_header.md"
        ],
        [
            # Check the header for an alternate header style.
            "tests/markdown_example_alternate_less.md"
        ],
    ]
    @parameterized.expand(test_markdown_filenames)
    def test_extract_header_from_markdown_alternate_header(self, markdown_filename):
        # Check the header for different accepted styles.
        header_line_want = "This is a simple alternate header"

        with open(markdown_filename, 'r') as mdfile:
            header_line_got = _extract_header_from_markdown(mdfile)

        self.assertEqual(header_line_got, header_line_want)


    test_markdown_filenames = [
        [
            "tests/markdown_example_bad_header.md"
        ],
        [
            "tests/markdown_example_h2.md"
        ],
        [
            "tests/markdown_example_alternate_bad.md"
        ],
    ]
    @parameterized.expand(test_markdown_filenames)
    def test_extract_header_from_markdown_bad_headers(self, markdown_filename):
        # Check that empty string is returned if no valid header is found.
        with open(markdown_filename, 'r') as mdfile:
            header_line_got = _extract_header_from_markdown(mdfile)

        self.assertFalse(header_line_got)


if __name__ == '__main__':
    unittest.main()
