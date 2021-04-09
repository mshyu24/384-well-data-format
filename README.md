# 384-well-data-format
Reformats data for 384-well-plate screen to be better suited for plotting

## Setup tl;dr:
1. Download the repository
2. Make a new virtual environment
3. Install requirements
4. Add your files to the folder the script is in (input and output)
5. Run the script

## Setup (click by click, for Mac users):
All things in curly brackets can be replaced with the relevant file name etc.
1. Download the repository (green button on main page)
2. Put the folder somewhere convenient, probably in a folder that doesn't have spaces in its name or your desktop
3. Open Terminal, navigate to that folder (use "cd {directory name}" to go to a particular folder, use "ls" to list what is in the folder you are currently in, use "pwd" to get the path to the folder you're currently in)
4. Navigate into the folder you downloaded
5. Make a new virtual environment (type "python3 -m venv {virtual environment name}")
6. Activate your new virtual environment (type "source {virtual environment name}/bin/activate")
7. Make sure you can run the python script (type "chmod +x pivot_wellplate_data.py")
8. Use pip to install the requirements file (type "pip install -r requirements.txt")

At this point you should be set!
To test your setup, you can use the sample file and the run instructions (move sample file to the same folder as the python script and make a new output folder)

## To run:
python3 pivot_wellplate_data.py {input file name} {output file name}

You will see file read and file written messages print to the command line as the script runs

## Formatting files:
Recommendation: name the files without spaces to avoid issues
Input files should be Excel files
This script will only work if you have complete columns (although you don't need a full plate's worth of data)
There should be 3 columns:
Well Position, Temperature, Fluorescence
(modify the script if you are repurposing for other data, this was written for thermal stability)
Well Position should be in letter number format (e.g. A1, B2, etc)

Output file should be an empty excel file, saved with a name

Put both files in the same folder as the python script and you're good to run!
