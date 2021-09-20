# -*- coding: utf-8 -*-
# opyright (c) 2020 Warpnet B.V.

import os
import re
from saltlint.linter.rule import Rule
from saltlint.utils import LANGUAGE_SLS


class StateNameRule(Rule):
    id = '215'
    shortdesc = ('State name not follow the full path naming pattern')
    description = ('State name not follow the full path naming pattern')
    severity = 'LOW'
    languages = [LANGUAGE_SLS]
    tags = ['formatting']
    version_added = 'v0.6.1'

    #path = file['path']
    #prefix = path.replace('/', '|').replace('-', '|')

    #basename = os.path.basename(path)
    #regex = re.compile(r"^\w.*:$")
    regex = re.compile(r"^.*$")

    def match(self, file, line):
        return self.regex.search(line)
