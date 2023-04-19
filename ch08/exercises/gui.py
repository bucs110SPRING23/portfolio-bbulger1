class PowerUp:
    def __init__(self, pnum=1, type="mushroom", moving=True):
        """
        Initialize power up object
        args: pnum [int] id number, type [string] type of power up, moving [boolean] whether or not power up should move
        """
        self.id_num = pnum
        self.type = type
        self.moving = moving

class Block:
    def __init__(self, pnum=1, type="brick", breakable=True, item=None):
        """
        Inititalize block object
        args: pnum [int] block's id number, type [string] whether block is a brick or question mark block, breakable [boolean] whether block can be broken (automatically false for question mark blocks), item [PowerUp] which powerup block contains (if None defaults to coin)
        """
        self.block_num = pnum
        self.type = type
        if type == "brick": self.breakable = breakable
        else: self.breakable = False
        self.item = item

class Level:
    def __init__(self, pnum=1, name="1-1", style="overworld", time=500):
        """
        Initialize level object
        args: pnum [int] level id number, name [string] world and level number, style [string] level style, time [int] allowed time for level
        """
        self.level_id_num = pnum
        self.name = name
        self.style = style
        self.time = time