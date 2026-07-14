import streamlit as st
import streamlit.components.v1 as components

def theme():
   st.markdown(
    """
    <style>

        .stApp {
        background-color: #0A0D14;
        color: #fff;
        }

        [data-testid="stSidebar"] {
        background-color: #111520;
        }

        /* =========================================================
        TYPOGRAPHY
        ========================================================= */

        .block-container,
        .block-container * {
        font-family: 'AdobeClean', sans-serif !important;
        }

        /* =========================================================
        LAYOUT
        ========================================================= */

        .block-container {
        padding: 50px 3rem !important;
        max-width: 750px !important;
        }

        /* =========================================================
        BUTTONS
        ========================================================= */

        button,
        .stButton button,
        .stDownloadButton button,
        .MuiBox-root button {
        background-color: #181D2A !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 0 !important;
        font-family: 'AdobeClean', sans-serif !important;
        }

        /* =========================================================
        INPUTS & TEXT ELEMENTS
        ========================================================= */

        input,
        textarea,
        p,
        li,
        code,
        [data-testid="stSelectbox"] > div > div,
        [data-baseweb="select"] > div,
        [data-baseweb="popover"] ul,
        [data-baseweb="menu"] {
        border-radius: 0 !important;
        font-family: 'AdobeClean', sans-serif !important;
        }

        /* =========================================================
        METRICS
        ========================================================= */

        [data-testid="stMetric"] {
        background-color: #181D2A;
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 1rem 1.2rem;
        border-radius: 0;
        }

        [data-testid="stMetric"] div {
        display: flex;
        justify-content: space-between;
        align-items: center;
        }

        [data-testid="stMetricValue"] {
        font-size: 1.5rem !important;
        font-weight: 400 !important;
        }

        [data-testid="stMetricLabel"] {
        font-size: 15px !important;
        opacity: 0.6;
        }

        [data-testid="stMetric"] div label p {
        font-size: 16px !important;
        }

        /* =========================================================
        CONTAINERS / CARDS
        ========================================================= */

        .stContainer,
        .stExpander,
        .stTabs,
        .stColumns,
        .stPopover,
        .stAlertContainer,
        .stStatusContainer,
        .stMetric,
        .stTable,
        .stDataFrame,
        .stForm,
        .stSelectbox,
        [data-baseweb="select"] > div,
        [data-testid="stForm"],
        [data-testid="stMetric"],
        [data-testid="stNumberInputContainer"],
        [data-testid="stDataFrameColumnMenu"],
        [data-testid="stHeadingWithActionElements"],
        [data-testid="stCaptionContainer"] p,
        [data-testid="stAlertContentInfo"] p,
        [data-testid="stSidebarNavLink"],
        [data-testid="stMarkdownContainer"] h3,
        [data-baseweb="popover"],
        [data-baseweb="menu"],
        div[role="menu"],
        div[role="menuitem"] {
        border-radius: 0 !important;
        font-family: 'AdobeClean', sans-serif !important;
        }

        /* =========================================================
        DATAFRAME FIX
        ========================================================= */

        .stDataFrame,
        .stDataFrame div,
        .stDataFrameGlideDataEditor {
        border-radius: 0 !important;
        font-family: 'AdobeClean', sans-serif !important;
        }

        /* =========================================================
        INTERACTIVE ELEMENTS
        ========================================================= */

        .stTextInput,
        .stTextArea,
        .stNumberInput,
        .stSlider,
        .stMultiselect,
        .stRadio,
        .stCheckbox,
        .stToggle,
        .stFileUploader,
        .stColorPicker,
        .stDateInput,
        .stTimeInput,
        .stCameraInput,
        [data-testid="stTextInput"] > div,
        [data-testid="stButton"] button,
        [data-testid="stBaseButton-secondaryFormSubmit"],
        [data-testid="stStatusWidget"] {
        border-radius: 0 !important;
        font-family: 'AdobeClean', sans-serif !important;
        }

        /* =========================================================
        MARKDOWN
        ========================================================= */

        [data-testid="stMarkdownContainer"] strong {
        font-family: 'AdobeClean', sans-serif !important;
        }

        /* =========================================================
        FORM
        ========================================================= */

        .stForm {
        margin-top: 2rem !important;
        padding: 1.5rem 1rem !important;
        background-color: #181D2A !important;
        color: #fff;
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
   
