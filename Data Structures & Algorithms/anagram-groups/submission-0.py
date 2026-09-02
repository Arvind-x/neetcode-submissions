class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_list = []
        final_dict = {}
        nums = 0
        for string in strs:
            if tuple(sorted(string)) not in final_dict:
                final_dict[tuple(sorted(string))] = nums
                final_list.append([string])
                nums+=1
            else:
                final_list[final_dict[tuple(sorted(string))]].append(string)
        
        return final_list

            

        