#!/usr/bin/env python
# -*- coding: utf-8 -*-

# EnPT, EnMAP Processing Tools - A Python package for pre-processing of EnMAP Level-1B data
#
# Copyright (C) 2019  Daniel Scheffler (GFZ Potsdam, daniel.scheffler@gfz-potsdam.de)
#
# This software was developed within the context of the EnMAP project supported
# by the DLR Space Administration with funds of the German Federal Ministry of
# Economic Affairs and Energy (on the basis of a decision by the German Bundestag:
# 50 EE 1529) and contributions from DLR, GFZ and OHB System AG.
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
test_controller
---------------

Tests for `execution.controller` module.
"""

from unittest import TestCase, main
import shutil

from enpt.execution.controller import EnPT_Controller
from enpt.options.config import config_for_testing, config_for_testing_dlr


class Test_EnPT_Controller(TestCase):
    def setUp(self):
        self.CTR = EnPT_Controller(**config_for_testing)

    def tearDown(self):
        # NOTE: ignore_errors deletes the folder, regardless of whether it contains read-only files
        shutil.rmtree(self.CTR.cfg.output_dir, ignore_errors=True)

    def test_run_all_processors(self):
        self.CTR.run_all_processors()


class Test_EnPT_Controller_DLR_testdata(TestCase):
    def setUp(self):
        self.CTR = EnPT_Controller(**config_for_testing_dlr)

    def tearDown(self):
        # NOTE: ignore_errors deletes the folder, regardless of whether it contains read-only files
        shutil.rmtree(self.CTR.cfg.output_dir, ignore_errors=True)

    def test_run_all_processors(self):
        self.CTR.run_all_processors()


if __name__ == '__main__':
    main()
