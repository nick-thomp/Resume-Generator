from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import yaml
from datetime import datetime
import os
import re

env = Environment(loader=FileSystemLoader('./templates/'))

def generate_html(template = "basic.html", resume = None):
    if resume == None:
        print("No yaml file given. Going to use default file.")
        with open("resume/sample_yaml.yaml", 'r') as f:
            resume = yaml.safe_load(f)

            f.close()

    template = env.get_template(template)
    
    return template.render(**resume)

def generate_pdf(output_path="./pdf/", html_out=None, target_job=None):
    if target_job:
        base_name = f"{target_job.lower().replace(' ', '_')}_resume"
    else:
        base_name = f"{datetime.now().strftime("%m-%d-%y")}_resume"

    output_path += get_unique_filename(base_name)

    if html_out == None:
        return {"status": "Error", "message": "Missing rendered html. Cannot generate PDF."}
    
    try:
        HTML(string=html_out).write_pdf(output_path)
        return {"status": "Success", "message": f"PDF Generated successfully and saved: {output_path}"}
    except Exception as e:
        return {"status": "Error", "message": f"Exception when generating pdf: {e}"}

def get_unique_filename(base_name, extension=".pdf"):
    number = 1
    new_name = f"{base_name}{extension}"

    while os.path.exists("./pdf/"+new_name):
        new_name = f"{base_name}_{number}{extension}"
        number += 1

    return new_name