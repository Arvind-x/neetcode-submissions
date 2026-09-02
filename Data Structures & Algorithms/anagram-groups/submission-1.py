class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_dict = {}
        for string in strs:
            count = [0]*26
            for j in string:
                count[ord(j) - ord('a')] += 1
            if tuple(count) in final_dict:
                final_dict[tuple(count)].append(string)
            else:
                final_dict[tuple(count)] = [string]

        return list(final_dict.values())


            

        