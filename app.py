import streamlit as st

st.set_page_config(page_title="साबू - Python Fixer", page_icon="🤖")

st.title("🤖 साबू रोबोट (Python Fixer)")
st.write("नीचे अपना खराब पायथन कोड डालें और साबू से ठीक करवाएँ!")

user_code = st.text_area("खराब कोड:", height=150, placeholder='print("hello"))')

ROAST_COMMENTS = [
    "अरे मेरे भाई! ब्रैकेट्स का मेला लगा रखा है क्या? जितने खोले हैं उतने ही बंद करो!",
    "वाह उस्ताद! ऐसा कोड तो पायथन का क्रिएटर भी देखकर रो पड़े। Syntax Error है!",
]

if st.button("🚀 साबू से ठीक करवाओ", type="primary"):
  if not user_code.strip():
    st.warning("अरे भाई, पहले कोड तो लिखो!")
  else:
    try:
      compile(user_code, "<string>", "exec")
      st.success(
          "साबू: अरे वाह भाई! कोड में कोई गलती नहीं मिली। एकदम सही कोड है! 🚀"
      )
      st.code(user_code, language="python")
    except SyntaxError as e:
      error_msg = str(e)
      fixed_code = user_code

      if "unmatched ')'" in error_msg or "was never closed" in error_msg:
        open_b = user_code.count("(")
        close_b = user_code.count(")")
        if close_b > open_b:
          fixed_code = user_code.rsplit(")", close_b - open_b)[0]

      st.error(f"साबू: {ROAST_COMMENTS[0]}")
      st.info(f"एरर विवरण: {e.msg} (लाइन {e.lineno})")
      st.subheader("सही कोड नीचे है:")
      st.code(fixed_code, language="python")
      
