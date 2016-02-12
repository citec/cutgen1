# -*- coding: utf-8 -*-


class Problem(object):

    def __init__(self, orders=None, stockLength=None):
        self.orders = list(orders or [])
        self.stockLength = stockLength

    def size(self):
        return len(self.orders)

    def getOrder(self, index):
        return index < self.size and self.orders[index] or None

    def addOrder(self, order):
        self.orders += [order]

    def getData(self):
        return [[o.getData() for o in self.orders], self.stockLength]

    def __str__(self):
        return str(self.getData())

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
