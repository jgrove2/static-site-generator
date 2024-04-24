from util import extract_title
from markdown_to_html import markdown_to_html
import os
import shutil
import glob

def main():
    public_loc = "public"
    static_loc = "static"
    if os.path.exists(public_loc):
        shutil.rmtree(public_loc)
    if os.path.exists(static_loc):
        shutil.copytree(static_loc, public_loc, dirs_exist_ok=True)
    generate_html_templates("", os.listdir(static_loc))

def generate_page(from_path, template_path, dest_path):
    md = open(from_path).read()
    template = open(template_path).read()
    title = extract_title(md)
    split_template = template.split("{{ Title }}")
    template_title = split_template[0] + title + split_template[1]
    split_template = template_title.split("{{ Content }}")
    template_final = split_template[0] + markdown_to_html(md) + split_template[1]
    open(dest_path, "w").write(template_final)

def generate_html_templates(path_dir, dir_list):
    print(path_dir)
    for path in dir_list:
        new_path = f"{path_dir}{path}"
        if os.path.isdir("static/"+new_path):
            print('test')
            generate_html_templates(new_path + "/", os.listdir("static/"+new_path))
        elif os.path.isfile("static/"+new_path):
            if path[-3:] == ".md":
                generate_page("static/"+new_path, "static/template.html", f"public/{path_dir}/{path[:-3]}.html")
main()