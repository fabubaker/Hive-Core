"""
Executable runtime for a Hive Queen.
Run this on a capable device that can facilitate
communications between Seekers and Providers in a Hive network.

IMPORTANT: There should be ONE Queen per Hive network.
"""

import yaml
import argparse

DESCRIPTION = """Starts the Hive Queen, using network info
                 from user-defined .yaml files."""

USAGE="queen.py <network.yaml>"

if __name__ == "__main__":
   parser = argparse.ArgumentParser(description=DESCRIPTION,
                                    usage=USAGE)
   parser.add_argument("network_yaml", help="Network config .yaml file.")
   args = parser.parse_args()
