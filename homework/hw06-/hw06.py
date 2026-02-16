""" Homework 6: OOP and Inheritance """

#####################
# Required Problems #
#####################

class Semiring:
    """A base class representing objects that can form a semiring."""

    def add(self, other):
        """Returns the sum of self and other."""
        pass
    
    def mult(self, other):
        """Returns the product of self and other."""
        pass
    
    def negative(self):
        """Returns the additive inverse of self."""
        pass

    def zero(self):
        """Returns the additive identity element."""
        pass

    def one(self):
        """Returns the multiplicative identity element."""
        pass

    # Problem 1.3
    def ntimes(self, n):
        """Returns self added to itself n times.
        >>> base = Integer(3)
        >>> base.ntimes(4)
        12
        >>> p = Polynomial([1, 1])  # Represents x + 1
        >>> p.ntimes(3)
        3x + 3
        """
        assert n >= 0, "n must be a non-negative integer."
        m = self
        if type(m).__name__ == 'Matrix':
            new = [[self.elements[i][j] * n 
                        for j in range(len(self.elements[0]))] 
                        for i in range(len(self.elements))]
            return Matrix(new)
        
        else:
            new = [c * n for c in self.coefficients]
            return Polynomial(new)

    # Problem 1.3
    def power(self, n):
        """Returns self raised to the power of n using repeated multiplication.
        >>> base = Integer(2)
        >>> base.power(3)
        8
        >>> p = Polynomial([1, 1])  # Represents x + 1
        >>> p.power(3)
        x^3 + 3x^2 + 3x + 1
        """
        assert n >= 0, "Exponent must be a positive integer."
        copy = self
        if n == 0:
            return copy.one()
        elif n == 1:
            return copy
        elif type(self).__name__ != 'Matrix':
            res = self.coefficients[:]
            for _ in range(n-1): # 这里重用了之前的mult函数代码
                l1 = len(self.coefficients)
                l2 = len(res)
                m = [0 for _ in range(l1 + l2 -1)]
                
                for i in range(len(m)): 
                    for j in range(max(i - l2 + 1, 0), min(l1 - 1, i) + 1):
                        m[i] += (self.coefficients[j] * res[i-j])
                res = m
            return Polynomial(res)
        else:
            return copy.mult(copy.power(n-1))

# Problem 1.3
def subst_poly(poly, x):
    """Substitutes the Semiring x into the polynomial poly and returns the result.
    For matrices, constant terms are multiplied by the identity matrix.
    >>> poly = Polynomial([1, -2, 3])  # Represents 3x^2 - 2x + 1
    >>> n = Integer(3)
    >>> p = Polynomial([0, 0, 1])  # x^2
    >>> m = Matrix([[1, 2, 3], [2, 1, 1], [2, 3, 3]])
    >>> subst_poly(poly, n)
    22
    >>> subst_poly(poly, m)
    [[32, 35, 36],
     [14, 23, 28],
     [38, 42, 49]]
    >>> subst_poly(poly, p)
    3x^4 - 2x^2 + 1
    """
    # 看题目意思是将x代入到poly中，返回结果
    m = poly.coefficients
    
    def pr(self): # 这个函数是我自己封装进去的，用于打印最终结果，但是可能太繁琐
        m = self.coefficients
        if len(m) == 1:
            return m[0]
        elif len(m) == 2:
            res = ""
            if m[1] > 0:
                res += f"{m[1]}x "
            elif m[1] < 0:
                res += f" - {abs(m[1])}x "
            if m[0] > 0:
                res += f" + {m[0]}"
            elif m[0] < 0:
                res += f"+ {m[0]}"
            else:
                res += "0"
                
        else:
            res = ""
            for i in range(len(m)-1, -1, -1):
                if m[i] == 0:
                    continue
                else:
                    if i == len(m) - 1:
                        if m[-1] != 1:
                            res += f"{m[-1]}x^{i}"
                        else:
                            res += f"x^{i}"
                    elif m[i] < 0:
                        if i == 1:
                            res += f" - {abs(m[i])}x"
                        elif i == 0:
                            res += f" - {abs(m[i])}"
                        else:
                            res += f" - {abs(m[i])}x^{i}"
                    else:
                        if i == 1:
                            res += f" + {m[i]}x"
                        elif i == 0:
                            res += f" + {m[i]}"
                        else:
                            res += f" + {m[i]}x^{i}"
        return res
    
    match type(x).__name__:
        case 'Integer':
            val = x.coefficients[0]
            sum = 0
            for i in range(len(m)):
                sum += pow(val, i) * m[i]
            return sum
        
        case 'Matrix':
            copy = Matrix(x.elements)
            res = Matrix([[0 for _ in range(len(x.elements[0]))] for _ in range(len(x.elements))])
            for i in range(len(m)):
                # print(x.power(i).mul(m[i]).elements)
                c = copy
                if i == 0:
                    res = res.add(c.one().ntimes(m[i]))
                else:
                    if m[i] > 0:
                        res = res.add(c.power(i).ntimes(m[i]))
                    else:
                        res = res.add(c.power(i).ntimes(-m[i]).negative())

            return res
            
        case 'Polynomial':
            res = Polynomial([0])
            for i in range(len(m)):
                if m[i] != 0:
                    t = x.power(i)
                    if m[i] > 0:
                        res = res.add(t.ntimes(m[i]))
                    else:
                        res = res.add(t.ntimes(-m[i]).negative())
            return res
        

