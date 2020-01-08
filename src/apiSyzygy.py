#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 16:01:23 2020

@author: bernardintheo
"""

import requests


def testFDP(string):
    urlFen = 'https://tablebase.lichess.ovh/standard?fen='+string
    resp = requests.get(urlFen)
    return (resp.json()['checkmate'])



    