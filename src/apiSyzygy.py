#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 16:01:23 2020
@author: bernardintheo
"""

import requests


def testFDP(string,couleur):
    """
    testFDP(string,string) => return Boolean,string
    Function which calls the syzygy API to test if the game is finished
    example of string : "rnbqkbnr/pp1B1ppp/2p5/4P3/8/6P1/PPPPP2P/RNBQK1NR b - - 0 1"
    """
    urlFen = 'https://tablebase.lichess.ovh/standard?fen='+string+"_"+couleur+"_-_-_0_1"
    resp = requests.get(urlFen)
    if resp.status_code == 400 :
        return True,couleur
    return (resp.json()['checkmate']),couleur



    
