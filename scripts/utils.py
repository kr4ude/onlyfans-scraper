"""
Utils functions -
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    from scraper import system_check
except:
    pass


def format_dict(data, attribute=None):
    for key, value in data.items():
        if key != attribute:
            if isinstance(value, dict):
                if any(value.values()):
                    print(f'{key.capitalize()}::')
                    for sub_key, sub_value in value.items():
                        if sub_value:
                            print(f'\t{sub_key.capitalize()}:: {sub_value}')
            elif isinstance(value, list):
                if value:
                    print(f'{key.capitalize()}:: {", ".join(value) if isinstance(value[0], str) else value}')
            else:
                if value is not None:
                    print(f'{key.capitalize()}:: {value}')
