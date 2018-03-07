# -*- coding: utf-8 -*-
from aiida_codtools.calculations.cif_base import CifBaseCalculation


class CifCellContentsCalculation(CifBaseCalculation):
    """
    Specific input plugin for cif_cell_contents from cod-tools package
    """

    def _init_internal_params(self):
        super(CifCellContentsCalculation, self)._init_internal_params()

        self._default_parser = 'codtools.cif_cell_contents'
        self._default_commandline_params = ['--print-datablock-name']
