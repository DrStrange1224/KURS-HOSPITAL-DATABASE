import os
import subprocess

source_dir = '.\\uis\\'
output_dir = '.\\py_uis\\'

for filename in os.listdir(source_dir):
    if filename.endswith('.ui'):
        input_file = os.path.join(source_dir, filename)
        output_file = os.path.join(output_dir, filename.replace('.ui', '.py'))
        subprocess.run(['pyside6-uic', input_file, '-o', output_file])
