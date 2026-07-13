import streamlit as st


def login_screen():
    st.markdown(
        "<h2 style='text-align: center;'>🏋️ AI Gym Coach</h2>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align: center; color: gray;'>Enter your name to begin</p>",
        unsafe_allow_html=True
    )

    st.write("")  # spacing

    with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            with st.form("login_form"):
                username = st.text_input(
                    "Username",
                    placeholder="e.g. Pranjli",
                    label_visibility="collapsed"
                )

                login_btn = st.form_submit_button(
                    "Start Workout",
                    use_container_width=True
                )

            if login_btn:
                if not username.strip():
                    st.error("Please enter a name.")
                else:
                    st.session_state["user_id"] = "temp_user"
                    st.session_state["username"] = username
                    st.rerun()


def logout():
    st.session_state.clear()
    st.rerun()


def is_logged_in():
    return "user_id" in st.session_state