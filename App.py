import streamlit as st
import streamlit.components.v1 as components

# Set page configuration
st.set_page_config(page_title="Forex Sentiment Widget", layout="centered")

# Add title
st.title("Forex Sentiment Widget")

# Embed the Forex Sentiment widget using HTML and JavaScript
widget_html = """
<div id="forexsentiment-widget" data-domain="ww.xtrend.com" data-type="all" data-theme="light" data-width="300" data-height="340"></div>
<script src="https://forexsentiment.live/js/min/widget-embed.js" async></script>
"""

# Render the widget
components.html(widget_html, height=350, width=310)

# Add a brief description
st.markdown("""
This app displays a Forex Sentiment widget showing market sentiment data.
The widget is sourced from forexsentiment.live and configured with a light theme.
""")
