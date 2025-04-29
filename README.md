# Resume Generator

A desktop app for quickly generating beautiful resumes from YAML files.

Built with:

- Python 3.12+
- PySide6 (GUI)
- Jinja2 (Template engine)
- WeasyPrint (HTML → PDF)
- PyYAML (YAML parsing)

## 📦Project Structure

```yaml
Resume Generator/
├── gui/
│   ├── main_window.py
│   └── preview_window.py
├── pdf/                  # Output PDFs
├── resumes/              # Input YAML files
├── templates/            # HTML/CSS Templates
├── pdf_generator.py      # Core functions to render HTML/PDF
├── main.py               # App entry point
└── README.md             # This file
```

## 🚀 Features (WIP)

- [x] Refresh YAML file list in GUI
- [x] Live HTML preview
- [x] Generate PDF with a click
- [x] Logging & Debugging support
- [ ] Command Line Interface (CLI) for batch resume generation
- [ ] Multiple resume templates
- [ ] Edit/save YAML directly from the GUI
- [ ] FastAPI integration for web-based generation

## 🛠️ How to Run

1. Create virtual environment:
   ```bash
   python -m venv venv
   ```
2. Install Requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python main.py
   ```

## 📝 Example YAML Structure

```yaml
target_job_title: Software Engineer
summary: Passionate software engineer with experience building scalable web applications and services.

personal_info:
  - name: John Doe
    email: johndoe@example.com
    number: 123-456-7890
    location: Anytown, USA
    url: linkedin.com/in/johndoe

work_experience:
  - company: ExampleCorp
    title: Backend Developer
    date: Jan 2022 - Present
    achievements:
      - Developed and maintained REST APIs with Python and Flask
      - Improved database query performance by 30% through optimization
      - Collaborated with cross-functional teams on Agile projects

  - company: Webify LLC
    title: Junior Developer
    date: Aug 2020 - Dec 2021
    achievements:
      - Assisted in developing frontend interfaces with React
      - Wrote unit tests to increase code coverage by 20%
      - Participated in code reviews and team stand-ups

certs:
  - name: AWS Certified Developer - Associate
    organization: Amazon Web Services
    issued: June 2023
    cred_id: ABCD-1234

skills:
  - Programming Languages:
      - Python
      - JavaScript
      - Java
  - Frameworks and Tools:
      - Flask
      - React
      - Git
      - Docker
  - Databases:
      - PostgreSQL
      - MongoDB
```

## ✨ Future Ideas

- Cloud storage for YAMLs
- Online editing + generation via FastAPI
- Multiple export formats (PDF, DOCX)

## 📄 License

MIT License.
