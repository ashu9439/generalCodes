def longestCmnSubstr(a: str,b: str)-> str:
    la = len(a)
    lb = len(b)
    t = [[0 for i in range(la+1)] for j in range(lb+1)]
    #print(t)
    lmax = 0
    imax = 0
    jmax = 0
    for i in range(la):
        for j in range(lb):
            if(a[i] == b [j]):
                t[i+1][j+1] = 1 + t[i][j]
            else:
                t[i+1][j+1] = 0
            if(t[i+1][j+1]> lmax):
                lmax = t[i+1][j+1]
                imax,jmax = i+1,j+1
    print(t,lmax,imax,jmax)         
    s =''
    i,j = imax,jmax
    while(t[i][j] != 0):
        s = s + a[i-1]
        i -=1
        j -=1
    return(s,lmax)
#------------------------------------------------------------------------------------------------------

def isStrPalindrom(s: str):
    return s == s[::-1]
    # sr = s[::-1]
    # if(sr == s):
    #     return s
    # return ''

    
def longestPal(s: str)-> str:
    if(len(s) == 1):
        return s
    if(isStrPalindrom(s)):
        return s    
    i = s.rfind(s[0])
    l= ''
    while(i>0):
        if(isStrPalindrom(s[:i+1])):
            l = s[:i+1] 
            break
        i = s[:i].rfind(s[0])
    return(max((longestPal(s[1:]),l), key = len))
