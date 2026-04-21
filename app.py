import streamlit as st
from dotenv import load_dotenv
from src.chain import create_chain

load_dotenv()

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(page_title="Sage the AI Therapist", page_icon="🧠")

# ── Crisis detection ─────────────────────────────────────────────────────────
CRISIS_KEYWORDS = [
    "suicide", "suicidal", "kill myself", "end my life", "want to die",
    "harm myself", "self-harm", "self harm", "no reason to live",
    "don't want to be here", "dont want to be here", "hopeless",
]

CRISIS_MESSAGE = """
**If you are in crisis or immediate danger, please reach out now:**

- **988 Suicide & Crisis Lifeline:** Call or text **988** (US)
- **Crisis Text Line:** Text **HOME** to **741741**
- **International Association for Suicide Prevention:** https://www.iasp.info/resources/Crisis_Centres/
- **Emergency services:** Call **911** (or your local emergency number)

Sage is here to listen, but is not a substitute for professional crisis support.
"""


def is_crisis_message(text: str) -> bool:
    lower = text.lower()
    return any(kw in lower for kw in CRISIS_KEYWORDS)


# ── Session state ─────────────────────────────────────────────────────────────
def init_session():
    if "chain" not in st.session_state:
        try:
            st.session_state.chain = create_chain()
            st.session_state.chain_error = None
        except EnvironmentError as e:
            st.session_state.chain = None
            st.session_state.chain_error = str(e)
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []


def reset_session():
    for key in ["chain", "chat_history", "chain_error"]:
        st.session_state.pop(key, None)
    init_session()


init_session()

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("About Sage")
    st.write(
        "Sage is a supportive AI chatbot designed to help you reflect on your "
        "thoughts and feelings. It is **not** a licensed therapist and cannot "
        "provide medical or psychiatric advice."
    )
    st.divider()
    if st.button("Clear conversation", use_container_width=True):
        reset_session()
        st.rerun()
    st.divider()
    st.caption("If you are in crisis, please contact **988** or **911**.")

# ── Main UI ───────────────────────────────────────────────────────────────────
st.title("🧠 Sage — Your Virtual Therapist")

if st.session_state.get("chain_error"):
    st.error(f"Configuration error: {st.session_state.chain_error}")
    st.info(
        "Set your `ANTHROPIC_API_KEY` in a `.env` file or in Streamlit Cloud secrets "
        "(Settings → Secrets), then reload the page."
    )
    st.stop()

# Render existing history
for sender, message in st.session_state.chat_history:
    role = "assistant" if sender == "Sage" else "user"
    with st.chat_message(role):
        st.markdown(message)

# Handle new input
user_input = st.chat_input("What's on your mind today?")
if user_input:
    # Show user message immediately
    with st.chat_message("user"):
        st.markdown(user_input)

    # Crisis check — show resources before responding
    if is_crisis_message(user_input):
        st.warning(CRISIS_MESSAGE)

    # Stream Sage's response
    response_text = ""
    with st.chat_message("assistant"):
        try:
            response_text = st.write_stream(
                st.session_state.chain.stream_response(user_input)
            )
        except Exception as e:
            st.error(
                f"Something went wrong while reaching the AI: `{e}`. "
                "Please try again in a moment."
            )

    # Persist to history
    st.session_state.chat_history.append(("You", user_input))
    if response_text:
        st.session_state.chat_history.append(("Sage", response_text))
