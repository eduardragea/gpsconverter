import os
import subprocess

def convert_gsd_to_gpx(input_folder, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Get a list of all GSD files in the main folder
    gsd_files = [file for file in os.listdir(input_folder) if file.endswith(".gsd")]

    # Convert each GSD file to GPX using GPSBabel
    for gsd_file in gsd_files:
        input_path = os.path.join(input_folder, gsd_file)
        output_path = os.path.join(output_folder, os.path.splitext(gsd_file)[0] + ".gpx")

        # Execute the GPSBabel command
        command = ["D:\GPSBabel\gpsbabel", "-i", "gsd", "-f", input_path, "-o", "gpx", "-F", output_path]
        subprocess.run(command)

if __name__ == "__main__":
    # Specify the input and output folders using absolute paths
    input_folder = r"D:\python projects\GPS\Disk"
    output_folder = r"D:\python projects\GPS\output"

    # Call the function to convert GSD to GPX
    convert_gsd_to_gpx(input_folder, output_folder)
