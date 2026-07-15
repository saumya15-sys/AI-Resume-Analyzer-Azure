\# 📄 Azure AI Resume Analyzer



An AI-powered Resume Analyzer built using \*\*Azure Document Intelligence\*\*, \*\*Azure AI Foundry (GPT-OSS-120B)\*\* and \*\*Streamlit\*\*.



The application extracts text from uploaded PDF resumes and uses Azure AI to generate professional insights including resume summary, technical skills, strengths, missing skills, and suitable job roles.



\---



\## 🚀 Features



\- 📄 Upload Resume PDF

\- 🔍 Extract text using Azure Document Intelligence

\- 🤖 AI-powered Resume Analysis using Azure AI Foundry

\- 📝 Professional Summary Generation

\- 💻 Technical Skills Identification

\- 💪 Strength Analysis

\- 📉 Missing Skill Detection

\- 🎯 Suitable Job Role Recommendations

\- 🌐 Interactive Streamlit Web Interface



\---



\## 🏗 Architecture



```

&#x20;               Resume PDF

&#x20;                    │

&#x20;                    ▼

&#x20;     Azure Document Intelligence

&#x20;                    │

&#x20;                    ▼

&#x20;         Extracted Resume Text

&#x20;                    │

&#x20;                    ▼

&#x20;Azure AI Foundry (GPT-OSS-120B)

&#x20;                    │

&#x20;                    ▼

&#x20;        AI Resume Analysis

&#x20;                    │

&#x20;                    ▼

&#x20;       Streamlit Web Application

```



\---



\## 🛠 Tech Stack



| Category | Technology |

|----------|------------|

| Language | Python |

| Cloud Platform | Microsoft Azure |

| AI Service | Azure Document Intelligence |

| LLM | Azure AI Foundry (GPT-OSS-120B) |

| SDK | Azure AI SDK, OpenAI SDK |

| Frontend | Streamlit |

| Configuration | python-dotenv |



\---



\## 📂 Project Structure



```

AI-Resume-Analyzer-Azure/

│

├── app.py

├── requirements.txt

├── README.md

├── .gitignore

│

├── utils/

│   ├── document\_parser.py

│   └── resume\_analyzer.py

│

└── screenshots/

&#x20;   ├── home.png

&#x20;   └── result.png

```



\---



\## 📷 Screenshots



\### Home Page



!\[Home](screenshots/home.png)



\---



\### AI Analysis



!\[Result](screenshots/result.png)



\---



\## ⚙️ Installation



Clone the repository



```bash

git clone https://github.com/saumya15-sys/AI-Resume-Analyzer-Azure.git

```



Move into the project directory



```bash

cd AI-Resume-Analyzer-Azure

```



Install dependencies



```bash

pip install -r requirements.txt

```



Create a `.env` file and configure the following variables:



```env

AZURE\_DOC\_ENDPOINT=YOUR\_ENDPOINT



AZURE\_DOC\_KEY=YOUR\_KEY



FOUNDRY\_ENDPOINT=YOUR\_ENDPOINT



FOUNDRY\_API\_KEY=YOUR\_KEY



FOUNDRY\_MODEL=gpt-oss-120b

```



Run the application



```bash

streamlit run app.py

```



\---



\## 🔮 Future Improvements



\- Resume vs Job Description Matching

\- ATS Score Prediction

\- Downloadable PDF Report

\- Resume Ranking

\- Azure AI Search Integration (RAG)

\- Recruiter Dashboard

\- Multi Resume Comparison



\---



\## 📚 Azure Services Used



\- Azure Document Intelligence

\- Azure AI Foundry

\- GPT-OSS-120B

\- Azure AI SDK



\---



\## 👨‍💻 Author



\*\*Saumya Arora\*\*



GitHub: https://github.com/saumya15-sys



\---



⭐ If you found this project useful, consider giving it a star.

