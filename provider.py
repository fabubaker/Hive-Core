"""
Executable runtime for a Hive Provider.
Run this on hardware devices that wish to expose their
sensors to the Hive network.

Reads network and sensor information from a user-defined .yaml file on startup.
"""

import yaml
import argparse

DESCRIPTION = """Starts the Hive Provider, using network and sensor 
               info from user-defined .yaml files."""

USAGE = "provider.py <network.yaml> <sensor.yaml>"

if __name__ == "__main__":
   parser = argparse.ArgumentParser(description=DESCRIPTION,
                                    usage=USAGE)
   parser.add_argument("network_yaml", help="Network config .yaml file.")
   parser.add_argument("sensor_yaml", help="Sensor config .yaml file." )
   args = parser.parse_args()



