class Solution:
    def minWindow(self, s: str, t: str) -> str:

        track_t = {}
        track_s = {}
        for n in t:
            track_t[n] = track_t.get(n, 0) + 1
            track_s[n] = track_s.get(n, 0)
        
        Left = 0
        min_num = float('inf')
        
        total_n = len(track_t.items())

        tracker = set()
        min_s = ""
        for Right in range(0, len(s)):
            if s[Right] in track_s:
                track_s[s[Right]] += 1
                if track_s[s[Right]] >= track_t[s[Right]]:
                    tracker.add(s[Right])

            print(f'tracker: {tracker}  i: {Right}')
            
            while len(tracker) == total_n:
                print("entered.")
    
                if min_num > (Right - Left + 1):
                    print(s[Left:Right+1])
                    min_num = Right - Left + 1
                    min_s = s[Left:Right+1]               
               
                if s[Left] in track_s:
                    track_s[s[Left]] -= 1
                    if track_s[s[Left]] < track_t[s[Left]]:
                        tracker.remove(s[Left])
                        print(f'in loop: {tracker}')
                
                Left += 1
        
        return min_s