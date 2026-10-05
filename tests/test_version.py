import unittest

import lxml.etree as etree

from app import __version__


class TestVersion(unittest.TestCase):
    def test_version(self):
        self.assertEqual(__version__, "0.1.0")
        self.assertEqual(etree.__version__, "6.0.2")


if __name__ == "__main__":
    unittest.main()
