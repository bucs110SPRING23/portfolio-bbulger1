class Weapon_Of_Mass_Destruction:
    def __init__(self, pnum=1, coords):
        """
        Initialize the Weapon of Mass Destruction
        args: pnum [int] the weapon's id number, coords [tuple] coordinates of target
        """
        self.wmd_num = pnum
        self.target = coords
        self.hit_target = False