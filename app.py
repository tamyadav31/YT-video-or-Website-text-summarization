import validators , streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader , UnstructuredURLLoader


#streamlit app 

st.set_page_config(page_title="langchain : summarize the text from yt or website" , page_icon="😊")
st.title=("😊 langchain:summarize text from yt or website")
st.subheader("summarize url")

## get groq api key from the user and url to be summarized 
# with st.sidebar:
#     groq_api_key= st.text_input("groq api key", value="" , type="password")

st.sidebar.title("Settings")
api_key=st.text_input("enter your groq api key :" , type="password")
    
generic_url=st.text_input("url", label_visibility="collapsed")

llm=ChatGroq(groq_api_key=api_key , model_name="Gemma-7b-It")

prompt_template="""
provide summary of the foloowing content in 300 words:
content:{text}


"""

prompt=PromptTemplate(template=prompt_template , input_variables=["text"])


if st.button("summarize the cotent from yt or website "):
    ##validate all the input 
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("please provide the information to get started ")
    elif not validators.url(generic_url):
        st.error("please provide the valid url . it can may be a yt video or website url ")
    else:
        try:
            with st.spinner("waiting ....."):
                ## loading the yt or website data
                if "youtube.com" in generic_url:
                    loader=YoutubeLoader.from_youtube_url(generic_url , add_video_info=True)
                else:
                    loader= UnstructuredURLLoader(urls=[generic_url], ssl_verify=False ,
                                                  headers={ "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
                docs=loader.load()
                
                ## chain for summarization
                chain=load_summarize_chain(llm , chain_type="stuff" , prompt=prompt)
                output_summary=chain.run(docs)
                
                st.success(output_summary)
                
        except Exception as e:
             st.exception(f"exception:{e}")
