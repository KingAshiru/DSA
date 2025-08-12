class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getHash(word):
            hash_ = [0] * 26
            for char in word:
                hash_[ord(char) - ord("a")] += 1
            return hash_
        keep_hash = {}
        
        for word in strs:
            hash_ = getHash(word)
            keep_hash[tuple(hash_)] = []
                    
        for word in strs:
            hash_ = getHash(word)
            if tuple(hash_) in keep_hash:
                keep_hash[tuple(hash_)].append(word)
        
        return list(keep_hash.values())
