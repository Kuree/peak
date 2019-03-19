from .peak import Peak
from hwtypes import BitVector


def gen_register(family, T, init=0):
    class Register(Peak):
        def __init__(self):
            self.value: T = init

        def __call__(self, value: T=None, en: family.Bit=1) -> T:
            retvalue = self.value
            if value is not None and en:
                assert value is not None
                self.value = value
            return retvalue
    return Register
