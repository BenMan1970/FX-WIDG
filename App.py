import streamlit as st
import streamlit.components.v1 as components
import time

# Set page configuration
st.set_page_config(page_title="Forex Sentiment Widget", layout="centered")

# Add title
st.title("Forex Sentiment Widget")

# Function to generate widget HTML
def get_widget_html():
    return """
    <div id="forexsentiment-widget" data-domain="ww.xtrend.com" data-type="all" data-theme="light" data-width="600" data-height="680"></div>
    <script src="https://forexsentiment.live/js/min/widget-embed.js" async></script>
    """

# Initialize session state for refresh
if 'refresh' not in st.session_state:
    st.session_state.refresh = False

# Refresh button
if st.button("Refresh Widget"):
    st.session_state.refresh = True
    time.sleep(1)  # Small delay to ensure refresh
    st.session_state.refresh = False

# Render the widget
components.html(get_widget_html(), height=690, width=610)

# Add a brief description
st.markdown("""
This app displays a Forex Sentiment widget showing market sentiment data.
The widget is sourced from forexsentiment.live and configured with a light theme.
""")
