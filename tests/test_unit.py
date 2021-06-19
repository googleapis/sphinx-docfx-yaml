from docfx_yaml.extension import find_unique_name
from docfx_yaml.extension import disambiguate_toc_name

import unittest

from yaml import load, Loader

class TestGenerate(unittest.TestCase):
    def test_find_unique_name(self):

        entries = {}
        
        # Disambiguate with unique entries.
        entry1_1 = "google.cloud.aiplatform.v1.schema.predict.instance_v1.types"
        entry1_2 = "google.cloud.aiplatform.v1beta2.schema.predict.instance_v1.types"
        want1_1 = "v1.types"
        want1_2 = "v1beta2.types"

        for entry in [entry1_1, entry1_2]:
            for word in entry.split("."):
                if word not in entries:
                    entries[word] = 1
                else:
                    entries[word] += 1

        got1_1 = find_unique_name(entry1_1.split("."), entries)
        got1_2 = find_unique_name(entry1_2.split("."), entries)

        self.assertEqual(want1_1, ".".join(got1_1))
        self.assertEqual(want1_2, ".".join(got1_2))


    def test_disambiguate_toc_name(self):

        want_file = open('tests/yaml_post.yaml', 'r')
        yaml_want = load(want_file, Loader=Loader)

        test_file = open('tests/yaml_pre.yaml', 'r')
        yaml_got = load(test_file, Loader=Loader)
        disambiguate_toc_name(yaml_got)

        want_file.close()
        test_file.close()

        self.assertEqual(yaml_want, yaml_got)

if __name__ == '__main__':
    unittest.main()
