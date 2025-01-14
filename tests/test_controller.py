#!/usr/bin/env python
# -*- coding: utf-8 -*-

# EnPT, EnMAP Processing Tool - A Python package for pre-processing of EnMAP Level-1B data
#
# Copyright (C) 2018-2023 Karl Segl (GFZ Potsdam, segl@gfz-potsdam.de), Daniel Scheffler
# (GFZ Potsdam, danschef@gfz-potsdam.de), Niklas Bohn (GFZ Potsdam, nbohn@gfz-potsdam.de),
# Stéphane Guillaso (GFZ Potsdam, stephane.guillaso@gfz-potsdam.de)
#
# This software was developed within the context of the EnMAP project supported
# by the DLR Space Administration with funds of the German Federal Ministry of
# Economic Affairs and Energy (on the basis of a decision by the German Bundestag:
# 50 EE 1529) and contributions from DLR, GFZ and OHB System AG.
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version. Please note the following exception: `EnPT` depends on tqdm, which
# is distributed under the Mozilla Public Licence (MPL) v2.0 except for the files
# "tqdm/_tqdm.py", "setup.py", "README.rst", "MANIFEST.in" and ".gitignore".
# Details can be found here: https://github.com/tqdm/tqdm/blob/master/LICENCE.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
test_controller
---------------

Tests for `execution.controller` module.
"""
from unittest import TestCase
from unittest.mock import patch
import shutil
from glob import glob
import os

from enpt.execution.controller import EnPT_Controller
from enpt.options.config import config_for_testing, config_for_testing_dlr, config_for_testing_water

__author__ = 'Daniel Scheffler'


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


class Test_EnPT_Controller_DLR_testdata_ACWater(TestCase):
    def setUp(self):
        self.CTR = EnPT_Controller(**config_for_testing_water)

    def tearDown(self):
        # NOTE: ignore_errors deletes the folder, regardless of whether it contains read-only files
        shutil.rmtree(self.CTR.cfg.output_dir, ignore_errors=True)

    def test_run_all_processors(self):
        self.CTR.run_all_processors()

        self.assertTrue(glob(os.path.join(self.CTR.cfg.output_dir, '*', 'ENMAP01*-ACOUT_POLYMER_LOGFB.TIF')))
        self.assertTrue(glob(os.path.join(self.CTR.cfg.output_dir, '*', 'ENMAP01*-ACOUT_POLYMER_BITMASK.TIF')))
        self.assertTrue(glob(os.path.join(self.CTR.cfg.output_dir, '*', 'ENMAP01*-ACOUT_POLYMER_LOGCHL.TIF')))
        self.assertTrue(glob(os.path.join(self.CTR.cfg.output_dir, '*', 'ENMAP01*-ACOUT_POLYMER_RGLI.TIF')))
        self.assertTrue(glob(os.path.join(self.CTR.cfg.output_dir, '*', 'ENMAP01*-ACOUT_POLYMER_RNIR.TIF')))
        # TODO: validate pixel values

    @patch('acwater.acwater.polymer_ac_enmap', None)
    def test_run_all_processors_without_acwater_installed(self):
        """Test to run all processors while replacing polymer_ac_enmap with None using mock.patch."""
        self.CTR.run_all_processors()

        self.assertTrue("As a fallback, SICOR is applied to water surfaces instead."
                        in self.CTR.L1_obj.logger.captured_stream)


if __name__ == '__main__':
    import pytest
    pytest.main()
