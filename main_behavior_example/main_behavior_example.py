import sys
from os.path import exists as file_exists

if len(sys.argv) < 3:
    sys.exit("""Target image filepath OR result filename not specified.
    Example usage: >>> python main_behavior_example.py ./uploads/dogAndCat_upload01.jpg ./results/result01.txt
    """)

# Print Arg1 and Arg2
# print ('Number of arguments:', len(sys.argv), 'arguments.')
# print ('Argument List:', str(sys.argv))

target_image_filepath = sys.argv[1]
results_filepath = sys.argv[2]

if not file_exists(target_image_filepath):
    sys.exit("Target image filepath is incorrect or the file does not exist.")


# IMAGE RECOGNITION CODE HERE


recognized_objects = ["Dog", "Cat"]
joined_list = ",".join(recognized_objects)

with open(results_filepath, 'w') as opened_file:
  opened_file.write(joined_list)