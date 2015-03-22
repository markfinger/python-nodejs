import os
import unittest
from nodejs.bindings import (
    node_installed, node_version, node_version_raw, node_run, ensure_node_installed, ensure_node_version_gte,
)
from nodejs.exceptions import MalformedVersionInput, OutdatedDependency
from nodejs.utils import six


class TestNode(unittest.TestCase):
    def test_node_is_installed(self):
        self.assertTrue(node_installed)

    def test_node_version_raw(self):
        self.assertTrue(isinstance(node_version_raw, six.string_types))
        self.assertGreater(len(node_version_raw), 0)

    def test_node_version(self):
        self.assertTrue(isinstance(node_version, tuple))
        self.assertGreaterEqual(len(node_version), 3)

    def test_ensure_node_installed(self):
        ensure_node_installed()

    def test_ensure_node_version_greater_than(self):
        self.assertRaises(MalformedVersionInput, ensure_node_version_gte, 'v99999.0.0')
        self.assertRaises(MalformedVersionInput, ensure_node_version_gte, '99999.0.0')
        self.assertRaises(MalformedVersionInput, ensure_node_version_gte, (None,))
        self.assertRaises(MalformedVersionInput, ensure_node_version_gte, (10,))
        self.assertRaises(MalformedVersionInput, ensure_node_version_gte, (999999999,))
        self.assertRaises(MalformedVersionInput, ensure_node_version_gte, (999999999, 0,))

        self.assertRaises(OutdatedDependency, ensure_node_version_gte, (999999999, 0, 0,))

        ensure_node_version_gte((0, 0, 0,))
        ensure_node_version_gte((0, 9, 99999999,))
        ensure_node_version_gte((0, 10, 0,))

    def test_node_run_returns_output(self):
        stderr, stdout = node_run('--version',)
        stdout = stdout.strip()
        self.assertEqual(stdout, node_version_raw)

    def test_node_run_returns_output_from_script(self):
        stderr, stdout = node_run(os.path.join(os.path.dirname(__file__), 'test.js',))
        self.assertEqual(stdout, 'python-nodejs test\n')