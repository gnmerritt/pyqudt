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

from qudt.units.concentration import ConcentrationUnit
from qudt.quantity import Quantity

import unittest


class MolarTest(unittest.TestCase):
    @unittest.skip("TODO<open phacts>")
    def test_electron_volt(self) -> None:
        obs = Quantity(0.000001, ConcentrationUnit.MOLAR)
        obs2 = obs.convert_to(ConcentrationUnit.NANOMOLAR)

        self.assertEqual(ConcentrationUnit.NANOMOLAR, obs2.unit)
        self.assertAlmostEqual(1000, obs2.value)


if __name__ == '__main__':
    unittest.main()
