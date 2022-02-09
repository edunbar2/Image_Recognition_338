The "results" and "uploads" directory should be added to the "src" directory as well, since these will be the locations the web server will use
to upload the image file and read results from once the script is finished running.

The main script needs to accept two command line arguments:
Argument 1: Path to the target image file. Ex: "./uploads/dogAndCat_upload01.jpg"
Argument 2: Path to write the result file to. Ex: "./results/result01.txt"

Running the "main_behavior_example.py" script will read the image file at the specified location and
then write a result .txt file at the specified location.

Example usage: >>> python main_behavior_example.py ./uploads/dogAndCat_upload01.jpg ./results/result01.txt
