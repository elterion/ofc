#cython: language_level=3, boundscheck=False, wraparound=False

cpdef tuple get_possible_slots(object hand):
    cdef:
        char front_slots
        char mid_slots
        char back_slots
        
    front_slots = 3 - len(hand.front)
    mid_slots = 5 - len(hand.mid)
    back_slots = 5 - len(hand.back)

    return (0,) * front_slots + (1,) * mid_slots + (2,) * back_slots
