# `streamlit run app.py`
# pip install streamlit numpy pandas

import datetime
import os
import streamlit as st
import numpy as np
import pandas as pd
import subprocess



# MY FUNCTION
def git_commit_and_push():
    subprocess.run(["git", "add", "README.md"])
    subprocess.run(["git", "commit", "-m", "Update README.md with new note"])
    subprocess.run(["git", "push"])













st.title("My Web GUI");
st.write("Hello world from codespace");
if st.button("Click Me"):
    st.success("You have clicked the button!");

st.header("y = x^2 Plot")

# Create data for the plot
x_values = np.linspace(-10, 10, 200)
y_values = x_values**2

chart_data = pd.DataFrame({
    'x': x_values,
    'y': y_values,
})

st.line_chart(chart_data, x="x", y="y")

# --- Markdown Note-Taking ---
st.header("Add Note to README.md")

with st.form("markdown_note_form", clear_on_submit=True):
    note_input = st.text_area("Write your note for README.md:")
    submitted = st.form_submit_button("Add Note")

    if submitted and note_input:
        timestamp = datetime.datetime.now().strftime("%Y/%m/%d (%I:%M %p)")  # Format: YYYY/MM/DD (HH:MM AM/PM)
        note_content = f"""
### {timestamp}
```
{note_input}
```
"""
        try:
            with open("README.md", "r+") as f:  # Open in read and write mode
                existing_content = f.read()
                f.seek(0, 0)  # Move the cursor to the beginning of the file
                f.write(note_content + existing_content)  # Write the new note at the top
                git_commit_and_push()




            st.success(f"Note added to README.md!")
        except FileNotFoundError:
            st.error("README.md not found. Please ensure it exists.")


# --- Markdown Previewer ---
st.header("Preview of README.md")


try:
    with open("README.md", "r") as f:
        markdown_content = f.read()
    st.markdown(markdown_content)
except FileNotFoundError:
    st.warning("README.md not found. Please create it in the same directory as app.py.")
