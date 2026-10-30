from typing import Sequence, Tuple

import numpy as np
import xraylib

from optlnls2.elements.crystal.types import Crystal, DarwinWidthData


def calc_darwin_width(crystal:Crystal,energy:float | Sequence[float], relative_angle_ratio:float=1, debye_temperature_factor:float=1) -> DarwinWidthData:

    def _darwin_width_single_value(energy:float) -> Tuple[float,float,float,float]:
        
        bragg = xraylib.Bragg_angle(crystal.xraylib_crystal, energy, *crystal.miller_indexes)

        FH = xraylib.Crystal_F_H_StructureFactor(
            crystal.xraylib_crystal,
            energy, *crystal.miller_indexes,
            debye_temperature_factor,
            relative_angle_ratio
        )
        
        FHbar = xraylib.Crystal_F_H_StructureFactor(
            crystal.xraylib_crystal,
            energy,
            *crystal.minus_miller_indexes,
            debye_temperature_factor,
            relative_angle_ratio
        )
        
        C = abs(np.cos(2*bragg))

        # TODO Humberto resolve depois
        dw_s = 1e10 * 2 * (xraylib.R_E / crystal.xraylib_crystal['volume']) * (xraylib.KEV2ANGST * xraylib.KEV2ANGST/ (energy * energy)) * np.sqrt(abs(FH * FHbar)) / np.pi / np.sin(2*bragg)
        dw_p = 1e10 * 2 * C * (xraylib.R_E / crystal.xraylib_crystal['volume']) * (xraylib.KEV2ANGST * xraylib.KEV2ANGST/ (energy * energy)) * np.sqrt(abs(FH * FHbar)) / np.pi / np.sin(2*bragg)

        resolution_s = dw_s/np.tan(bragg)
        resolution_p = dw_p/np.tan(bragg)
        
        return dw_s,dw_p,resolution_s,resolution_p

    if isinstance(energy,(int,float)):
        width_s,width_p,resolution_s,resolution_p = _darwin_width_single_value(energy)

    elif isinstance(energy,(np.ndarray,tuple,list)):
        width_s = np.empty(shape=(len(energy),1))
        width_p = np.empty(shape=(len(energy),1))
        resolution_s = np.empty(shape=(len(energy),1))
        resolution_p = np.empty(shape=(len(energy),1))
        for idx,_energy in enumerate(energy):
            width_s[idx],width_p[idx],resolution_s[idx],resolution_p[idx] =_darwin_width_single_value(_energy)
    else:
        raise ValueError(f"Invalid energy type {type(energy)}")

    return DarwinWidthData(
        width_s = width_s,
        width_p = width_p,
        resolution_s = resolution_s,
        resolution_p = resolution_p
    )