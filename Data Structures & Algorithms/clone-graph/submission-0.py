class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node is None:
            return None

        mp = {}

        def dfs(curr):

            # Already cloned
            if curr in mp:
                return mp[curr]

            # Create clone
            copy = Node(curr.val)
            mp[curr] = copy

            # Clone neighbors
            for nei in curr.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)