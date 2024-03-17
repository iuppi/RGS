import os

#print the contents of all the files in the src/XXXX directory
def main():
    #change the src_dir to the directory you want to print the contents of
    src_dir = "./src/aid"
    output_file = "./data/output/print_output.txt"

    with open(output_file, 'w') as outfile:
        for filename in os.listdir(src_dir):
            if filename.endswith(".py"):
                with open(os.path.join(src_dir, filename), 'r') as infile:
                    outfile.write(f"\n----- Start of {filename} -----\n")
                    outfile.write(infile.read())
                    outfile.write(f"\n----- End of {filename} -----\n")

if __name__ == "__main__":
    main()