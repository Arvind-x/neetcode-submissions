class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for i in nums:
            if i in freqs:
                freqs[i] +=1
            else:
                freqs[i] = 1
        
        list_of_freq = [(freqs[i], i) for i in freqs]

        heap = []

        def sift_up(i):
            while i > 0:
                p = (i-1) // 2
                if heap[i][0] > heap[p][0]:
                    heap[i], heap[p] = heap[p], heap[i]
                    i = p
                else:
                    break
        
        #build_heap
        for i in range(0, len(list_of_freq)):
            heap.append(list_of_freq[i])
            sift_up(i)

        def sift_down(i):
            l = 2*i + 1
            r = 2*i + 2
            largest = i
            if l < len(heap) and heap[l][0] > heap[largest][0]:
                largest = l


            if r < len(heap) and heap[r][0] > heap[largest][0]:
                largest = r



            if i != largest:
                heap[i], heap[largest] = heap[largest], heap[i]
                sift_down(largest)

        listof = []
        for i in range(0, k):
            heap[0], heap[-1] = heap[-1], heap[0]
            listof.append(heap.pop()[1])
            sift_down(0)
        return listof
