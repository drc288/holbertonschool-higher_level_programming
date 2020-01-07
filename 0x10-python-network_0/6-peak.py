#!/usr/bin/python3
""" 
"""
def find_peak(list_of_integers):
    return peak(list_of_integers, 0, len(list_of_integers) - 1)

"""
"""
def peak(m_li, initial, final):
    if initial is final:
        return initial
    midel = int((initial + final) / 2)
    if m_li[midel] > m_li[midel + 1]:
        return peak(m_li, initial, midel)
    return peak(m_li, midel + 1, final)
