from dotenv import load_dotenv
import os

from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient

load_dotenv()

endpoint = os.getenv("AZURE_DOC_ENDPOINT")
key = os.getenv("AZURE_DOC_KEY")

client = DocumentIntelligenceClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)

def extract_resume_text(pdf_file):

    with open(pdf_file, "rb") as f:

        poller = client.begin_analyze_document(
            "prebuilt-read",
            body=f
        )

    result = poller.result()

    extracted_text = ""

    for page in result.pages:

        for line in page.lines:

            extracted_text += line.content + "\n"

    return extracted_text