import streamlit as st
from github import Github
import requests

st.title("Portfolio Developer")

# Input field for user's name
name = st.text_input("Enter your name")

uploaded_file = st.file_uploader("Choose a file", "pdf")
if uploaded_file is not None:
    for page_layout in extract_pages(uploaded_file):
        for element in page_layout:
            st.write(element)

# Button to create the repository
if st.button("Create Repository"):
    # GitHub API authentication using your personal access token
    g = Github("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")
    org = g.get_organization('PortfolioDeveloper')
    # Create a new public repository with the user's name
    repo = org.create_repo(name, private=False)

    # Create the streamlit_app.py file
    content = '''
    import streamlit as st

    def main():
        st.title("Hello, {}!")

    if __name__ == "__main__":
        main()
    '''.format(name)

    # Create and commit the streamlit_app.py file to the repository
    repo.create_file("streamlit_app.py", "Initial commit", content)
    repo.create_file("requirements.txt","newcommit",requirementals)
    repo.create_file("config.json","adding config file"configfile)
    # Display success message and link to the newly created repository
    st.success(f"Repository '{name}' created successfully!")
    st.write("You can access your repository at:")
    st.write(repo.html_url)

    # Deploy the repository on Streamlit Cloud
    # st.write("Deploying to Streamlit Cloud...")
    # response = requests.post(
    #     "https://api.streamlit.io/apps/deploy",
    #     json={"githubUrl": repo.clone_url, "branch": "main"},
    #     headers={"Authorization": "Bearer YOUR_STREAMLIT_CLOUD_API_KEY"}
    # )

    # # Check the deployment response status
    # if response.status_code == 201:
    #     st.success("Deployment to Streamlit Cloud successful!")
    #     st.write("You can access your deployed app at:")
    #     st.write(response.json()["url"])
    # else:
    #     st.error("Failed to deploy to Streamlit Cloud. Please try again.")



 