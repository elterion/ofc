# cython: language_level=3, boundscheck=False, wraparound=False

cpdef char score_back(int score):
    cdef char res
    
    if score < 67305472:
        res = 0
    if 67305472 <= score <= 67895296:
        res = 2
    if 84226576 <= score <= 84720279:
        res = 4
    if 100667392 <= score <= 101494784:
        res = 6
    if 117444608 <= score <= 118272000:
        res = 10
    if 134414336 <= score <= 134938624:
        res = 15
    if score == 135004160:
        res = 25
    
    return res

cpdef char score_mid(int score):
    cdef char res
    
    if score < 50340096:
        res = 0
    if 50340096 <= score <= 51165696:
        res = 2
    else:
        res = 2 * score_back(score)
        
    return res

cpdef char score_front(int score):
    cdef char res
    
    if score < 17039360:
        res = 0
    if 17039360 <= score <= 17088512: # pair 66
        res = 1
    if 17104896 <= score <= 17154048: # pair 77
        res = 2
    if 17170432 <= score <= 17219584: # pair 88
        res = 3
    if 17235968 <= score <= 17285120: # pair 99
        res = 4
    if 17301504 <= score <= 17350656: # pair TT
        res = 5
    if 17367040 <= score <= 17416192: # pair JJ
        res = 6
    if 17432576 <= score <= 17481728: # pair QQ
        res = 7
    if 17498112 <= score <= 17547264: # pair KK
        res = 8
    if 17563648 <= score <= 17608704: # pair AA
        res = 9
    if score == 50331648: # set 222
        res = 10
    if score == 50397184: # set 333
        res = 11
    if score == 50462720: # set 444
        res = 12
    if score == 50528256: # set 555
        res = 13
    if score == 50593792: # set 666
        res = 14
    if score == 50659328: # set 777
        res = 15
    if score == 50724864: # set 888
        res = 16
    if score == 50790400: # set 999
        res = 17
    if score == 50855936: # set TTT
        res = 18
    if score == 50921472: # set JJJ
        res = 19
    if score == 50987008: # set QQQ
        res = 20
    if score == 51052544: # set KKK
        res = 21
    if score == 51118080: # set AAA
        res = 22
        
    return res