class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        res = []

        def f(val,index,c):
            if c>4:
                return
            if c == 4 and index == len(s):
                res.append(val)
            for i in range(1,4):
                if index + i > len(s):
                    break
                
                st = s[index:index+i]
                if(st.startswith("0") and len(st) > 1) or (i == 3 and int(st) >= 256):
                    continue #not possible
                nxt =val + st + ("." if c <3 else "")
                f(nxt,index+i,c+1)
        f("",0,0)
        return res
