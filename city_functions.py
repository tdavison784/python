#!/usr/bin/python


def get_state_info(city, state, population=''):
    """Function to process city and country data
    in a neatly generated format"""
    if population:
        city_info = city + ' ' + state + ' - ' + population
        city_info.title()
    else:
        city_info = city + ' ' + state
        city_info.title()
    return city_info