# Problem 1.1
class Matrix(Semiring):
    """A class representing 3x3 matrices."""

    def __init__(self, elements):
        """Initializes a 3x3 matrix with the given list of lists.
        >>> Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
        """
        self.elements = elements
    
    def add(self, other):
        """Returns a new Matrix representing the sum of self and other.
        >>> m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        >>> m2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
        >>> m1.add(m2)
        [[10, 10, 10],
         [10, 10, 10],
         [10, 10, 10]]
        """
        m = Matrix([[0,0,0], [0,0,0], [0,0,0]])
        for i in range(len(self.elements)):
            for j in range(len(self.elements[0])):
                m.elements[i][j] += (other.elements[i][j] + self.elements[i][j])
        return m
    
    
    def mult(self, other):
        """Returns a new Matrix representing the product of self and other.
        >>> m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        >>> m2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
        >>> m1.mult(m2)
        [[30, 24, 18],
         [84, 69, 54],
         [138, 114, 90]]
        """
        m = Matrix([[0,0,0], [0,0,0], [0,0,0]])
        for i in range(len(self.elements)):
            for j in range(len(self.elements)):
                for k in range(len(self.elements)):
                    m.elements[i][j] += self.elements[i][k] * other.elements[k][j]
        return m
                    
    
    def negative(self):
        """Returns a new Matrix representing the additive inverse of self.
        >>> m = Matrix([[1, -2, 3], [-4, 5, -6], [7, -8, 9]])
        >>> m.negative()
        [[-1, 2, -3],
         [4, -5, 6],
         [-7, 8, -9]]
        """
        m = Matrix([[0,0,0], [0,0,0], [0,0,0]])
        for i in range(len(self.elements)):
            for j in range(len(self.elements)):
                m.elements[i][j] = -self.elements[i][j]
        return m

    def zero(self):
        """Returns the zero matrix."""
        m = Matrix([[0,0,0], [0,0,0], [0,0,0]])
        return m
    
    def one(self):
        """Returns the identity matrix."""
        m = Matrix([[1,0,0], [0,1,0], [0,0,1]])
        return m
    
    def __repr__(self):
        """Returns the string representation of the matrix.
        You are not supposed to understand this code now.
        """
        rows = [str(row) for row in self.elements]
        return "[{}]".format(",\n ".join(rows))

