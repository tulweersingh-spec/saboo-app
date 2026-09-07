import streamlit as st
import google.generativeai as genai
import random

st.set_page_config(page_title="Saboo Robot", page_icon="🤖")
st.title("🤖 साबू रोबोट (Python Code Debugger)")

# API Key Config
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("API Key सेट करने में समस्या है! कृपया Streamlit Secrets जाँचें।")

# साबू के रैंडम डायलॉग्स
saboo_dialogues = [
    "साबू आपका कोड देखकर सिर पकड़ रहा है... 🤦‍♂️",
    "साबू अपने जुपिटर वाले दिमाग से आपका बग ढूंढ रहा है... 🪐",
    "साबू को गुस्सा आ रहा है, ऐसा कोड कौन लिखता है भाई? 😡",
    "साबू चश्मा लगाकर आपके कोड की धज्जियाँ उड़ाने की तैयारी में है... 👓",
    "चाचा चौधरी की बुद्धि और साबू का दिमाग मिलकर कोड ठीक कर रहे हैं... 💡",
    "साबू सोच रहा है कि इस कोड को सुधारे या सीधा डिलीट मार दे... 🗑️"
]

# इनपुट बॉक्स हमेशा खाली रहेगा
user_code = st.text_area("खराब कोड यहाँ डालें:", placeholder="अपना Python कोड यहाँ टाइप या पेस्ट करें...", height=150)

if st.button("🚀 साबू से ठीक करवाओ"):
    if user_code.strip():
        random_dialogue = random.choice(saboo_dialogues)
        with st.spinner(random_dialogue):
            prompt = f"""
            You are 'Saboo', a hilarious, sarcastic, and brutally roasting Python expert. 
            Analyze this user's Python code and roast them uniquely based on their mistakes, then provide the correct code.
            
            User's Code:
            {user_code}

            Give response in Hindi with two clear sections:
            1. 🚨 साबू का रोस्ट: (A unique sarcastic roast about their code)
            2. ✅ सही कोड: (The corrected Python code)
            """
            try:
                response = model.generate_content(prompt)
                st.markdown(response.text)
            except Exception as err:
                st.error(f"AI एरर: {err}")
    else:
        st.warning("भाई, बॉक्स खाली है! पहले कुछ कोड तो लिखो!")
    
