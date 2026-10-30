from collections import namedtuple
from dataclasses import dataclass
from functools import cached_property

import numpy as np
import xraylib
from core import units

MillerIndexes = namedtuple("MillerIndexes", "h k l")

@dataclass
class Crystal:
    crystal: str
    miller_indexes: MillerIndexes | tuple[int,int,int]

    def __post_init__(self):
        self.miller_indexes = MillerIndexes(*self.miller_indexes)
        self.minus_miller_indexes = MillerIndexes(-self.miller_indexes.h,-self.miller_indexes.k,-self.miller_indexes.l)
        self.xraylib_crystal = xraylib.Crystal_GetCrystal(material=self.crystal)

    @cached_property
    def d_spacing(self):
        return xraylib.Crystal_dSpacing(
            self.xraylib_crystal,
            *self.miller_indexes
        )*units.angstrom

    @cached_property
    def atomic_mass(self):
        return xraylib.AtomicWeight(
            self
        )

    @cached_property
    def volume(self):
        return self.xraylib_crystal["volume"]*units.angstrom**3


@dataclass
class DarwinWidthData:
    width_s: float | np.ndarray
    width_p: float | np.ndarray
    resolution_s: float | np.ndarray
    resolution_p: float | np.ndarray