# Problem 1.2
class Polynomial(Semiring):
    """A class representing polynomials."""

    def __init__(self, coefficients):
        """Initializes a Polynomial with the given list of coefficients.
        The coefficient at index i corresponds to the term with degree i.
        >>> p = Polynomial([1, 2, 3])  # Represents 3x^2 + 2x + 1
        >>> p.coefficients
        [1, 2, 3]
        """
        self.coefficients = coefficients
    
    '''
    def print_res(self): # 没仔细读题自己搓了一遍
        m = self.coefficients
        if len(m) == 1:
            print(m[0])
        elif len(m) == 2:
            res = ""
            if m[1] > 0:
                res += f"{m[1]}x "
            elif m[1] < 0:
                res += f" - {abs(m[1])}x "
            if m[0] > 0:
                res += f" + {m[0]}"
            elif m[0] < 0:
                res += f"+ {m[0]}"
            else:
                res += "0"
            print(res)
                
        else:
            res = ""
            for i in range(len(m)-1, -1, -1):
                if m[i] == 0:
                    continue
                else:
                    if i == len(m) - 1:
                        if m[-1] != 1:
                            res += f"{m[-1]}x^{i}"
                        else:
                            res += f"x^{i}"
                    elif m[i] < 0:
                        if i == 1:
                            res += f" - {abs(m[i])}x"
                        elif i == 0:
                            res += f" - {abs(m[i])}"
                        else:
                            res += f" - {abs(m[i])}x^{i}"
                    else:
                        if i == 1:
                            res += f" + {m[i]}x"
                        elif i == 0:
                            res += f" + {m[i]}"
                        else:
                            res += f" + {m[i]}x^{i}"
            print(res)
    '''
    
    def add(self, other):
        """Returns a new Polynomial representing the sum of self and other.
        >>> p1 = Polynomial([1, 2])      # 2x + 1
        >>> p2 = Polynomial([3, 4, 5])   # 5x^2 + 4x + 3
        >>> p1.add(p2)
        5x^2 + 6x + 4
        """
        n = self
        m = n.coefficients
        l1 = len(m)
        l2 = len(other.coefficients)
        for i in range(min(l1,l2)):
            m[i] += other.coefficients[i]
        if l1 < l2:
            for i in range(l1, l2):
                m.append(other.coefficients[i])
        
        return Polynomial(m)
    
    def mult(self, other):
        """Returns a new Polynomial representing the product of self and other.
        >>> p1 = Polynomial([1, 2])      # 2x + 1
        >>> p2 = Polynomial([3, 4])      # 4x + 3
        >>> p1.mult(p2)
        8x^2 + 10x + 3
        """
        l1 = len(self.coefficients)
        l2 = len(other.coefficients)
        m = [0 for _ in range(l1 + l2 -1)]
        
        for i in range(len(m)): #计算i次幂的系数
            for j in range(max(i - l2 + 1, 0), min(l1 - 1, i) + 1): # 同时满足 0 <= j <= l1-1 && 0 <= i-j <= l2-1
                m[i] += (self.coefficients[j] * other.coefficients[i-j])
        n = Polynomial(m)   
        
        return n
    
    def negative(self):
        """Returns a new Polynomial representing the additive inverse of self.
        >>> p = Polynomial([1, -2, 3])  # 3x^2 - 2x + 1
        >>> p.negative()
        -3x^2 + 2x - 1
        """
        m = self.coefficients
        for i in range(len(m)):
            m[i] = -m[i]

        n = Polynomial(m)   
        
        return n

    def zero(self):
        """Returns the zero polynomial."""
        m = Polynomial([0])
        return m

    def one(self):
        """Returns the identity polynomial."""
        m = Polynomial([1])
        return m

    def __repr__(self):
        """Returns the string representation of the polynomial.
        You are not supposed to understand this code now.
        >>> p = Polynomial([1, 0, 3])  # Represents 1 + 0x + 3x^2
        >>> repr(p)
        '3x^2 + 1'
        """
        terms = []
        for power, coeff in enumerate(self.coefficients):
            if coeff != 0:
                if power == 0:
                    terms.append(f'{coeff}')
                    continue
                elif power == 1:
                    base = 'x'
                else:
                    base = f'x^{power}'

                if coeff == 1:
                    terms.append(base)
                else:
                    terms.append(f'{coeff}{base}')
        return " + ".join(reversed(terms)).replace(" + -", " - ") if terms else "0"

class Integer(Polynomial):
    """A class representing a single integer as a polynomial."""

    def __init__(self, value):
        """Initializes a Integer with the given value.
        >>> Integer(5)
        5
        """
        super().__init__([value])

    def zero(self):
        """Returns the additive identity integer (0)."""
        return Integer(0)

    def one(self):
        """Returns the multiplicative identity integer (1)."""
        return Integer(1)

import random

# Problem 2.1
class Buff:
    """
    Represents a temporary stat modification (buff or debuff).
    Duration decreases each turn until it expires.
    """
    
    def __init__(self, name, attack_bonus=0, defense_bonus=0, duration=3):
        self.name          = name
        self.attack_bonus  = attack_bonus
        self.defense_bonus = defense_bonus
        self.duration      = duration
    
    def decrease_duration(self):
        """Decrease duration by 1. Returns True if expired.
        >>> buff = Buff("Test Buff", attack_bonus=5, defense_bonus=3, duration=2)
        >>> buff.decrease_duration()
        False
        >>> buff.decrease_duration()
        True
        """
        self.duration -= 1
        return self.duration <= 0
    
    def copy(self):
        """Returns a copy of the buff."""
        return Buff(self.name, self.attack_bonus, self.defense_bonus, self.duration)

    def __repr__(self):
        """Returns a string representation of the buff.
        You are not supposed to understand this code now."""
        stats = []
        if self.attack_bonus != 0:
            stats.append(f"ATK {self.attack_bonus:+d}")
        if self.defense_bonus != 0:
            stats.append(f"DEF {self.defense_bonus:+d}")
        stat_str = ", ".join(stats) if stats else "No effect"
        return f"{self.name}: {stat_str} ({self.duration} turns)"


