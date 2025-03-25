import streamlit as st
import arxiv
import fitz  # PyMuPDF
import requests
from io import BytesIO
from openai import OpenAI

# ----- Streamlit Config -----
st.set_page_config(page_title="🧠 AI Research Assistant", page_icon="📄")
st.title("🧠 AI Research Assistant")
st.markdown("Enter a research topic to find and summarize top papers from arXiv.")

# ----- OpenAI API Key Input -----
user_api_key = st.sidebar.text_input("🔐 Enter your OpenAI API Key", type="password")

if user_api_key:
    client = OpenAI(api_key=user_api_key)
else:
    st.warning("Please enter your OpenAI API key in the sidebar to continue.")
    st.stop()

# ----- Sidebar Footer -----
st.sidebar.markdown("---")
st.sidebar.markdown("💡 Built with ❤️ by [Avinash](https://aviinashh-ai.vercel.app)")

# ----- Functions -----
def search_arxiv_papers(query, max_results=3):
    client = arxiv.Client()
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )
    return list(client.results(search))

def extract_text_from_pdf(pdf_url):
    try:
        response = requests.get(pdf_url)
        doc = fitz.open(stream=BytesIO(response.content), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text[:15000]  # Trim to fit GPT token limit
    except Exception as e:
        return f"Error extracting PDF: {e}"

def summarize_text(text):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {"role": "system", "content": "You are an AI research assistant. Read the research paper text and provide:"
"1. A detailed summary of the paper (aim for depth, not brevity),"
"2. Key insights, contributions, and techniques,"
"3. Any limitations or future work mentioned."
"Write in a way that helps students or researchers quickly grasp the paper essence."
},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error during summarization: {e}"

# ----- UI -----
query = st.text_input("🔍 Your Research Topic", placeholder="e.g. Bayesian Optimization")

if st.button("Search & Summarize") and query:
    st.write(f"🔍 Searching for: **{query}**")

    with st.spinner("🔎 Fetching papers..."):
        papers = search_arxiv_papers(query)

    for i, paper in enumerate(papers):
        st.markdown(f"### 📄 Paper {i+1}: {paper.title}")
        st.markdown(f"**Authors**: {', '.join(author.name for author in paper.authors)}")
        st.markdown(f"**Published**: {paper.published.date()}")
        st.markdown(f"[🔗 View PDF]({paper.pdf_url})")

        with st.spinner("🧠 Extracting and summarizing..."):
            text = extract_text_from_pdf(paper.pdf_url)
            summary = summarize_text(text)

        with st.expander("✨ Summary", expanded=True):
            st.write(summary)

        st.download_button(
            label="⬇️ Download Summary",
            data=summary,
            file_name=f"summary_paper_{i+1}.txt",
            mime="text/plain"
        )

        st.markdown("---")
