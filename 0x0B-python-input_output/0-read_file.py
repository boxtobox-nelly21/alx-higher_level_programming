#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 20:19:26 2022

@author: Nelson Otieno
"""


def read_file(filename=""):
    """
    Reads the file

    Arguments:
        filename (str): The name of the file to open
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