class Equipment:
    """
    Base class for all equipment (weapons and armor).
    Equipment can be equipped by the player to boost stats.
    """
    
    def __init__(self, name, attack_bonus=0, defense_bonus=0, price=0):
        self.name = name
        self.attack_bonus = attack_bonus
        self.defense_bonus = defense_bonus
        self.price = price

    def __repr__(self):
        """Returns a string representation of the equipment.
        You are not supposed to understand this code now."""
        stats = []
        if self.attack_bonus > 0:
            stats.append(f"ATK +{self.attack_bonus}")
        if self.defense_bonus > 0:
            stats.append(f"DEF +{self.defense_bonus}")
        return f"{self.name} ({', '.join(stats)})" if stats else self.name


class Weapon(Equipment):
    """Weapon subclass for attack-focused equipment."""
    
    def __init__(self, name, attack_bonus, price=0):
        """Initialize a Weapon with the given name, attack bonus, and price.
        >>> sword = Weapon("Sword", attack_bonus=10, price=100)
        >>> print(sword)
        Sword (ATK +10)
        >>> print(sword.price)
        100
        """
        super().__init__(name, attack_bonus=attack_bonus, price=price)


class Armor(Equipment):
    """Armor subclass for defense-focused equipment."""
    
    def __init__(self, name, defense_bonus, price=0):
        """Initialize an Armor with the given name, defense bonus, and price.
        >>> shield = Armor("Shield", defense_bonus=8, price=80)
        >>> print(shield)
        Shield (DEF +8)
        >>> print(shield.price)
        80
        """
        super().__init__(name, defense_bonus=defense_bonus, price=price)


