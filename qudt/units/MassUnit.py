################################################################################
#
#  Copyright (C) 2019 Garrett Brown
#  This file is part of pyqudt - https://github.com/eigendude/pyqudt
#
#  pyqudt is derived from jQUDT
#  Copyright (C) 2012-2013  Egon Willighagen <egonw@users.sf.net>
#
#  SPDX-License-Identifier: BSD-3-Clause
#  See the file LICENSE for more information.
#
################################################################################

from qudt import Unit
from qudt.ontology import UnitFactory


class MassUnit(object):
    """
    """
    KILOGRAM: Unit = UnitFactory.get_unit('http://qudt.org/vocab/unit#Kilogram')
    GRAM: Unit = UnitFactory.get_unit('http://qudt.org/vocab/unit#Gram')
    MILLIGRAM: Unit = UnitFactory.get_unit('http://www.openphacts.org/units/Milligram')
    MICROGRAM: Unit = UnitFactory.get_unit('http://www.openphacts.org/units/Microgram')
    NANOGRAM: Unit = UnitFactory.get_unit('http://www.openphacts.org/units/Nanogram')
    PICOGRAM: Unit = UnitFactory.get_unit('http://www.openphacts.org/units/Picogram')
    FEMTOGRAM: Unit = UnitFactory.get_unit('http://www.openphacts.org/units/Femtogram')