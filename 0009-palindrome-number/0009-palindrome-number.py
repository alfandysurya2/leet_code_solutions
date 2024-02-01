class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        else:
            x_str = str(x)
            x_str_list = [i for i in x_str]
            reversed_list = x_str_list[::-1]
            if reversed_list == x_str_list:
                return True
            else:
                return False