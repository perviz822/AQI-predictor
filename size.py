import streamlit as st
import streamlit.components.v1 as components


def get_screen_width():
    # HTML + JS to get screen width on page load
    screen_size_script = """
    <html lang="en">
    <head>
        <title>Screen Width Detection</title>
    </head>
    
    <body style="text-align: center;">
        <script>
            window.onload = function() {
                let width = window.innerWidth;
                window.parent.postMessage({screen_width: width}, "*");
            };
        </script>
    </body>
    </html>
    """

    # Render the script in Streamlit's app
    components.html(screen_size_script, height=100)

    # Wait for the screen width message
    screen_width_value = None
    if "screen_width" in st.session_state:
        screen_width_value = st.session_state["screen_width"]
    
    # Return the screen width value
    return screen_width_value


# Capture the screen width value from JavaScript and handle messages

# Call function
