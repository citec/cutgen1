# -*- coding: utf-8 -*-


class PseudoRandom(object):

    def __init__(self, seed=2013):
        self.IA = 16807
        self.IM = 2147483647
        self.IQ = 127773
        self.IR = 2836
        self.seed = seed

    def nextDouble(self):
        am = 1.0 / self.IM
        k = self.seed / self.IQ

        self.seed = self.IA * (self.seed - k * self.IQ) - self.IR * k
        if (self.seed < 0.0):
            self.seed += self.IM

        return am * self.seed

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
