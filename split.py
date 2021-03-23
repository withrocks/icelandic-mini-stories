import sys

f = open(sys.argv[1])

story = 1

for line in f:
    line = line.strip()

    if line == "*{}*".format(story):
        print(line)

        story += 1
        with open("story_{}".format(story), "w") as fs:
            pass



