from royalty_calculator import RoyaltyCalculator
from eval7 import evaluate, Card, handtype


class Hand:
    def __init__(self, front=None, mid=None, back=None, dead_cards=None):
        self.front = front if front else []
        self.mid = mid if mid else []
        self.back = back if back else []
        self.dead_cards = dead_cards if dead_cards else []

        self.last_update = tuple()

        self._front_score = 0
        self._mid_score = 0
        self._back_score = 0

        self.is_fantasy = 0
        self.is_legal = 0
        self.is_complited = 0

    def add_card(self, card, row):
        if not isinstance(card, Card):
            raise TypeError('Карта должна быть объектом класса eval7.Card')

        if row == 0:
            if len(self.front) > 2:
                raise IndexError('Ряд заполнен!')
            self.front.append(card)
        elif row == 1:
            if len(self.mid) > 4:
                raise IndexError('Ряд заполнен!')
            self.mid.append(card)
        elif row == 2:
            if len(self.back) > 4:
                raise IndexError('Ряд заполнен!')
            self.back.append(card)
        elif row > 2:
            raise IndexError('Введите правильный номер ряда')

    def copy(self):
        return Hand(self.front[:], self.mid[:], self.back[:])

    def get_empty_cells(self):
        return {0: 3 - len(self.front), 1: 5 - len(self.mid), 2: 5 - len(self.back)}

    def evaluate_hand(self):
        self._front_score = evaluate(self.front)
        self._mid_score = evaluate(self.mid)
        self._back_score = evaluate(self.back)

        if len(self.front) == 3 and len(self.mid) == len(self.back) == 5:
            self.is_complited = 1

        if self._front_score < self._mid_score < self._back_score:
            self.is_legal = 1

        if self.is_legal and self._front_score >= 17432576:
            self.is_fantasy = 1

        # print(self._front_score, self._mid_score, self._back_score)

    def total_score(self):
        if not self.is_complited:
            raise Exception('Рука ещё не завершена!')

        return self._front_score + self._mid_score + self._back_score

    def fantasy_score(self):
        if not self.is_complited:
            raise Exception('Рука ещё не завершена!')

        if self.is_legal:
            return RoyaltyCalculator.score_front(self._front_score) + \
                   RoyaltyCalculator.score_mid(self._mid_score) + \
                   RoyaltyCalculator.score_back(self._back_score)
        else:
            return -6

    def is_fantasy_keeping(self):
        return self.is_legal and (self._front_score >= 50331648 or
                                    self._mid_score >= 100667392 or
                                    self._back_score >= 117444608)

    def print_hand(self):
        if self.is_complited and self.is_legal:
            print("%-35s%-15s%s\n%-34s %-15s%s\n%-34s %-15s%s\n%-34s %-15s%s" % ("Hand", "Rank", "Score",
                list(card.__str__() for card in self.front), handtype(self._front_score), RoyaltyCalculator.score_front(self._front_score),
                list(card.__str__() for card in self.mid), handtype(self._mid_score), RoyaltyCalculator.score_mid(self._mid_score),
                list(card.__str__() for card in self.back), handtype(self._back_score), RoyaltyCalculator.score_back(self._back_score)))
        elif self.is_complited and not self.is_legal:
            print(list(card.__str__() for card in self.front))
            print(list(card.__str__() for card in self.mid))
            print(list(card.__str__() for card in self.back))
            print('Hand mucked! Score: -6')
        else:
            print(list(card.__str__() for card in self.front))
            print(list(card.__str__() for card in self.mid))
            print(list(card.__str__() for card in self.back))
