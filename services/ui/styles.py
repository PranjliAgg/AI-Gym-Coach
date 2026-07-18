import streamlit as st
import streamlit.components.v1 as components


def theme():
    st.markdown("""
    <style>

    /* ===== GLOBAL ===== */
    .stApp {
        background: radial-gradient(circle at top left, #111827, #0B0F14);
        color: #E5E7EB;
        font-family: 'Inter', sans-serif;
    }
        
                
    /* Hide top toolbar */
    header[data-testid="stHeader"] {
        height: 0;
        background: transparent;
    }

    button[data-testid="stSidebarCollapsedControl"] {
        display: block !important;
    }
    
    .block-container {
        padding-top: 1.5rem;
    }
                
    .hero {
        padding:25px;
        border-radius:24px;
        background: linear-gradient(135deg, rgba(255,104,88,0.15), rgba(59,130,246,0.10));
        border: 1px solid rgba(255,255,255,0.08);
        margin-bottom:25px;
    }

    .hero p {
        font-size:18px;
        color:#94A3B8;
    }

    /* Login Card Gradient */
    .st-key-login-container {
        background: linear-gradient(
            135deg,
            rgba(255,104,88,0.15),
            rgba(59,130,246,0.08)
        ) !important;

        border-radius: 24px !important;
        border: 1px solid rgba(255,255,255,0.1) !important;

        padding: 25px !important;

        backdrop-filter: blur(12px);
    }           
                

    /* ===== MAIN CONTAINER ===== */
    .block-container {
        padding: 2rem 3rem;
    }

    /* ===== HEADINGS ===== */
    h1 {
        font-size: 2.2rem;
        font-weight: 700;
        color: white;
    }

    h2, h3 {
        color: #F3F4F6;
        font-weight: 600;
    }
                
    .empty-card {
        margin-top:32px;
        margin-bottom:32px;
        padding:50px 30px;
        text-align:center;
        background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.06),
            rgba(255,255,255,0.02)
        );
        border-radius:24px;
        border: 1px solid rgba(255,255,255,0.08);
        backdrop-filter:blur(15px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.25);
    }


    .empty-card h2 {
        color:#F9FAFB;
        font-size:28px;
        margin-bottom:12px;
    }


    .empty-card p {
        color:#94A3B8;
        font-size:16px;
        line-height:1.6;
    }


    .empty-icon {
        font-size:64px;
        margin-bottom:15px;
    }


    .empty-tip {
        display:inline-block;
        margin-top:25px;
        padding:10px 18px;
        border-radius:50px;
        background: rgba(255,104,88,0.12);
        color:#FF6858;
        font-weight:600;
    }

    /* ===== GLASS CARD EFFECT ===== */
    .stContainer {
        background: rgba(17, 24, 39, 0.6);
        backdrop-filter: blur(12px);
        border-radius: 16px;
        padding: 20px;
        border: 1px solid rgba(255,255,255,0.08);
        box-shadow: 0 8px 30px rgba(0,0,0,0.3);
    }

    /* ===== INPUT ===== */
    .stTextInput input {
        background-color: rgba(17, 24, 39, 0.9);
        color: white !important;
        border: 1px solid #374151;
        border-radius: 12px;
        padding: 12px;
        font-size: 14px;
    }

    .stTextInput input:focus {
        border: 1px solid #FF6858 !important;
        box-shadow: 0 0 0 2px rgba(255,104,88,0.3);
    }

    /* ===== BUTTONS ===== */

    button[kind="primary"] {
        background: #FF6858 !important;
        color: white !important;
        font-weight: 700;
        border: none !important;
        border-radius: 14px !important;
        padding: 0.6rem 1.5rem;
        transition: 0.2s ease;
    }

    button[kind="primary"] * {
        color: white !important;
    }

    button[kind="primary"]:hover {
        background: #FF5545 !important;
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(255,104,88,0.35);
    }

    button[kind="secondary"] {
        background: linear-gradient(135deg, #F97316, #EF4444) !important;
        color: #E5E7EB !important;
        border: 1px solid rgba(255,255,255,0.15) !important;
        border-radius: 14px !important;
    }

    button[kind="secondary"] * {
        color: #E5E7EB !important;
    }

    button[kind="secondary"]:hover {
        background: rgba(255,104,88,0.1) !important;
        border-color: #FF6858 !important;
        color: #FF6858 !important;
    }

    /* ===== SIDEBAR ===== */
    section[data-testid="stSidebar"] {
        background: #0B0F14;
        border-right: 1px solid #1F2937;
    }

    /* ===== METRIC CARDS ===== */
    div[data-testid="stMetric"] {
        background: rgba(17, 24, 39, 0.7);
        border-radius: 14px;
        padding: 12px;
        border: 1px solid rgba(255,255,255,0.05);
    }

    /* ===== SCROLLBAR ===== */
    ::-webkit-scrollbar {
        width: 8px;
    }

    ::-webkit-scrollbar-thumb {
        background: #374151;
        border-radius: 10px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: #FF6858;
    }

    </style>
    """, unsafe_allow_html=True)



def inject_webrtc_styles():
    components.html(
        f"""
        <script>
        (function patchWebRTCStyles() {{
            function injectIntoIframe(iframe) {{
                try {{
                    const doc = iframe.contentDocument || iframe.contentWindow.document;
                    if (!doc || !doc.head) return;
                    if (doc.head.querySelector('#webrtc-custom-styles')) return;
                    const style = doc.createElement('style');
                    style.id = 'webrtc-custom-styles';
                    style.textContent = `
                        @font-face {{
                            font-family: 'AdobeClean';
                            font-weight: 100 900;
                            font-style: normal;
                        }}
                        .MuiButtonBase-root,
                        .MuiButton-root,
                        .MuiButton-contained,
                        .MuiButton-text {{
                            border-radius: 0 !important;
                            font-family: 'AdobeClean', sans-serif !important;
                            letter-spacing: 0.05em !important;
                        }}
                    `;
                    doc.head.appendChild(style);
                }} catch (e) {{
                    console.warn('[patcher] could not inject:', e);
                }}
            }}

            function findAndPatch() {{
                const parentDoc = window.parent.document;
                const iframes = parentDoc.querySelectorAll('iframe');
                iframes.forEach(iframe => {{
                    if (iframe.src && iframe.src.includes('webrtc')) {{
                        if (iframe.contentDocument && iframe.contentDocument.readyState === 'complete') {{
                            injectIntoIframe(iframe);
                        }} else {{
                            iframe.addEventListener('load', () => injectIntoIframe(iframe));
                        }}
                    }}
                }});
            }}

            findAndPatch();
        }})();
        </script>
        """,
        height=0,
    )
   
