# -*- coding: utf-8 -*-
from Order import Order
from Problem import Problem


class ProblemGenerator(object):

    def __init__(self, random, descriptors):
        self.rGen = random
        self.descriptors = descriptors

    def nextProblem(self):
        lengths = self.generateLengths()
        demands = self.generateDemands()

        return self.merge(lengths, demands)

    def generateLengths(self):
        result = []
        lb = self.descriptors.orderLengthLowerBound
        ub = self.descriptors.orderLengthUpperBound

        for i in range(0, self.descriptors.size):
            rValue = self.rGen.nextDouble()
            length = (lb + (ub - lb) * rValue) * self.descriptors.stockLength + rValue
            result.append(int(length))

        return list(sorted(result, reverse=True))

    def generateDemands(self):
        result = []

        rands = []
        for i in range(0, self.descriptors.size):
            rands.append(self.rGen.nextDouble())
        suma = sum(rands)

        totalDemand = self.descriptors.averageDemand * self.descriptors.size
        rest = totalDemand
        for i in range(0, self.descriptors.size - 1):
            demand = totalDemand * rands[i] / suma + 0.5
            result.append(max(1, int(demand)))

            rest -= int(result[i])

        result.append(max(1, rest))

        return result

    def merge(self, lengths, demands):
        problem = Problem(stockLength=self.descriptors.stockLength)
        for i, length in enumerate(lengths):
            if i == len(lengths) - 1 or length != lengths[i + 1]:
                order = Order(length, demands[i])
                problem.addOrder(order)
            else:
                demands[i + 1] += demands[i]

        return problem

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
