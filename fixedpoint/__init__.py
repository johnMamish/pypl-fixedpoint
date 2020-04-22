# Copyright (c) 2019-2020, Schweitzer Engineering Laboratories, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of Schweitzer Engineering Laboratories, Inc. nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL SCHWEITZER ENGINEERING LABORATORIES, INC.
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
"""Fixed point arithmetic library."""
__author__ = "Zack Sheffield"
__copyright__ = "2019-2020, Schweitzer Engineering Laboratories, Inc."
__license__ = "BSD"
__credits__ = [
    "Glenn Bethmann",
    "Kayden Scott",
    "Jason Graham",
    "Derek Lautenschlager",
    "Johnny Sim",
]
__maintainer__ = "Zack Sheffield"
__email__ = "zack_sheffield@selinc.com"
__version__ = "1.0.0"

from fixedpoint.fixedpoint import *  # noqa # ignore unused imports
from fixedpoint.functions import *  # noqa # ignore unused imports


class FixedPointError(Exception):
    """Base class for FixedPoint exceptions.

    This allows any warning raised from the FixedPoint object to be caught.
    """


class FixedPointOverflowError(FixedPointError, OverflowError):
    """Issued when overflow occurs."""


class MismatchError(FixedPointError):
    """Issued when properties don't match and arbitration must occur."""


class ImplicitCastError(FixedPointError, FloatingPointError):
    """Issued when casting to a FixedPoint introduces error."""