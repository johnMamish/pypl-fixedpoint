#!/usr/bin/env python3
# This test was written by a different author and doesn't conform to the quality of the other tests
# in this repository.

import sys
sys.path.insert(1, str(pathlib.Path('./../..').resolve()));
import fixedpoint as uut

# fuzz test square root
for i in range(1000):
    x = uut.FixedPoint(0, m=int(random() * 100)+1, n=int(random() * 100)+1, signed=0)

    # because we are choosing only numbers that are precisely representable in fixed-point,
    # no error is introduced at these steps.
    x._bits = getrandbits(x._m + x._n + int(x._signed))

    xf = float(x)

    r = x.sqrt()

    err = (math.sqrt(xf)) - float(r)
    if (math.fabs(err) > (1 / (2**(x.n)))):
        print(f"division of sqrt({x.qformat}) has error {err}, greater than 1 lsb")
        print(f"r = {float(r)}, rf = {math.sqrt(xf)}")
