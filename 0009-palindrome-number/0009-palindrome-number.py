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
            if x_str_list[::-1] == x_str_list:
                return True
            else:
                return False