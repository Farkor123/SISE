import os

for file in os.listdir("/home/farkor123/Desktop/SISE/tests/inputs"):
    filename = ""+file
    filename = filename.replace(".txt", "")
    str = "python3 /home/farkor123/Desktop/SISE/src/solver.py -a manh" \
    " -i /home/farkor123/Desktop/SISE/tests/inputs/"+file+" -s /home/farkor123/Desktop/SISE/tests/astr/manh/"+filename+"_solution.txt" \
    " -m /home/farkor123/Desktop/SISE/tests/astr/manh/"+filename+"_additional.txt"
    os.system(str)
