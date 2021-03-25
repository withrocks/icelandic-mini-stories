from jinja2 import Template

with open("src/index.md.j2") as fs:
    template = Template(fs.read())
    print(template.render(stories_list=range(1, 61)))
