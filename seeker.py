"""
Executable runtime for a Hive Seeker.
Run this on hardware devices that wish to access the
collection of sensors on the Hive network.

Reads network and application information from a user-defined
.yaml file on startup.
"""

import yaml
import argparse

DESCRIPTION = """Starts the Hive Seeker, using network  
               info from user-defined .yaml files."""

USAGE = "seeker.py <network.yaml> <apps.yaml>"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=DESCRIPTION,
                                    usage=USAGE)
    parser.add_argument("network_yaml", help="Network config .yaml file.")
    parser.add_argument("apps_yaml", help="Apps config .yaml file.")
    args = parser.parse_args()

    devices = yaml.load(open(args.network_yaml))
    apps = yaml.load(open(args.apps_yaml))

