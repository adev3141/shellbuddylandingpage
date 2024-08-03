import streamlit as st

# Set page config to widen the layout and set a title
st.set_page_config(page_title='ShellBuddy', layout='wide')

# Header section
st.image('Resources/logo3.png', width=200)  # Update with the path to your logo
st.title('ShellBuddy - Gemini Powered')
st.write("Streamline your workflow with easy access to Git commands and more.")

# Installation section
st.header('Installation')
st.code('npm install -g shellbuddy@beta', language='bash')

# Usage section
st.header('Usage')
st.write('Start using ShellBuddy with simple, natural language queries:')
st.code('buddy how to undo the last commit', language='bash')
st.write('**Output:** `git revert HEAD`')

# Features section
st.header('Features')
st.write("""
- **Intuitive NLP Interface**: Ask questions in plain English and get precise Git commands.
- **Comprehensive Git Command Library**: Access a wide range of Git commands for common and advanced operations.
- **Virtual Environment Management**: Easily create, manage, and close Python virtual environments.
- **Custom Command Execution**: Define and run custom commands to streamline your workflow.
- **In-Depth Repository Status**: Get a detailed overview of your repository, including branch status, recent commits, and more.
- **System Statistics**: Quickly check system performance metrics with integrated tools like `htop`.
- **Extendable and Adaptable**: Add new features and custom commands to suit your unique needs.
""")

# Footer section
st.write('Distributed under the MIT License.')

def nav_button(label, url):
    st.markdown(
        f'<a href="{url}" target="_blank"><button style="width: 100%;">{label}</button></a>',
        unsafe_allow_html=True
    )

# Sidebar with buttons
with st.sidebar:
    nav_button('Explore More', 'https://github.com/adev3141/shell-buddy')
    nav_button('Discord', 'https://discord.gg/DkC6fpSJ')


