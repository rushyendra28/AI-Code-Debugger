import streamlit as st
import requests

# 🔥 Page config
st.set_page_config(
    page_title="AI Code Debugger",
    page_icon="🐞",
    layout="wide"
)

# 🔥 Custom CSS (premium look)
st.markdown("""
    <style>
        .main {
            background-color: #0e1117;
        }
        h1, h2, h3 {
            color: #ffffff;
        }
        .stTextArea textarea {
            background-color: #1e1e1e;
            color: #ffffff;
        }
    </style>
""", unsafe_allow_html=True)

# 🔥 Header
st.title("🐞 AI Code Debugger")
st.caption("Debug smarter. Fix faster. Powered by Gemini ⚡")

# 🔥 Layout
col1, col2 = st.columns([2, 1])

with col1:
    code = st.text_area("💻 Paste your code", height=400)

with col2:
    language = st.selectbox(
        "🌐 Language",
        ["python", "javascript", "java", "go", "c++"]
    )

    debug_btn = st.button("🚀 Debug Code", use_container_width=True)

# 🔥 Debug action
if debug_btn:

    if not code.strip():
        st.warning("⚠️ Please enter some code")
    else:
        with st.spinner("Analyzing your code..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/debug",
                    json={
                        "code": code,
                        "language": language
                    }
                )

                data = response.json()

                # 🔥 Tabs for clean UI
                tab1, tab2, tab3, tab4 = st.tabs([
                    "🚨 Issues",
                    "🧠 Explanation",
                    "✅ Fixed Code",
                    "⚡ Improvements"
                ])

                with tab1:
                    issues = data.get("issues", [])
                    if issues:
                        for issue in issues:
                            st.error(issue)
                    else:
                        st.success("No major issues found 🎉")

                with tab2:
                    st.write(data.get("explanation", ""))

                with tab3:
                    fixed_code = data.get("fixed_code", "")
                    st.code(fixed_code, language=language)

                    # 🔥 Copy button
                    st.download_button(
                        label="⬇️ Download Fixed Code",
                        data=fixed_code,
                        file_name="fixed_code.txt",
                        mime="text/plain"
                    )

                with tab4:
                    improvements = data.get("improvements", [])
                    if improvements:
                        for imp in improvements:
                            st.info(imp)
                    else:
                        st.write("No suggestions")

            except Exception as e:
                st.error(f"❌ Error: {e}")