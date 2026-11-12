import contextlib
import io
import unittest

import hello


class HelloTest(unittest.TestCase):
    def test_prints_hello_world(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            line = hello.main([])
        self.assertEqual(line, "Hello, world")
        self.assertEqual(out.getvalue(), "Hello, world\n")


if __name__ == "__main__":
    unittest.main()
