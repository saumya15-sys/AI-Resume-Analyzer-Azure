from utils.document_parser import extract_resume_text
from utils.resume_analyzer import analyze_resume

resume_text = extract_resume_text(
    "Saumya-Arora.pdf"
)

print("\nTEXT EXTRACTION COMPLETE\n")

analysis = analyze_resume(
    resume_text
)

print("\n===== AI ANALYSIS =====\n")

print(analysis)