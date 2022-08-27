import os
import sys
data_dir = os.path.realpath("Data")
file_path = os.path.join(os.path.dirname(__file__), '..', '..')
sys.path.insert(0, os.path.abspath(file_path))
