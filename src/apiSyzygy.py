#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 16:01:23 2020

@author: bernardintheo
"""

import requests


def testFDP(string,couleur):
    #rnbqkbnr/pp1B1ppp/2p5/4P3/8/6P1/PPPPP2P/RNBQK1NR b - - 0 1
    urlFen = 'https://tablebase.lichess.ovh/standard?fen='+string+" "+couleur+" - - 0 1"
    resp = requests.get(urlFen)
    return (resp.json()['checkmate'])



    