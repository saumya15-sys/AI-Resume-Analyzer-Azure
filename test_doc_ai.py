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

with open("Saumya-Arora.pdf", "rb") as f:

    poller = client.begin_analyze_document(
        "prebuilt-read",
        body=f
    )

result = poller.result()

print("\n===== EXTRACTED TEXT =====\n")

for page in result.pages:

    for line in page.lines:

        print(line.content)