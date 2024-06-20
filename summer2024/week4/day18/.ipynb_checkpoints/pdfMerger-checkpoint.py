import PyPDF2
import sys
import os

merger = PyPDF2.PdfFileMerger()

files = ["/home/donghaeyi/practicing-programming/summer2024/week4/day17/oj_harvey_scholarship_2024-2025.pdf", "/home/donghaeyi/practicing-programming/summer2024/week4/day17/vma_veteran_scholarship_2024-2025.pdf"]
for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)
        print(file)
    
merger.write("MergedFile.pdf")