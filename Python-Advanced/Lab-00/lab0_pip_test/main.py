# main.py
import numpy as np
import sys


def run_check():
  print("--- Python Check ---")
  print(f"Python Version: {sys.version.split()[0]}")

  try:
    arr = np.array([1, 2, 3])
    print(f"Numpy Version:  {np.__version__}")
    print(f"Numpy Test OK:  {arr.sum() == 6}")
  except ImportError:
    print("Numpy Import FEHLGESCHLAGEN")


if __name__ == "__main__":
  run_check()