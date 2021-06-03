import csv
import os

file_path = os.path.join("Resources", "election_data.csv")
save_path = os.path.join("analysis", "test.txt")
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

with open(save_path,"w") as results:
    results.write(f"total votes:{total}\n")
    for name in all_candidates: 
        results.write(f"{name}: {all_votes[name]}\n")
    # results.write(all_candidates)
    # results.write(all_votes)


