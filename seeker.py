"""
Executable runtime for a Hive Seeker.
Run this on hardware devices that wish to access the
collection of sensors on the Hive network.

Reads network information from a user-defined .yaml file on startup.
"""

import yaml
import argparse

DESCRIPTION = """Starts the Hive Seeker, using network  
               info from user-defined .yaml files."""

USAGE = "seeker.py <network.yaml>"

if __name__ == "__main__":
   parser = argparse.ArgumentParser(description=DESCRIPTION,
                                    usage=USAGE)
   parser.add_argument("network_yaml", help="Network config .yaml file.")
   args = parser.parse_args()
