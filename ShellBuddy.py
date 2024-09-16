import streamlit as st

# Set page config to widen the layout and set a title
st.set_page_config(page_title='ShellBuddy', layout='wide')

# Header section
st.image('Resources/logo3.png', width=200)  # Update with the path to your logo
st.title('ShellBuddy')
st.write("Increase your productivity on the commandline interfaces.")

# Installation section
st.header('Installation')
st.code('npm install -g shellbuddy@beta', language='bash')

# Usage section
st.header('Usage')
st.write('Start using ShellBuddy with simple, natural language queries:')
st.code('buddy how to undo the last commit', language='bash')
st.write('**Output:** `git revert HEAD`')

# Features section with interactive elements
st.header('Features')

with st.expander("Productivity Commands"):
    st.subheader("Git Operations")
    st.write("- **Comprehensive Git Command Library**: Access a wide range of Git commands for common and advanced operations.")
    st.write("- **In-Depth Repository Status**: Get a detailed overview of your repository, including branch status, recent commits, and more.")
    st.write("- **Commit Message and Tagging**: Easily commit changes with a message and optional tag, with automated checks for changes before committing.")
    st.write("- **Detailed Commit History**: View the details of the last commits, including the files changed in each commit.")
    st.subheader("Environment Management")
    st.write("- **Virtual Environment Management**: Easily create, manage, and close Python virtual environments.")
    st.write("- **Automated Virtual Environment Checks**: Automatically check if a Python virtual environment exists and create one if necessary.")
    st.write("- **Environment and Dependency Management**: Read environment and dependency information to provide commands for running the application efficiently.")
    st.subheader("System Utilities")
    st.write("- **System Statistics**: Quickly check system performance metrics with integrated tools like `htop`.")

with st.expander("AI-Powered Features"):
    st.subheader("AI Interaction")
    st.write("- **Intuitive NLP Interface**: Ask questions in plain English and get precise Git commands.")
    st.write("- **Real-Time Content Generation with AI**: Interact with Llama3 for generating responses and content based on user prompts.")
    st.write("- **Handle Unknown Commands with AI Assistance**: Automatically generate responses for unrecognized commands using the Gemini AI model.")

with st.expander("Customization & Extensibility"):
    st.subheader("Custom Commands")
    st.write("- **Custom Command Execution**: Define and run custom commands to streamline your workflow.")
    st.write("- **Interactive Git Command Menu**: Access an interactive menu for selecting and executing common Git commands.")
    st.write("- **Extendable and Adaptable**: Add new features and custom commands to suit your unique needs.")

# Footer section
st.write('Distributed under the MIT License.')

# Sidebar with buttons
def nav_button(label, url):
    st.markdown(
        f'''
        <a href="{url}" target="_blank" style="text-decoration: none;">
            <div style="
                display: flex;
                justify-content: center;
                align-items: center;
                background-color: #4CAF50;
                color: white;
                padding: 10px;
                border-radius: 5px;
                margin-bottom: 10px;
                cursor: pointer;
                text-align: center;
            ">
                {label}
            </div>
        </a>
        ''',
        unsafe_allow_html=True
    )

with st.sidebar:
    nav_button('GitHub', 'https://github.com/adev3141/shell-buddy')
    nav_button('Discord', 'https://discord.gg/DkC6fpSJ')
    nav_button('NPM Package', 'https://www.npmjs.com/package/shellbuddy')  # New Button Added
