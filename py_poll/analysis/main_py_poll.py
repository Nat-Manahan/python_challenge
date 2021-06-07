import csv
import os

file_path = os.path.join("..", "Resources", "election_data.csv")
save_path = os.path.join("test_py_poll.txt")
all_candidates = []
all_votes = {}
total = 0
with open(file_path) as election:
    reader = csv.reader(election)
    header = next(reader)
    for row in reader:
        total = total + 1
        curr_candidate = row[2]
        if curr_candidate not in all_candidates:
            all_candidates.append(curr_candidate)
            all_votes[curr_candidate] = 1
        else :
            all_votes[curr_candidate] = all_votes[curr_candidate] + 1
print(f"total votes:{total}")
print(all_candidates)
print(all_votes)

win_count = 0
win_can = ""
for name in all_candidates: 
    if all_votes[name] > win_count:
        win_can= name
        win_count = all_votes[name]

print(f"Total votes:{total}\n")
print("-----\n")
for name in all_candidates: 
    per= round(all_votes[name]/total *100, 2)
    print(f"{name}: ({per}%) {all_votes[name]}\n")
print("-----\n")
print(f"Winner: {win_can}\n")
print("-----\n")

with open(save_path,"w") as results:
    results.write(f"Total votes:{total}\n")
    results.write("-----\n")
    for name in all_candidates: 
        per= round(all_votes[name]/total *100, 2)
        results.write(f"{name}: ({per}%) {all_votes[name]}\n")
    results.write("-----\n")
    results.write(f"Winner: {win_can}\n")
    results.write("-----\n")



