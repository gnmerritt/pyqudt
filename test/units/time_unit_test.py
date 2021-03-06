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

from qudt.quantity import Quantity
from qudt.units.time import TimeUnit

import unittest


class TimeUnitTest(unittest.TestCase):
    def test(self) -> None:
        hour = TimeUnit.HOUR
        second = TimeUnit.SECOND

        obs = Quantity(1, hour)
        obs2 = obs.convert_to(second)

        self.assertEqual(second, obs2.unit)
        self.assertAlmostEqual(3600, obs2.value)


if __name__ == '__main__':
    unittest.main()
