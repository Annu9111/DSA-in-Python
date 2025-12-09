# https://leetcode.com/problems/design-hashset/description/?envType=problem-list-v2&envId=hash-table
class MyHashSet(object):

    def __init__(self):
        self.hashset=set()
        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hashset.add(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.hashset:
            self.hashset.remove(key)
        return None    
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        if key in self.hashset:
            return True
        else:
            return False    

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)