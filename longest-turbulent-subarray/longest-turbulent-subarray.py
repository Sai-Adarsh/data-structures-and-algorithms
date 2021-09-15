class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        prev = arr[0]
        last = ''
        cnt = 1
        mx = 0
        for i in range(1, len(arr)):
            if prev < arr[i]:
                # Bad case. Start new subarray from last two elements.
                if last == 'lt':
                    mx = max(cnt, mx)
                    cnt = 2
                    prev = arr[i]
                    continue
                last = 'lt'
            elif prev > arr[i]:
                # Bad Case.
                if last == 'gt':
                    mx = max(cnt, mx)
                    cnt = 2
                    prev = arr[i]
                    continue
                last = 'gt'
            else:
                # last == arr[i]. Start new subarray with just current element.
                mx = max(cnt, mx)
                cnt = 1
                prev = arr[i]
                last = ''
                continue
            cnt += 1
            prev = arr[i]

        return max(cnt, mx)