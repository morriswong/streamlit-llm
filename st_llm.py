import cohere 
import streamlit as st

api_key = st.secrets["API_KEY"]
co = cohere.Client(
  api_key=api_key, # This is your trial API key
) 

st.header('LLM Playground')
st.markdown('---')

# Create two columns of equal width
col1, col2 = st.columns(2)
# Display the prompt in the left column
with col1:
    prompt = st.text_area('Prompt playground', height=500) # Adjusting the height here can help align the columns visually.
    btn = st.button('send')

# Display the result in the right column with some CSS styling to align it properly.
with col2:
    if not prompt:
        st.write('Your response would be showed here')
    elif btn:    
        response = co.chat(
            # chat_history=[...], 
            message=prompt, 
            connectors=[{"id": "web-search"}]
        )
        st.markdown("""<style> .css-1y0tads { margin-top: 30px; } </style>""", unsafe_allow_html=True) # Adjusting the margin-top can help align the columns vertically. 
        st.write(response.text)