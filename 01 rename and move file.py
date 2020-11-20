# This code renames a file and moves it to a new folde.

import os

# Pay attention to r before the paths

os.rename(r"C:\Users\Muhammad\Desktop\NewJobsCopy\1.pdf", r"C:\Users\Muhammad\Desktop\NewJobsCopy\1-ad.pdf") # Rename file - If error: You should probably escape the backslashes or use raw strings: "C:\\Users..." or r"C:\Users..."

os.mkdir(r"C:\Users\Muhammad\Desktop\NewJobsCopy\1") # Create a direcory

os.rename(r"C:\Users\Muhammad\Desktop\NewJobsCopy\1-ad.pdf", r"C:\Users\Muhammad\Desktop\NewJobsCopy\1\1-ad.pdf") # Move the file to the new directroy you created above
