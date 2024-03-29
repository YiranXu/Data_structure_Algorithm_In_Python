from turtle import position


class Tree:
    """From 'data structure and algorithm in Python' book
    Abstract base class representing a tree structure"""
    #-----nested Position class-------
    class Position:
        """An abstract class representing the location of a single element"""
        def element(self):
            """Return the element stored at this Position"""
            raise NotImplementedError('must be implemented by subclass')
        def __eq__(self,other):
            """Return True if other Positin represents the same location"""
            raise NotImplementedError('must be implemented by subclass')
        def __ne__(self,other):
            """Return True if other does not represent the same location"""
            return not (self==other) #oppposite of __eq__
    #------abstract methods that concrete subclass must support---------
    def root(self):
        """Return Position representing the tree's root (or None if empty)"""
        raise NotImplementedError('must be implemented by subclass')
    def parent(self,p):
        """Return Position representing p's parent (or None if p is root)"""
        raise NotImplementedError('must be implemented by subclass')
    def num_children(self,p):
        """Return the number of children that Position p has."""
        raise NotImplementedError('must be implemented by subclass')
    def children(self,p):
        """Generate an iteration of Positions representing p's childern."""
        raise NotImplementedError('must be implemented by subclass')
    def __len__(self):
        """Return the total number of elements in the tree"""
        raise NotImplementedError('must be implemented by subclass')
    #-----concrete methods implemented in the class -------
    def is_root(self,p):
        """Return True if Position p represents the root of the tree"""
        return self.root()==p
    def is_leaf(self,p):
        """Return True if Position p does not have any children."""
        return self.num_children(p)==0
    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self)==0
    def depth(self,p):
        """
        Return the number of levels separating Position p from the root
        """
        if self.is_root(p):
            return 0
        else:
            return 1+self.depth(self.parent(p))
    def _height1(self):
        """Return height of the tree"""
        #worst case --O(n^2) ---all positions are in one line (every node has only a child)
        return max(self.depth(p) for p in self.position if self.is_leaf(p))
    def _height2(self,p):
        """
        time is linear in size of subtrees (O(n)worst case)
        """
        if self.is_leaf(p):
            return 0
        else:
            return 1+max(self._height2(c) for c in self.children(p))