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

    def test_name_flag(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            line = hello.main(["--name", "Ada"])
        self.assertEqual(line, "Hello, Ada")
        self.assertEqual(out.getvalue(), "Hello, Ada\n")

    def test_shout_prints_capitals(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            line = hello.main(["--shout"])
        self.assertEqual(line, "HELLO, WORLD")
        self.assertEqual(out.getvalue(), "HELLO, WORLD\n")


if __name__ == "__main__":
    unittest.main()
