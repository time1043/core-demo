class LimitFieldElement:
    """
    有限域
    order: 域的阶 必须是素数
    num: 具体数字
    """
    def __init__(self, num, order):
        if not (0 <= num <= order - 1): 
            err = f"元素 {num} 数值必须在 0 到 {order-1} 之间"
            raise ValueError(err)
        self.num = num
        self.order = order

    def __repr__(self):
        return f"LimitFieldElement_{self.order}({self.num})"
    
    def __eq__(self, other):
        """ 判断两个有限域元素是否相等 (order num) """
        if other is None:
            return False
        return self.num == other.num and self.order == other.order
    
    def __ne__(self, other):
        """ 判断两个有限域元素是否不相等 (order num) """
        if other is None:
            return True
        return self.num!= other.num or self.order!= other.order
    
    def __add__(self, other):
        """ 有限域加法(普通加法 再求余) """
        if other is None:
            raise ValueError("other element is None")
        if self.order != other.order:
            raise ValueError("two elements are not in the same field")
        
        num = (self.num + other.num) % self.order
        return self.__class__(num, self.order)
        # return LimitFieldElement(num, self.order)

    def __mul__(self, other):
        """ 有限域乘法(普通乘法 再求余) """
        if other is None:
            raise ValueError("other element is None")
        if self.order != other.order:
            raise ValueError("two elements are not in the same field")
        
        num = (self.num * other.num) % self.order
        return self.__class__(num, self.order)
    
    def __pow__(self, power, modulo=None):
        """ 有限域幂运算(普通幂运算 再求余) """
        while power < 0:
            power += self.order  
        
        num = pow(self.num, power, self.order)
        return self.__class__(num, self.order)
    
    def __truediv__(self, other):
        """ 有限域除法(乘法的逆运算 基于费马小定理) """
        if other is None:
            raise ValueError("other element is None")
        if self.order != other.order:
            raise ValueError("two elements are not in the same field")
        
        negative = other ** (self.order - 2)
        num = (self.num * negative.num) % self.order
        return self.__class__(num, self.order)


