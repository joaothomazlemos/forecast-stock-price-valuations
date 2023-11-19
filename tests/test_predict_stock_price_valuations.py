#!/usr/bin/env python

"""Tests for `predict_stock_price_valuations` package."""


import unittest
from click.testing import CliRunner

from predict_stock_price_valuations import predict_stock_price_valuations
from predict_stock_price_valuations import cli


class TestPredict_stock_price_valuations(unittest.TestCase):
    """Tests for `predict_stock_price_valuations` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'predict_stock_price_valuations.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
