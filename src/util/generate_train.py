import os

image_files = []
os.chdir("img")
for filename in os.listdir(os.getcwd()):
    if not filename.endswith(".txt") and filename != ".DS_Store":
        image_files.append("data/img/" + filename)
        counter += 1
os.chdir("..")

with open("train.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")