class StringUtility:
    def __init__(self, string):
        self.init_string = string
    def __str__(self):
        return self.init_string
    def vowels(self):
        count = 0
        for x in self.init_string:
            if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
                count += 1
        if count < 5: return str(count)
        else: return "many"
    def bothEnds(self):
        if len(self.init_string) >= 2:
            new_string = ""
            for x in range(len(self.init_string)):
                if x < 2:
                    new_string += self.init_string[x]
            for x in range(len(self.init_string)):
                if x >= len(self.init_string) - 2:
                    new_string += self.init_string[x]
            return new_string
        else: return ""
    def fixStart(self):
        if self.init_string != "": first_char = self.init_string[0]
        else: first_char = ""
        on_char_1 = True
        new_string = first_char
        for x in self.init_string:
            if on_char_1 == False:
                if x == first_char:
                    new_string += "*" 
                else: new_string += x
            else:
                on_char_1 = False
        return new_string
    def asciiSum(self):
        sum = 0
        for x in self.init_string:
            sum += ord(x)
        return sum
    def cipher(self):
        length = len(self.init_string)
        new_string = ""
        for x in self.init_string:
            if ord(x) != 32:
                new_x = ord(x) + length
                while new_x > 122 or new_x < 96 and new_x > 90: new_x -= 26
                new_x = chr(new_x)
            else: new_x = x
            new_string += new_x
        return new_string