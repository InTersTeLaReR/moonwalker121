import streamlit as st


CREDENTIALS = {
    "admin": "bgs123",
    "user": "bgscet"
}

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "login"

def login_page():
    st.markdown("### 🌟 Welcome to the Learning Portal")

    if st.button("🚀 Go to Primary Learning", use_container_width=True):
        st.session_state.page = "primary"
        return

    st.markdown("---")
    st.markdown("#### 🔐 Login")

    username = st.text_input("👤 Username")
    password = st.text_input("🔑 Password", type="password")

    if st.button("Login"):
        if username in CREDENTIALS and password == CREDENTIALS[username]:
            st.success("✅ Login successful!")
            if username == "user":
                st.session_state.page = "extra_learning"
            else:
                st.session_state.page = "home"
        else:
            st.error("❌ Invalid credentials!")

def home_page():
    st.title("🏠 Welcome Home")

    st.write("You're logged in. You can start learning!")

    if st.button("📘 Go to Primary Learning"):
        st.session_state.page = "primary"

    if st.button("🔒 Logout"):
        st.session_state.page = "login"

def primary_learning_page():
    st.title("📘 Primary Learning Zone")
    st.markdown("### ✨ Choose a Language to Learn")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🔤 English"):
            st.session_state.page = "english"
    with col2:
        if st.button("🌸 Kannada"):
            st.session_state.page = "kannada"
    with col3:
        if st.button("🪔 Hindi"):

            st.session_state.page = "hindi"

    st.markdown("---")
    if st.button("🔙 Back to Home"):
        st.session_state.page = "home"

def english_page():
    st.title("🔤 English Alphabet Learning")
    st.markdown("### Click on a letter to learn how to write it")

    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for i in range(0, len(letters), 6):
        cols = st.columns(6)
        for j, col in enumerate(cols):
            if i + j < len(letters):
                letter = letters[i + j]
                if col.button(letter, use_container_width=True):
                    st.session_state.selected_letter = letter

    if "selected_letter" in st.session_state:
        selected = st.session_state.selected_letter
        if selected == "Q":
            st.image(
                "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.makeagif.com%2Fmedia%2F8-17-2020%2FsR_V2n.gif&f=1&nofb=1&ipt=bdd72401bd797fc4aa9957d80a510da0da4fa2b064424d35475da49e77f15e70",
                caption="✍️ How to write 'Q'",
                use_column_width=True
            )
        elif selected == "A":
            st.image(
                "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.makeagif.com%2Fmedia%2F6-02-2021%2FJKYoCQ.gif&f=1&nofb=1&ipt=da40fea9b77b4660dc0b7eca024571f7ae6ba06e5e2e0fc50566fc49ceb0818b",
                caption="✍️ How to write 'A'",
                use_column_width=True
            )
        else:
            st.info(f"📝 Animation for letter '{selected}' not available yet.")

    if st.button("🔙 Back to Primary"):
        st.session_state.page = "primary"
        st.session_state.selected_letter = None

def kannada_page():
    st.title("🌸 Kannada Letters")
    st.markdown("""
    <div style='font-size: 56px; text-align: center; line-height: 2;'>
        <strong>ಸ್ವರಗಳು (Vowels)</strong><br>
        ಅ ಆ ಇ ಈ ಉ ಊ ಋ ೀ ಎ ಏ ಐ ಒ ಓ ಔ ಅಂ ಅಃ<br><br>
        <strong>ವ್ಯಂಜನಗಳು (Consonants)</strong><br>
        ಕ ಖ ಗ ಘ ಙ<br>
        ಚ ಛ ಜ ಝ ಞ<br>
        ಟ ಠ ಡ ಢ ಣ<br>
        ತ ಥ ದ ಧ ನ<br>
        ಪ ಫ ಬ ಭ ಮ<br>
        ಯ ರ ಲ ವ ಶ ಷ ಸ ಹ ಳ ಕ್ಷ ಜ್ಞ
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔙 Back to Primary"):
        st.session_state.page = "primary"

def hindi_page():
    st.title("🨔 Hindi Letters")
    st.markdown("""
    <div style='font-size: 48px; text-align: center; line-height: 2;'>
        अ आ इ ई उ ऊ ऋ ए ऐ ओ औ अं अः<br>
        क ख ग घ ङ च छ ज झ ञ ट ठ ड ढ ण<br>
        त थ द ध न प फ ब भ म य र ल व श ष स ह
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔙 Back to Primary"):
        st.session_state.page = "primary"

def section_page(title, image_url):
    st.title(f"📘 {title} Section")
    st.image(image_url, use_column_width=True)

    st.markdown("### 💬 Ask me anything related to this subject")

    query = st.text_input("🔍 Enter your query:")
    if st.button("Ask"):
        if query:
            with st.spinner("Thinking..."):
                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[{"role": "user", "content": query}]
                    )
                    st.success(response['choices'][0]['message']['content'])
                except Exception as e:
                    st.error(f"❌ Error: {e}")
        else:
            st.warning("⚠️ Please enter a question first.")

def extra_learning_page():
    st.title("🎓 Advanced Education Portal")

    st.markdown("### 📚 Choose your stream")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🏫 High School"):
            st.session_state.page = "high_school"
    with col2:
        if st.button("🏫 PUC"):
            st.session_state.page = "puc"

    col3, col4 = st.columns(2)
    with col3:
        if st.button("🧑‍💻 Engineering"):
            st.session_state.page = "engineering"
    with col4:
        if st.button("💰 Finance"):
            st.session_state.page = "finance"

    if st.button("🩺 MBBS"):
        st.session_state.page = "mbbs"

    if st.button("🔙 Back to Home"):
        st.session_state.page = "home"

# Page router
if st.session_state.page == "login":
    login_page()
elif st.session_state.page == "home":
    home_page()
elif st.session_state.page == "primary":
    primary_learning_page()
elif st.session_state.page == "english":
    english_page()
elif st.session_state.page == "kannada":
    kannada_page()
elif st.session_state.page == "hindi":
    hindi_page()
elif st.session_state.page == "extra_learning":
    extra_learning_page()
elif st.session_state.page == "high_school":
    section_page("High School", "https://cdn-icons-png.flaticon.com/512/2965/2965879.png")
elif st.session_state.page == "puc":
    section_page("PUC", "https://cdn-icons-png.flaticon.com/512/3135/3135740.png")
elif st.session_state.page == "engineering":
    section_page("Engineering", "https://cdn-icons-png.flaticon.com/512/4359/4359963.png")
elif st.session_state.page == "finance":
    section_page("Finance", "https://cdn-icons-png.flaticon.com/512/2331/2331966.png")
elif st.session_state.page == "mbbs":
    section_page("MBBS", "https://cdn-icons-png.flaticon.com/512/3621/3621639.png")