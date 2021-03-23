import sys
import os

input_file = sys.argv[1]
output_dir = sys.argv[2]

f = open(input_file)


story = 0
lines = list()

def work(lines, story):
    content = "\n".join(lines)

    filename = "story_{}".format(story)
    with open(os.path.join(output_dir, filename), "w") as fs:
        fs.write(content)

for line in f:
    line = line.strip()

    if line.startswith("#"):
        if story != 0:
            work(lines, story)

        story += 1
        lines = list()
    else:
        lines.append(line)

work(lines, story)



