from intermol.decorators import *
from abstract_angle import *

class CrossBondBondAngle(AbstractAngle):
    __slots__ = ['r1', 'r2', 'k']

    @accepts_compatible_units(None, None, None,
            units.nanometers, units.nanometers,
            units.kilojoules_per_mole * units.nanometers**(-2))
    def __init__(self, atom1, atom2, atom3, r1, r2, k):
        """
        """
        AbstractAngle.__init__(self, atom1, atom2, atom3)
        self.r1 = r1
        self.r2 = r2
        self.k = k

    def get_parameters(self):
        return (self.atom1, self.atom2, self.atom3, self.r1, self.r2, self.k)

    def __repr__(self):
        print self.atom1+'  '+self.atom2+'  '+ self.atom3+'  '+self.r1+'  '+self.r2+'  '+self.k


    def __str__(self):
        print self.atom1+'  '+self.atom2+'  '+ self.atom3+'  '+self.r1+'   '+ self.r2+'  '+self.k

