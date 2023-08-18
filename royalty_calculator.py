class RoyaltyCalculator():
    @staticmethod
    def score_back(score):
        if score < 67305472:
            return 0
        if 67305472 <= score <= 67895296:
            return 2
        if 84226576 <= score <= 84720279:
            return 4
        if 100667392 <= score <= 101494784:
            return 6
        if 117444608 <= score <= 118272000:
            return 10
        if 134414336 <= score <= 134938624:
            return 15
        if score == 135004160:
            return 25

    @staticmethod
    def score_mid(score):
        if score < 50340096:
            return 0
        if 50340096 <= score <= 51165696:
            return 2
        else:
            return 2 * self.score_back(score)

    @staticmethod
    def score_front(score):
        if score < 17039360:
            return 0
        if 17039360 <= score <= 17088512: # pair 66
            return 1
        if 17104896 <= score <= 17154048: # pair 77
            return 2
        if 17170432 <= score <= 17219584: # pair 88
            return 3
        if 17235968 <= score <= 17285120: # pair 99
            return 4
        if 17301504 <= score <= 17350656: # pair TT
            return 5
        if 17367040 <= score <= 17416192: # pair JJ
            return 6
        if 17432576 <= score <= 17481728: # pair QQ
            return 7
        if 17498112 <= score <= 17547264: # pair KK
            return 8
        if 17563648 <= score <= 17608704: # pair AA
            return 9
        if score == 50331648: # set 222
            return 10
        if score == 50397184: # set 333
            return 11
        if score == 50462720: # set 444
            return 12
        if score == 50528256: # set 555
            return 13
        if score == 50593792: # set 666
            return 14
        if score == 50659328: # set 777
            return 15
        if score == 50724864: # set 888
            return 16
        if score == 50790400: # set 999
            return 17
        if score == 50855936: # set TTT
            return 18
        if score == 50921472: # set JJJ
            return 19
        if score == 50987008: # set QQQ
            return 20
        if score == 51052544: # set KKK
            return 21
        if score == 51118080: # set AAA
            return 22
