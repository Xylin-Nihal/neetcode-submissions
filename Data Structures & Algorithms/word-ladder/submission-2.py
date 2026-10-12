
from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        q = deque([(beginWord, 1)])
        visited = {beginWord}
        wordSet = set(wordList)

        while q:
            word, steps = q.popleft()

            if word == endWord:
                return steps

            for nextWord in wordSet:
                diff = 0

                for i in range(len(word)):
                    if word[i] != nextWord[i]:
                        diff += 1

                if diff == 1 and nextWord not in visited:
                    visited.add(nextWord)
                    q.append((nextWord, steps + 1))

        return 0
