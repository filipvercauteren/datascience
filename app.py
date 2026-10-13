"""NMBS Whiteboard - Streamlit skelet."""

import streamlit as st


def render_header() -> None:
    st.title("NMBS Whiteboard")
    st.caption("Skelet-app - nog geen dataverwerking.")


def render_body() -> None:
    st.info("Hier komt binnenkort de analyse.")


def main() -> None:
    st.set_page_config(page_title="NMBS Whiteboard", layout="wide")
    render_header()
    render_body()


if __name__ == "__main__":
    main()
