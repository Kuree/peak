from dataclasses import dataclass
from .. import Bits, Enum, Product
from .cond import Cond
from .mode import Mode
from .lut import Bit, LUT
from .isa import *

# https://github.com/StanfordAHA/CGRAGenerator/wiki/PE-Spec

def lut(bit0_mode=Mode.BYPASS, bit1_mode=Mode.BYPASS, bit2_mode=Mode.BYPASS, \
        bit0_const=0, bit1_const=0, bit2_const=0,
        bits=0):
    return LUT(Bit0_Mode(bit0_mode), bit0_const,
               Bit1_Mode(bit1_mode), bit1_const,
               Bit2_Mode(bit2_mode), bit2_const,
               Bits(8)(bits))

def alu( Op, data_modes=None, data_consts=None ):
    if not data_modes:
        data_modes = [Data_Mode(Mode.BYPASS) for i in range(NUM_INPUTS)]
    if not data_consts:
        data_consts = [Data_Const(0) for i in range(NUM_INPUTS)]
    return ALU(Op(data_modes, data_consts))

def inst(alu, lut, cond=Cond.Z):
    return Inst(alu, lut, cond)

def add():
    return inst(alu(Add),lut())

def sub():
    return inst(alu(Sub),lut())

def and_():
    return inst(alu(And),lut())

def or_():
    return inst(alu(Or),lut())

def xor():
    return inst(alu(XOr),lut())