# Problem 2.2
class Character:
    """Base class for all characters in the game."""
    
    def __init__(self, name, max_hp, attack, defense):
        self.name         = name
        self.max_hp       = max_hp
        self.current_hp   = max_hp
        self.base_attack  = attack
        self.base_defense = defense
        self.buffs        = []
    
    def is_alive(self):
        return self.current_hp > 0
    
    def get_attack(self):
        """Calculate total attack including buffs.
        >>> char = Character("Student", max_hp=100, attack=20, defense=10)
        >>> buff = Buff("Might", attack_bonus=5, duration=2)
        >>> char.buffs.append(buff)
        >>> char.get_attack()
        25
        """
        b = self.base_attack
        for e in self.buffs:
            b += e.attack_bonus
        return b
    
    def get_defense(self):
        """Calculate total defense including buffs.
        >>> char = Character("Student", max_hp=100, attack=20, defense=10)
        >>> buff = Buff("Shield", defense_bonus=3, duration=2)
        >>> char.buffs.append(buff)
        >>> char.get_defense()
        13
        """
        b = self.base_defense
        for e in self.buffs:
            b += e.defense_bonus
        return b
    
    def take_damage(self, damage):
        """Apply damage, accounting for defense. Returns actual damage taken.
        >>> char = Character("Student", max_hp=100, attack=20, defense=10)
        >>> char.take_damage(25)
        15
        >>> char.current_hp
        85
        """
        if damage <= self.get_defense():
            return 0
        real = damage - self.get_defense()
        if real >= self.current_hp:
            real = self.current_hp
            self.current_hp = 0
            return real
        self.current_hp -= real
        return real
            
    
    def heal(self, amount):
        """Heal the character. Returns actual amount healed."
        >>> char = Character("Student", max_hp=100, attack=20, defense=10)
        >>> char.current_hp = 50
        >>> char.heal(30)
        30
        >>> char.current_hp
        80
        """
        if self.current_hp + amount > self.max_hp:
            heal = self.max_hp - self.current_hp
            self.current_hp = self.max_hp
        else:
            heal = amount
            self.current_hp += heal
        return heal
        
    
    def update_buffs(self):
        """Update all buffs (decrease duration, remove expired).
        >>> char = Character("Student", max_hp=100, attack=20, defense=10)
        >>> buff1 = Buff("Might", attack_bonus=5, duration=1)
        >>> buff2 = Buff("Shield", defense_bonus=3, duration=2)
        >>> char.buffs.extend([buff1, buff2])
        >>> len(char.buffs)
        2
        >>> char.update_buffs()
        >>> len(char.buffs)
        1
        >>> char.update_buffs()
        >>> len(char.buffs)
        0
        """
        
        '''
        错误示范:
        # Decrease duration by 1. Returns True if expired.
        for e in self.buffs:
            f = e.decrease_duration()
            if f == True:
                self.buffs.remove(e)
            print(self.buffs)
        以上这个做法是错误的.
        在遍历列表的同时修改了列表, 导致buff2因为buff1被删, 索引向前移动变成了0, 从而被迭代器跳过了
        '''
        self.buffs = [b for b in self.buffs if not b.decrease_duration()] 
    
    def basic_attack(self, target):
        """Perform a basic attack on target."""
        damage = self.get_attack()
        actual_damage = target.take_damage(damage)
        return f"{self.name} attacks {target.name} for {actual_damage} damage!"
    
    def magic_attack(self, target):
        """Perform a magic attack. Can be overridden by subclasses.
        Return a string describing the attack.
        >>> char = Character("Mage", max_hp=80, attack=15, defense=5)
        >>> enemy = Character("Goblin", max_hp=50, attack=10, defense=2)
        >>> result = char.magic_attack(enemy)
        >>> print(result)
        Mage uses magic attack on Goblin for 20 damage!
        >>> enemy.current_hp
        30
        >>> char.buffs[0]
        Exhaustion: ATK -5, DEF -3 (2 turns)
        """
        actual_damage = target.take_damage(int(self.get_attack() * 1.5))
        self.buffs.append(Buff("Exhaustion", attack_bonus=-5, defense_bonus=-3, duration=2))
        # 这个函数的逻辑是，获得1.5倍伤害，代价是获得Exhaustion的buff
        return f"{self.name} uses magic attack on {target.name} for {actual_damage} damage!"
    

    def __repr__(self):
        """Return a status string for the character.
        You are not supposed to understand this code now."""
        filled = int((self.current_hp / self.max_hp) * 20) if self.max_hp > 0 else 0
        empty = 20 - filled
        hp_bar = f"[{'█' * filled}{'░' * empty}]"
        if self.buffs:
            buff_descriptions = ", \n  ".join(str(buff) for buff in self.buffs)
            buff_info = f" Buffs: [{buff_descriptions}]"
        else:
            buff_info = ""
        return f"{self.name}:\n{hp_bar} ({self.current_hp}/{self.max_hp} HP)\n{buff_info}"


# Problem 2.3
class Player(Character):
    """
    Player character class.
    Extends Character with leveling, equipment, and inventory systems.
    """
    
    def __init__(self, name):
        super().__init__(name, max_hp=100, attack=15, defense=5)
        self.level = 1
        self.experience = 0
        self.gold = 50
        self.equipped_weapon = None
        self.equipped_armor = None
        self.potions = 3
    
    def get_attack(self):
        """Override to include weapon bonus.
        >>> player = Player("Student")
        >>> sword = Weapon("Sword", attack_bonus=10)
        >>> player.equip_weapon(sword)
        >>> player.get_attack()
        25
        """
        atk = self.base_attack 
        if self.equipped_weapon != None:
            atk += self.equipped_weapon.attack_bonus
        return atk
    
    def get_defense(self):
        """Override to include armor bonus.
        >>> player = Player("Student")
        >>> shield = Armor("Shield", defense_bonus=8)
        >>> player.equip_armor(shield)
        >>> player.get_defense()
        13
        """
        dfs = self.base_defense
        if self.equipped_armor != None:
            dfs += self.equipped_armor.defense_bonus
        return dfs
    
    def equip_weapon(self, weapon):
        """Equip a weapon."""
        self.equipped_weapon = weapon
    
    def equip_armor(self, armor):
        """Equip armor."""
        self.equipped_armor = armor
    
    def spend_gold(self, amount):
        """Spend gold. Returns True if successful, False if not enough gold.
        >>> player = Player("Student")
        >>> player.spend_gold(30)
        True
        >>> player.gold
        20
        """
        if amount > self.gold:
            return False
        self.gold -= amount
        return True
    
    def use_potion(self):
        """Use a health potion.
        Return a string description if used, else None.
        >>> player = Player("Student")
        >>> player.current_hp = 40
        >>> player.use_potion()
        'Used a potion! Restored 50 HP.'
        >>> player.current_hp
        90
        >>> player.potions
        2
        """
        if self.potions == 0:
            return None
        self.potions -= 1
        healed = self.max_hp - self.current_hp if (self.max_hp - self.current_hp < 50) else 50
        self.current_hp += healed
        return f"Used a potion! Restored {healed} HP."
    
    def add_experience(self, amount):
        """Add experience and check for level up.
        Return a string if leveled up, else None.
        >>> player = Player("Student")
        >>> player.current_hp = 80
        >>> player.add_experience(60)
        'Level Up! You are now level 2!'
        >>> player.level
        2
        >>> player.current_hp
        120
        >>> player.add_experience(30)
        >>> player.level
        2
        >>> player.add_experience(70)
        'Level Up! You are now level 3!'
        >>> player.level
        3
        >>> player.base_attack
        25
        """
        self.experience += amount
        def judge(exp, level):
            i = level
            e = i * (i+1) * 25
            while exp > e:
                i+=1
                e = i * (i+1) * 25
            return i, i > level
        self.level, is_up = judge(self.experience, self.level)
        if is_up:
            self.max_hp += 20
            self.current_hp = self.max_hp
            self.base_attack += 5
            self.base_defense +=2
            return f"Level Up! You are now level {self.level}!"
        return None


