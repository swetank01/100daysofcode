# board
import random

Pipeline = ["git", "Angular", "Docker", "k8", "Jenkins", "Ansible", "GCP"]

friends = ["shubham", "vanash", "deepu", "akash", "mannu"]

print(friends[random.randint(0, (int(len(friends)) - 1))] + " should learn " + Pipeline[random.randint(0, (int(len(Pipeline)) - 1))])