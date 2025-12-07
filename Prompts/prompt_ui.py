# # from langchain_openai import ChatOpenAI
# # from dotenv import load_dotenv
# # import streamlit as st
# # from langchain_core.prompts import PromptTemplate,load_prompt

# # load_dotenv()
# # model = ChatOpenAI()

# # st.header('Reasearch Tool')

# # paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

# # style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

# # length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

# # template = load_prompt('template.json')



# # if st.button('Summarize'):
# #     chain = template | model
# #     result = chain.invoke({
# #         'paper_input':paper_input,
# #         'style_input':style_input,
# #         'length_input':length_input
# #     })
# #     st.write(result.content)





# from langchain_community.llms import HuggingFaceEndpoint
# from langchain_core.prompts import PromptTemplate
# from dotenv import load_dotenv
# import streamlit as st

# load_dotenv()

# # HuggingFace free summarization model
# llm = HuggingFaceEndpoint(
#     repo_id="facebook/bart-large-cnn",  # Good for summaries
#     temperature=0.3,
#     max_new_tokens=300,
# )

# st.header("Research Paper Summarizer (HuggingFace)")

# paper_input = st.selectbox(
#     "Select Research Paper Name", 
#     [
#         "Attention Is All You Need", 
#         "BERT: Pre-training of Deep Bidirectional Transformers", 
#         "GPT-3: Language Models are Few-Shot Learners", 
#         "Diffusion Models Beat GANs on Image Synthesis"
#     ]
# )

# style_input = st.selectbox(
#     "Select Explanation Style", 
#     ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
# ) 

# length_input = st.selectbox(
#     "Select Explanation Length", 
#     ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
# )

# # Properly structured prompt (to avoid repetition issue)
# prompt_template = PromptTemplate.from_template("""
# Summarize the research paper "{paper}" in a {length} way.
# Make the explanation {style} and easy to understand for beginners.
# Do not repeat the words 'Research Paper' unnecessarily. 
# Give only the explanation as the answer.
# """)

# if st.button("Summarize"):
#     final_prompt = prompt_template.format(
#         paper=paper_input,
#         style=style_input,
#         length=length_input
#     )
#     response = llm.invoke(final_prompt)
#     st.write("### Summary:")
#     st.write(response)


from dotenv import load_dotenv
import streamlit as st

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

# Gemini Chat Model (choose gemini-1.5-pro or flash)
model = ChatGoogleGenerativeAI(
    model="gemini-pro-latest",  # OR: "gemini-1.5-flash", "gemini-1.5-pro"
    temperature=0.3
)

st.header('Research Tool (Gemini Powered)')

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical"
    ]
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)"
    ]
)

# Load prompt template
# template = load_prompt('template.json')

# if st.button('Summarize'):
#     chain = template | model
#     response = chain.invoke({
#         "paper_input": paper_input,
#         "style_input": style_input,
#         "length_input": length_input
#     })

#     # Gemini returns response.content as a list of pieces, so join safely
#     final_output = response.content if isinstance(response.content, str) else "".join(
#         [p["text"] for p in response.content if "text" in p]
#     )

#     st.write(final_output)

# Properly structured prompt (to avoid repetition issue)
prompt_template = PromptTemplate.from_template("""
Summarize the research paper "{paper}" in a {length} way.
Make the explanation {style} and easy to understand for beginners.
Do not repeat the words 'Research Paper' unnecessarily. 
Give only the explanation as the answer.
""")

if st.button("Summarize"):
    final_prompt = prompt_template.format(
        paper=paper_input,
        style=style_input,
        length=length_input
    )
    response = model.invoke(final_prompt)
    st.write("### Summary:")
    st.write(response.content)
