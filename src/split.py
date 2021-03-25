import sys
import os

input_file = sys.argv[1]
language = sys.argv[2]

f = open(input_file)

other_language = "is" if language == "en" else "en"

story = 0
lines = list()

def textfile(story):
    return "story_{0:02d}.md".format(story)

def audiofile(story):
    return "story_{0:02d}.mp3".format(story)

def work(lines, story):
    content = "\n".join(lines)

    with open(os.path.join(language, textfile(story)), "w") as fs:
        fs.write(content)

for line in f:
    line = line.strip()

    if line.startswith("#"):
        if story != 0:
            work(lines, story)
            lines = list()
        story += 1

        lines.append(line)
        lines.append("")
        prev_story = ((story - 1 - 1) % 60) + 1
        next_story = (story % 60) + 1

        lines.append("[{0}](../{0}/{1})".format(other_language, textfile(story)))
        lines.append("")

        lines.append("[audio](../audio/{})".format(audiofile(story)))
        lines.append("")

        lines.append("[← prev](../{0}/{1})".format(language, textfile(prev_story)))
        lines.append("[next →](../{0}/{1})".format(language, textfile(next_story)))

    else:
        lines.append(line)

work(lines, story)
