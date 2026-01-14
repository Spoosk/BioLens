BioLens is a software that can be used to clean and visualize data packages downloaded from Wildlife Insights.  As of this initial release, it contains 2 python scripts to run the data set, but in the future a proper front end will be implemented.

HOW TO RUN:

1. Make sure essential libraries are installed (pandas, plotly, dash, datetime)
2. Enter datapack filename as input_file in CSV date cleaner (cleans up camera metadata discrepencies) - this will return a _CLEANED file to the root directory
3. Enter the _CLEANED file as the input file on the main script, Trailcam_Grapher.py, run the script, and it should open the dash link automatically, if not just click the localhost link in the terminal and it should open.