class Enemy(Character):
    """
    Enemy character class.
    Base class for all enemies including TAs and Boss.
    """
    
    def __init__(self, name, max_hp, attack, defense, exp_reward, gold_reward):
        super().__init__(name, max_hp, attack, defense)
        self.exp_reward = exp_reward
        self.gold_reward = gold_reward
        self.description = "A mysterious enemy"
    
    def choose_action(self, player):
        pass

    def need_buff(self):
        if len(self.buffs) == 0:
            return True
        elif len(self.buffs) == 1:
            return self.buffs[0].name == "Exhaustion"
        return False


class TA(Enemy):
    """
    Teaching Assistant enemy class.
    Each TA has a specialty and scales with difficulty.
    """
    
    def __init__(self, name, difficulty, specialty_buff, description):
        hp      = 50 + (difficulty * 15)
        attack  = 8  + (difficulty * 3 )
        defense = 2  + (difficulty * 1 )
        exp     = 30 + (difficulty * 10)
        gold    = 20 + (difficulty * 15)
        
        super().__init__(name, hp, attack, defense, exp, gold)
        self.specialty_buff = specialty_buff 
        self.description    = description
    
    def choose_action(self, player):
        """Choose action based on current HP and buffs."""
        if not any(buff.name == self.specialty_buff['buff'].name for buff in self.buffs):
            self.buffs.append(self.specialty_buff['buff'].copy())
            return f"{self.name} {self.specialty_buff['message']}"
        else:
            rand_action = random.choices([self.basic_attack, self.magic_attack], weights=[70, 30])[0]
            return rand_action(player)


class Boss(Enemy):
    """
    Final boss character with enhanced abilities.
    """
    
    def __init__(self):
        super().__init__(
            name="Professor Lambda",
            max_hp=300,
            attack=25,
            defense=10,
            exp_reward=200,
            gold_reward=500
        )
        self.description = "The legendary SICP professor who has mastered all paradigms!"
        self.phase = 1
        
    
    def choose_action(self, player):
        """Choose action based on current HP and buffs.
        Return a string describing the action taken.
        >>> boss = Boss()
        >>> player = Player("Student")
        >>> boss.current_hp = 210
        >>> boss.choose_action(player)
        'Professor Lambda attacks Student for 20 damage!'
        >>> player.current_hp
        80
        >>> boss.current_hp = 200
        >>> boss.choose_action(player)
        'Professor Lambda enters a frenzy! (ATK +40, DEF -20)'
        >>> boss.choose_action(player)
        'Professor Lambda uses magic attack on Student for 80 damage!'
        >>> player.current_hp
        0
        """
        
        if self.current_hp < self.max_hp * 0.7:
            self.phase = 2
            Buf = Buff("Frenzy", attack_bonus=40, defense_bonus=-20, duration=999)
            # print(self.buffs)
            if self.buffs == []:
                self.buffs.append(Buf)
                return f"{self.name} enters a frenzy! (ATK +40, DEF -20)"
        if self.phase == 2:
            return self.magic_attack(player)
        
        if self.phase == 1: #这一行必须放在最后，否则永远不能升级
            return self.basic_attack(player)

# 玩这个游戏只需要： 
# $ python game.py