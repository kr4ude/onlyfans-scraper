#!/usr/bin/env python3
"""
__main__.py for Freqtrade
To launch Freqtrade as a module

> python -m freqtrade (with Python >= 3.11)
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    from scraper import system_check
except:
    pass

from freqtrade import main 


if __name__ == "__main__":
    main.main()
