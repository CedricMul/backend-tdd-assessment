#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo

# Your test case class goes here
class TestEcho(unittest.TestCase):
    def setUp(self):
        self.parser = echo.create_parser()
    
    def test_upper_long(self):
        args = ["--upper", "hello"]
        #namespace = self.parser.parse_args(args)
        #self.assertTrue(namespace.upper)
        result = echo.main(args)
        self.assertEquals(result, "HELLO")

    def test_upper_short(self):
        args = ["-u", 'hello']
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.upper)
        result = echo.main(args)
        self.assertEquals(result, "HELLO")
    
    # def test_help(self):
    #     # Run the command `python ./echo.py -h` in a separate process, then
    #     # collect it's output.
    #     process = subprocess.Popen(
    #         ["python", "./echo.py", "-h"],
    #         stdout=subprocess.PIPE)
    #     stdout, _ = process.communicate()
    #     with open("USAGE") as f:
    #         usage = f.read()

    #     self.assertEquals(stdout, usage)

    def test_lower_short(self):
        args = ["-l", "HELLO"]
        #namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.lower)
        result = echo.main(args)
        self.assertEquals(result, 'hello')
    
    def test_lower_long(self):
        args = ["--lower", "HELLO"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.lower)
        result = echo.main(args)
        self.assertEquals(result, 'hello')
    
    def test_title_short(self):
        args = ["-t", "hello world"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.title)
        result = echo.main(args)
        self.assertEquals(result, 'Hello World')
    
    def test_title_long(self):
        args = ['--title', 'hello world']
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.title)
        result = echo.main(args)
        self.assertEquals(result, 'Hello World')

def main():
    TestEcho(echo)


if __name__ == '__main__':
    unittest.main()
