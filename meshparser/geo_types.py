from dataclasses import dataclass

import numpy as np


@dataclass
class point:
    x: np.float64
    y: np.float64
    z: np.float64


@dataclass
class tri:
    p1: point
    p2: point
    p3: point


@dataclass
class quad:
    p1: point
    p2: point
    p3: point
    p4: point
