# -*- coding: utf-8 -*-
# opyright (c) 2020 Warpnet B.V.

import unittest

from saltlint.config import Configuration
from saltlint.linter.runner import Runner
from saltlint.linter.collection import RulesCollection
from saltlint.rules.StateNameRule import StateNameRule


class TestStateNameRule(Rule):
    collection = RulesCollection()

    def setUp(self):
        self.collection.register(StateNameRule())

    def test_file_positive(self):
        path = 'tests/test-state-name-success.sls'
        runner = Runner(self.collection, path, Configuration())
        self.assertEqual(2, len(runner.run()))

    def test_file_negative(self):
        path = 'tests/test-state-name-failure.sls'
        runner = Runner(self.collection, path, Configuration())
        self.assertEqual([], runner.run())
