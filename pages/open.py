import streamlit as st
import time
from supabase import create_client
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted

# --- 1. CONFIG & BRANDING ---
st.set_page_config(page_title="Nexus KMS | Open Query", layout="wide")

st.markdown("""
    <style>
        .main { background-color: #f8f9fa; }
        .stButton>button { width: 100%; border-radius: 5px; background-color: #0b5ed7; color: white; font-weight: bold; }
        header { visibility: hidden; }
        [data-testid="stSidebarNav"] {display: none;}
    </style>
""", unsafe_content_html=True)

# --- 2. INITIALIZE CONNECTIONS ---
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-2.5-flash-lite')

@st.cache_resource
def init_connection():
    return create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])

supabase = init_connection()

# --- 3. KNOWLEDGE BASE ---
SYSTEM_CONTEXT = """
You are the Nexus Corporate Intelligence System. Use ONLY this data:
- Q1: IT migrated to AWS (15% speed up). Finance Revenue $2.1M.
- Q2: Cyber attack led to 40k fake reviews. HR hired 25 contractors. Revenue dropped to $1.9M. 
- Q3: Analytics deployed GenAI (+22% order value). Revenue $2.6M. Churn 1.9%.
- Q4: Record Revenue $3.4M. Logistics costs reduced. 100% uptime.
"""

# --- 4. SIDEBAR TASK TRACKER ---
with st.sidebar:
    st.title("📂 Research Task")
    st.info("**Objective:** Identify the cause of the Q2 revenue drop and find the Q3 churn rate.")
    st.write("---")
    st.metric("Search Iterations", st.session_state.get('iteration_count', 0))
    if st.button("Emergency Restart"):
        st.switch_page("app.py")

# --- 5. MAIN INTERFACE ---
col1, col2 = st.columns([1, 4])
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/2800/2800168.png", width=70)
with col2:
    st.title("Nexus Open Query Terminal")
    st.caption("Natural Language Interface | Version 2.4.0-Stable")

st.divider()

user_query = st.chat_input("Ask the corporate database a question...")

if user_query:
    st.session_state.iteration_count += 1
    
    with st.chat_message("user"):
        st.write(user_query)
        
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Decrypting Database..."):
            try:
                full_prompt = f"{SYSTEM_CONTEXT}\n\nUser: {user_query}"
                response = model.generate_content(full_prompt)
                st.markdown(response.text)
            except ResourceExhausted:
                st.warning("⚠️ System load high. This iteration was not charged. Please wait 10 seconds.")
            except Exception as e:
                st.error("System Error. Please try again.")

# --- 6. LOGGING ---
st.write("###")
if st.button("✅ I have found the required information"):
    total_time = round(time.time() - st.session_state.get('start_time', time.time()), 2)
    
    data = {
        "Participant_ID": int(time.time()),
        "Condition": "Open",
        "Total_Time_Seconds": total_time,
        "Prompt_Iterations": st.session_state.iteration_count
    }
    
    try:
        supabase.table("HCI").insert(data).execute()
        st.balloons()
        st.success("Data securely logged. Thank you for participating!")
        time.sleep(2)
        st.stop()
    except Exception as e:
        st.error(f"Log Error: {e}")
