# -*- coding: utf-8 -*-
import unittest

from cutgen.Order import Order
from cutgen.Problem import Problem
from cutgen.ProblemGenerator import ProblemGenerator
from cutgen.ProblemDescriptors import ProblemDescriptors
from cutgen.PseudoRandom import PseudoRandom


class ProblemGeneratorTest(unittest.TestCase):

    def test_ejorSample(self):
        descriptors = ProblemDescriptors(10, 1000, 0.375, 0.625, 50)

        rGen = PseudoRandom(seed=1994)
        pGen = ProblemGenerator(rGen, descriptors)

        firstActual = pGen.nextProblem()
        firstExpected = self.setupFirstProblem(descriptors.stockLength)
        self.assertProblemEquality(firstExpected, firstActual)

        for i in range(2, 150):
            pGen.nextProblem()

        lastActual = pGen.nextProblem()
        lastExpected = self.setupLastProblem(descriptors.stockLength)
        self.assertProblemEquality(lastExpected, lastActual)

    def setupFirstProblem(self, stockLength):
        expected = Problem(stockLength=stockLength)
        expected.addOrder(Order(577, 63))
        expected.addOrder(Order(570, 64))
        expected.addOrder(Order(544, 85))
        expected.addOrder(Order(539, 84))
        expected.addOrder(Order(526, 54))
        expected.addOrder(Order(512, 20))
        expected.addOrder(Order(504, 24))
        expected.addOrder(Order(459, 31))
        expected.addOrder(Order(446, 48))
        expected.addOrder(Order(378, 27))
        return expected

    def setupLastProblem(self, stockLength):
        expected = Problem(stockLength=stockLength)
        expected.addOrder(Order(570, 16))
        expected.addOrder(Order(558, 94))
        expected.addOrder(Order(543, 20))
        expected.addOrder(Order(540, 99))
        expected.addOrder(Order(513, 59))
        expected.addOrder(Order(490, 48))
        expected.addOrder(Order(476, 78))
        expected.addOrder(Order(453, 35))
        expected.addOrder(Order(434, 51))
        return expected

    def assertProblemEquality(self, expected, actual):
        self.assertTrue(actual is not None)

        self.assertEquals(expected.size(), actual.size())
        self.assertEquals(expected.stockLength, actual.stockLength)

        for i in range(0, expected.size()):
            expectedOrder = expected.getOrder(i)
            actualOrder = actual.getOrder(i)

            self.assertEquals(expectedOrder.length, actualOrder.length)
            self.assertEquals(expectedOrder.demand, actualOrder.demand)


if __name__ == '__main__':
    unittest.main()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
