from docfx_yaml.extension import find_unique_name
from docfx_yaml.extension import disambiguate_toc_name
from docfx_yaml.extension import _resolve_reference_in_module_summary
from docfx_yaml.extension import REF_PATTERN
from docfx_yaml.extension import REF_PATTERN_LAST

import unittest

from yaml import load, Loader

class TestGenerate(unittest.TestCase):
    def test_find_unique_name(self):

        entries = {}
        
        # Disambiguate with unique entries.
        entry1 = "google.cloud.aiplatform.v1.schema.predict.instance_v1.types"
        entry2 = "google.cloud.aiplatform.v1beta2.schema.predict.instance_v1.types"
        want1 = "v1.types"
        want2 = "v1beta2.types"

        for entry in [entry1, entry2]:
            for word in entry.split("."):
                if word not in entries:
                    entries[word] = 1
                else:
                    entries[word] += 1

        got1 = find_unique_name(entry1.split("."), entries)
        got2 = find_unique_name(entry2.split("."), entries)

        self.assertEqual(want1, ".".join(got1))
        self.assertEqual(want2, ".".join(got2))


    def test_disambiguate_toc_name(self):

        want_file = open('tests/yaml_post.yaml', 'r')
        yaml_want = load(want_file, Loader=Loader)

        test_file = open('tests/yaml_pre.yaml', 'r')
        yaml_got = load(test_file, Loader=Loader)
        disambiguate_toc_name(yaml_got)

        want_file.close()
        test_file.close()

        self.assertEqual(yaml_want, yaml_got)


    def test_reference_in_summary(self):
        lines_got = """
If a ``stream`` is attached to this download, then the downloaded
resource will be written to the stream.

Args:
    transport (~requests.Session): A ``requests`` object which can
        make authenticated requests.

    timeout (Optional[Union[float, Tuple[float, float]]]):
        The number of seconds to wait for the server response.
        Depending on the retry strategy, a request may be repeated
        several times using the same timeout each time.

        Can also be passed as a tuple (connect_timeout, read_timeout).
        See :meth:`requests.Session.request` documentation for details.

Returns:
    ~requests.Response: The HTTP response returned by ``transport``.

Raises:
    ~google.resumable_media.common.DataCorruption: If the download's
        checksum doesn't agree with server-computed checksum.
    ValueError: If the current :class:`Download` has already
        finished.
"""
        lines_got = lines_got.split("\n")

        PATTERNS = [REF_PATTERN, REF_PATTERN_LAST]
        for PATTERN in PATTERNS:
            lines_got = _resolve_reference_in_module_summary(PATTERN, lines_got)

        lines_want = """
If a ``stream`` is attached to this download, then the downloaded
resource will be written to the stream.

Args:
    transport (<xref:Session>): A ``requests`` object which can
        make authenticated requests.

    timeout (Optional[Union[float, Tuple[float, float]]]):
        The number of seconds to wait for the server response.
        Depending on the retry strategy, a request may be repeated
        several times using the same timeout each time.

        Can also be passed as a tuple (connect_timeout, read_timeout).
        See <xref:requests.Session.request> documentation for details.

Returns:
    <xref:Response>: The HTTP response returned by ``transport``.

Raises:
    <xref:DataCorruption>: If the download's
        checksum doesn't agree with server-computed checksum.
    ValueError: If the current <xref:Download> has already
        finished.
"""
        lines_want = lines_want.split("\n")

        self.assertEqual(lines_got, lines_want)

if __name__ == '__main__':
    unittest.main()
