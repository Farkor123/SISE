import os

for file in os.listdir("/home/farkor123/Desktop/SISE/tests/inputs"):
    filename = ""+file
    filename = filename.replace(".txt", "")
    str = "python3 /home/farkor123/Desktop/SISE/src/solver.py -a dfs -p D R U L" \
    " -i /home/farkor123/Desktop/SISE/tests/inputs/"+file+" -s /home/farkor123/Desktop/SISE/tests/dfs/drul/"+filename+"_solution.txt" \
    " -m /home/farkor123/Desktop/SISE/tests/dfs/drul/"+filename+"_additional.txt"
    os.system(str)

for file in os.listdir("/home/farkor123/Desktop/SISE/tests/inputs"):
    filename = ""+file
    filename = filename.replace(".txt", "")
    str = "python3 /home/farkor123/Desktop/SISE/src/solver.py -a dfs -p L U D R" \
    " -i /home/farkor123/Desktop/SISE/tests/inputs/"+file+" -s /home/farkor123/Desktop/SISE/tests/dfs/ludr/"+filename+"_solution.txt" \
    " -m /home/farkor123/Desktop/SISE/tests/dfs/ludr/"+filename+"_additional.txt"
    os.system(str)

for file in os.listdir("/home/farkor123/Desktop/SISE/tests/inputs"):
    filename = ""+file
    filename = filename.replace(".txt", "")
    str = "python3 /home/farkor123/Desktop/SISE/src/solver.py -a dfs -p L U R D" \
    " -i /home/farkor123/Desktop/SISE/tests/inputs/"+file+" -s /home/farkor123/Desktop/SISE/tests/dfs/lurd/"+filename+"_solution.txt" \
    " -m /home/farkor123/Desktop/SISE/tests/dfs/lurd/"+filename+"_additional.txt"
    os.system(str)

for file in os.listdir("/home/farkor123/Desktop/SISE/tests/inputs"):
    filename = ""+file
    filename = filename.replace(".txt", "")
    str = "python3 /home/farkor123/Desktop/SISE/src/solver.py -a dfs -p R D L U" \
    " -i /home/farkor123/Desktop/SISE/tests/inputs/"+file+" -s /home/farkor123/Desktop/SISE/tests/dfs/rdlu/"+filename+"_solution.txt" \
    " -m /home/farkor123/Desktop/SISE/tests/dfs/rdlu/"+filename+"_additional.txt"
    os.system(str)

for file in os.listdir("/home/farkor123/Desktop/SISE/tests/inputs"):
    filename = ""+file
    filename = filename.replace(".txt", "")
    str = "python3 /home/farkor123/Desktop/SISE/src/solver.py -a dfs -p R D U L" \
    " -i /home/farkor123/Desktop/SISE/tests/inputs/"+file+" -s /home/farkor123/Desktop/SISE/tests/dfs/rdul/"+filename+"_solution.txt" \
    " -m /home/farkor123/Desktop/SISE/tests/dfs/rdul/"+filename+"_additional.txt"
    os.system(str)

for file in os.listdir("/home/farkor123/Desktop/SISE/tests/inputs"):
    filename = ""+file
    filename = filename.replace(".txt", "")
    str = "python3 /home/farkor123/Desktop/SISE/src/solver.py -a dfs -p U L D R" \
    " -i /home/farkor123/Desktop/SISE/tests/inputs/"+file+" -s /home/farkor123/Desktop/SISE/tests/dfs/uldr/"+filename+"_solution.txt" \
    " -m /home/farkor123/Desktop/SISE/tests/dfs/uldr/"+filename+"_additional.txt"
    os.system(str)

for file in os.listdir("/home/farkor123/Desktop/SISE/tests/inputs"):
    filename = ""+file
    filename = filename.replace(".txt", "")
    str = "python3 /home/farkor123/Desktop/SISE/src/solver.py -a dfs -p U L R D" \
    " -i /home/farkor123/Desktop/SISE/tests/inputs/"+file+" -s /home/farkor123/Desktop/SISE/tests/dfs/ulrd/"+filename+"_solution.txt" \
    " -m /home/farkor123/Desktop/SISE/tests/dfs/ulrd/"+filename+"_additional.txt"
    os.system(str)
