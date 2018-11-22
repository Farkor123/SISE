import os

i=0
for file in os.listdir("/home/farkor123/Desktop/Python/SISE/SISE/tests/inputs"):
    filename = ""+file
    filename = filename.replace(".txt", "")
    str = "python3 /home/farkor123/Desktop/Python/SISE/SISE/src/solver.py astr hamm" \
    " /home/farkor123/Desktop/Python/SISE/SISE/tests/inputs/"+file+" /home/farkor123/Desktop/Python/SISE/SISE/tests/astr/hamm/"+filename+"_solution.txt " \
    "/home/farkor123/Desktop/Python/SISE/SISE/tests/astr/hamm/"+filename+"_additional.txt"
    os.system(str)
    print(i)
    i+=1
