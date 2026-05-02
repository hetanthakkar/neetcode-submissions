class Solution:
    def foreignDictionary(self, words) -> str:
        def findDiff(word1, word2):
            for i in range(len(word1)):
                if i == len(word2):
                    return False
                if word1[i] != word2[i]:
                    return [word1[i], word2[i]]
            return None

        letters = set()
        for w in words:
            for c in w:
                letters.add(c)
        adjacency_list = {k: set() for k in letters}
        indegree = defaultdict(int)
        for i in range(len(words) - 1):
            res = findDiff(words[i], words[i + 1])
            if res is False:
                return ""
            if res is None:
                continue
            if res[1] not in adjacency_list[res[0]]:
                adjacency_list[res[0]].add(res[1])
                indegree[res[1]] += 1

        res = []
        visited = set()
        queue = deque([])
        for key in adjacency_list.keys():
            if indegree[key] == 0:
                queue.append(key)
                visited.add(key)
        while queue:
            popped = queue.popleft()
            res.append(popped)
            for neighbor in adjacency_list[popped]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        if len(res) != len(letters):
            return ""
        return "".join(res)
