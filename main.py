import pyperclip
from parser import extract_text_from_pdf
from analyzer import calculate_similarity, skill_analysis
from tkinter import Tk, filedialog

# Function to get resume text
def get_resume_text():
    # Hide the main tkinter window
    root = Tk()
    root.withdraw()

    # Open file dialog to select resume
    resume_path = filedialog.askopenfilename(
        title="Select Resume PDF",
        filetypes=[("PDF files", "*.pdf")]
    )

    if not resume_path:
        print("No file selected. Exiting.")
        exit()

    # Extract text from the selected resume
    resume_text = extract_text_from_pdf(resume_path)
    return resume_text

# Function to get job description from clipboard
def get_job_description():
    print("Copy the Job Description to your clipboard and then press Enter...")
    input()  # Wait for the user to press Enter after copying

    # Get the job description from the clipboard
    job_description = pyperclip.paste()
    return job_description

def main():
    print("----- Resume Analyzer -----\n")

    # Get resume text
    resume_text = get_resume_text()

    # Get job description from clipboard
    job_description = get_job_description()

    # Analyze the resume and job description
    score = calculate_similarity(resume_text, job_description)
    matched, missing = skill_analysis(resume_text, job_description)

    # Display the results
    print("\n===== Analysis Result =====")
    print("Match Score:", score, "%")
    print("Matched Skills:", matched)
    print("Missing Skills:", missing)

if __name__ == "__main__":
    main()

# pip install pyperclip