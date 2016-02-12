# -*- coding: utf-8 -*-


class ProblemDescriptors(object):

    def __init__(self, size, stockLength, orderLengthLowerBound, orderLengthUpperBound, averageDemand):
        self.size = size
        self.stockLength = stockLength
        self.orderLengthLowerBound = orderLengthLowerBound
        self.orderLengthUpperBound = orderLengthUpperBound
        self.averageDemand = averageDemand

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
