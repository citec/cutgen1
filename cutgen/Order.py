# -*- coding: utf-8 -*-

class Order(object):

    def __init__(self, length, demand):
        self.length = length
        self.demand = demand

    def getData(self):
        return (self.length, self.demand)

    def __str__(self):
        return str(self.getData())

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
