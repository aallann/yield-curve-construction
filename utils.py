# -*- coding: utf-8 -*-


import abc
import enum
import math


class convention(enum.Enum):
    BNESS  = 0
    ACTACT = 1
    ACT360 = 2
    ACT365 = 3

class frequency(enum.Enum):
    continuous = 0
    D = 1
    W = 2
    M = 3
    Q = 4
    S = 5
    A = 6
    zerocoupon = 7


class rating(enum.Enum):
    AA      = 0
    A       = 1
    BBB     = 2


def day_convention(c: convention) -> float:
    match (c):
        case (convention.BNESS):
            return float(252)
        case (convention.ACT360):
            return float(360)
        case (convention.ACT365):
            return float(365)
        case (_):
            return float(365)

def adjusted_rate(rate: float, freq: frequency, 
                  c: convention = convention.ACT360) -> float:
    match (freq):
        case (frequency.zerocoupon):
            return rate
        case (frequency.D):
            days: float = day_convention(c)
            return (1 + (rate / days)) ** days - 1
        case (frequency.W):
            weeks: float = 52
            return (1 + (rate / weeks)) ** weeks - 1
        case (frequency.M):
            months: float = 12
            return (1 + (rate / months)) ** months - 1
        case (frequency.Q):
            quarters: float = 4
            return (1 + (rate / quarters)) ** quarters - 1
        case (frequency.S):
            semesters: float = 2
            return (1 + (rate / semesters)) ** semesters - 1    
        case (frequency.A):
            return rate
        case (frequency.continuous):
            return math.exp(rate) - 1



def credit_spread(r: rating) -> float:
    match (r):
        case (rating.AA):
            return 0.015
        case (rating.A):
            return 0.030
        case (rating.BBB):
            return 0.0060
        case (_):
            return 0




