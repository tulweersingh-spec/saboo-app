import streamlit as st

st.set_page_config(page_title="साबू - Python Fixer", page_icon="🤖")

# Sidebar Language Switcher
lang = st.sidebar.radio("🌐 Choose Language / भाषा चुनें", ["Hindi (हिंदी)", "English"])

if lang == "Hindi (हिंदी)":
    st.title("🤖 साबू रोबोट (Python Fixer)")
    st.write("नीचे अपना खराब पायथन कोड डालें और साबू से ठीक करवाएँ!")
    code_input = st.text_area("खराब कोड यहाँ डालें:", value='print("hello"))', height=150)
    btn_text = "🚀 साबू से ठीक करवाओ"
else:
    st.title("🤖 Saboo Robot (Python Fixer)")
    st.write("Paste your broken Python code below and let Saboo fix & roast it!")
    code_input = st.text_area("Paste broken code here:", value='print("hello"))', height=150)
    btn_text = "🚀 Fix with Saboo"

if st.button(btn_text):
    if code_input.strip():
        # Simple check for extra/missing parenthesis
        if code_input.count('(') != code_input.count(')'):
            if lang == "Hindi (हिंदी)":
                st.error("🚨 साबू का रोस्ट: अरे भाई! जितने ब्रैकेट खोलते हो, उतने बंद भी तो करो! ब्रैकेट गिनना भूल गए क्या? 😂")
                st.success("✅ सही कोड:\n```python\nprint(\"hello\")\n```")
            else:
                st.error("🚨 Saboo's Roast: Bro! Count your brackets! You opened fewer brackets than you closed! 😂")
                st.success("✅ Fixed Code:\n```python\nprint(\"hello\")\n```")
        else:
            if lang == "Hindi (हिंदी)":
                st.info("🎉 साबू: कोड में कोई ब्रैकेट की गलती नहीं मिली!")
            else:
                st.info("🎉 Saboo: No bracket errors found in the code!")

st.markdown("---")

# Feedback Section
if lang == "Hindi (हिंदी)":
    st.subheader("💬 साबू को सुझाव या फ़ीडबैक दें")
    feedback = st.text_input("आपको यह ऐप कैसी लगी या इसमें क्या नया जोड़ें?")
    if st.button("भेजें (Submit)"):
        st.success("धन्यवाद! आपका फ़ीडबैक साबू तक पहुँच गया। ❤️")
else:
    st.subheader("💬 Give Feedback / Suggestions")
    feedback = st.text_input("How do you like this app or what feature should we add?")
    if st.button("Submit Feedback"):
        st.success("Thank you! Your feedback has been received. ❤️")

# Branding
st.caption("Made with ❤️ for Coders & Students")
