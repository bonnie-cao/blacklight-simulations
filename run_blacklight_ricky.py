#!/usr/bin/env python3

import os
import sys
import re
import glob



def update_input_file(athdf_file, ifile, filename="example.input"):
  import re

  with open(filename, "r") as f:
    text = f.read()

  text = re.sub(
    r"simulation_file\s*=.*",
    f"simulation_file = {athdf_file}",
    text
  )

  text = re.sub(
        r"output_file\s*=.*",
        f"output_file = ./output/dump_{ifile:05d}.npz",
        text
  )

  with open(filename, "w") as f:
    f.write(text)
def extract_index(fname):
    """
    Extract the integer index from filenames like:
    fm_torus.out2.03750.athdf
    """
    match = re.search(r"\.(\d+)\.athdf$", fname)
    if not match:
        raise ValueError(f"Could not extract index from {fname}")
    return int(match.group(1))


def main():
    # Find all .athdf files
    files = glob.glob("*.athdf")

    if not files:
        print("No .athdf files found.")
        return

    # Sort by extracted integer index
    files_sorted = sorted(files, key=extract_index)

    # Extract indices
    indices = [extract_index(f) for f in files_sorted]

    print("Found files:")
    for f, i in zip(files_sorted, indices):
        print(f"{f} -> {i}")

    # Loop and call update_input_file
    for f, ifile in zip(files_sorted, indices):
        print(f"Processing dump {ifile}: {f}") 
        if (os.path.isfile("./output/dump_%05d.npz" %ifile)): continue
        update_input_file(f, ifile, filename="example_simulation.input")
        os.system("./blacklight example_simulation.input")


if __name__ == "__main__":
    main()