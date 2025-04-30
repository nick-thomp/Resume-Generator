from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import yaml
from datetime import datetime
import os
import logging

env = Environment(loader=FileSystemLoader('./templates/'))

def generate_html(template = "basic.html", resume = None):
    # If no resume file given then parse sample file
    if resume is None:
        logging.warning("No yaml file found. Going to use sample file")
        try:
            with open("resume/sample.yaml", 'r') as f:
                resume = yaml.safe_load(f)
        except Exception as e:
            logging.error("Failed to load sample.yaml", exc_info=True)
            return {"status": "Error", "message": f"Exception when generating pdf: {e}"}
    # else if resume is given as a str then assume that it is the file and still needs to be parsed
    elif isinstance(resume, str):
        try:
            with open(f"resumes/{resume}", 'r') as f:
                resume = yaml.safe_load(f)
        except Exception as e:
            logging.error(f"Failed to parse yaml file {resume}", exc_info=True)
            return {"status": "Error", "message": f"Failed to parse yaml file {resume}"}

    # Get template that needs to be used in rendering
    try:
        template = env.get_template(template)
    except Exception as e:
        logging.error("Failed to load template '%s'", template, exc_info=True)
        return {"status": "Error", "message": f"Exception when generating pdf: {e}"}
    
    # Render template with resume dictionary (parsed yaml)
    try:
        rendered_template = template.render(**resume)
        return {"status": "Success", "message": rendered_template}
    except Exception as e:
        logging.error("Failed to render template '%s'", template, exc_info=True)
        return {"status": "Error", "message": f"Exception when generating pdf: {e}"}

def generate_pdf(output_path="./pdf/", html_out=None, target_job=None):
    # make sure pdf/ folder exist
    if not os.path.exists('pdf'):
        logging.info("Creating folder for pdf's")
        os.mkdir('pdf')

    # If we have the target job then use that in the name. Otherwise, use the current date
    if target_job:
        base_name = f"{target_job.lower().replace(' ', '_')}_resume"
    else:
        base_name = f"{datetime.now().strftime("%m-%d-%y")}_resume"

    # Append name onto the output path
    output_path += get_unique_filename(base_name)

    if html_out == None:
        logging.error("Cannot generate PDF. Missing rendered HTML")
        return {"status": "Error", "message": "Missing rendered html. Cannot generate PDF."}
    
    try:
        HTML(string=html_out).write_pdf(output_path)
        return {"status": "Success", "message": f"PDF Generated successfully and saved: {output_path}"}
    except Exception as e:
        return {"status": "Error", "message": f"Exception when generating pdf: {e}"}

# use this function to make sure we don't overwrite any existing pdf
def get_unique_filename(base_name, extension=".pdf"):
    number = 1
    new_name = f"{base_name}{extension}"

    while os.path.exists("./pdf/"+new_name):
        new_name = f"{base_name}_{number}{extension}"
        number += 1

    return new_name