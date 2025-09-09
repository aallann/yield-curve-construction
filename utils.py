# -*- coding: utf-8 -*-


import abc
import enum


from typing import Mapping


class frequency(enum.Enum):
    Z = 0
    D = 1
    W = 2
    M = 3
    Q = 4
    S = 5
    A = 6


class convention(enum.Enum):
    A360 = 0
    A365 = 1
    T360 = 2


class rating(enum.Enum):
    AA  = 0
    A   = 1
    BBB = 2
    illegal = 999

    @classmethod
    def _missing_(cls, value):
        return cls.illegal


def credit_spread(r: rating) -> float:
    match (r):
        case (rating.AA):
            return 0.015
        case (rating.A):
            return 0.030
        case (rating.BBB):
            return 0.0060
        case (rating.illegal):
            return 0



