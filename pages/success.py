import streamlit as st

st.set_page_config(page_title="Crane AI | Study Complete", layout="centered")

# Trigger the celebration immediately when the page loads
st.balloons()

st.markdown("""
    <div style="background-color: rgba(46, 204, 113, 0.1); border: 1px solid #2ecc71; padding: 50px 30px; border-radius: 12px; text-align: center; margin-top: 40px;">
        <h1 style="color: #2ecc71; margin-top: 0; margin-bottom: 15px; font-size: 3rem;">✅ Study Complete!</h1>
        <p style="font-size: 1.25rem; color: var(--text-color); margin-bottom: 30px;">Thank you for participating in this research. Your responses have been successfully recorded.</p>
        
        <hr style="border: 0; border-top: 1px solid rgba(150, 150, 150, 0.2); margin: 35px 0;">
        
        <p style="font-size: 1.2rem; color: var(--text-color); margin-bottom: 20px;">
            The following code gives you Karma that can be used to get free research participants at <strong>SurveySwap.io</strong>.
        </p>
        
        <a href="https://surveyswap.io/sr/UAKH-JVCM-1LR8" target="_blank" style="display: inline-block; background-color: #0068c9; color: white; padding: 16px 32px; border-radius: 8px; text-decoration: none; font-size: 1.2rem; font-weight: 600; margin-bottom: 30px; transition: 0.3s;">
            👉 Click Here to Claim Karma
        </a>
        
        <p style="font-size: 1.1rem; color: #888; margin-bottom: 10px;">Or, alternatively, enter the code manually:</p>
        <div style="background-color: rgba(150, 150, 150, 0.1); display: inline-block; padding: 12px 24px; border-radius: 8px; border: 1px dashed #888;">
            <code style="font-size: 1.6rem; color: var(--text-color); background: transparent;">UAKH-JVCM-1LR8</code>
        </div>
    </div>
""", unsafe_allow_html=True)