#!/usr/bin/python

# This script is for converting the .ui files produced by Qt Designer into
# Python source code, it requires uic to be installed on your computer.

import os
import sys
import subprocess

# Works on Arch Linux
UIC_DEFAULT_PATH = '/usr/lib/qt6/uic'

if __name__ == '__main__':
  # Override path to uic with one from args if provided.
  uic_path = UIC_DEFAULT_PATH if len(sys.argv) < 2 else sys.argv[1]

  # Make sure path to uic is valid.
  if not os.path.isfile(uic_path):
    sys.stderr.write(f'Error: uic could not be found{os.linesep}')
    sys.exit()

  root_dir = os.path.dirname(os.path.realpath(__file__))
  # Create output directory if needed.
  out_dir = os.path.join(root_dir, 'ui')
  if not os.path.isdir(out_dir): os.mkdir(out_dir)
  
  # Iterate over files in source directory.
  for entry in os.scandir(os.path.join(root_dir, 'designer')):
    if entry.path.endswith('.ui') and entry.is_file():
      out_name = entry.name.replace('.', '_') + '.py'
      out_path = os.path.join(out_dir, out_name)
      # Run uic on the files.
      subprocess.run([
        uic_path,
        '-g',
        'python',
        '-o',
        out_path,
        entry.path
      ], check=True)
