# -*- coding: utf-8 -*-
import sys

from cutgen.ProblemGenerator import ProblemGenerator
from cutgen.ProblemDescriptors import ProblemDescriptors
from cutgen.PseudoRandom import PseudoRandom


if __name__ == '__main__':
    seed = sys.argv[1]
    qtyProblems = len(sys.argv) >= 3 and int(sys.argv[2]) or 1

    descriptors = ProblemDescriptors(10, 1000, 0.375, 0.625, 50)

    rGen = PseudoRandom(seed=1994)
    pGen = ProblemGenerator(rGen, descriptors)

    for i in range(0, qtyProblems):
        firstActual = pGen.nextProblem()
        print "Problem %04d: %s" % (i, firstActual)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
