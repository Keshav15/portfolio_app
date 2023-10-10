
import requests
import json
import os
from github import Github

def createrepo():
    # Replace with your GitHub organization name, repository name, and Personal Access Token
    org_name = 'PortfolioDeveloper'

    github_token = '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'
    g=Github(github_token)

    repo_name='new_repo5'

    org = g.get_organization(org_name)
    repo = org.create_repo(repo_name, private=False)  # Set private to True for a private repository

    # Define the local file path
    local_file_path = 'streamlit_app.py'

    config_file_path='config_file.json'

    # Read the content of the local file
    with open(local_file_path, 'r') as file:
        file_content = file.read()
        
    with open(config_file_path, 'r') as file:
        config_content = file.read()
        

    # Create and push the file to the new GitHub repository
    repo.create_file(local_file_path, f'Adding {local_file_path}', file_content)

    print(f"Repository '{repo_name}' created successfully with '{local_file_path}' uploaded.")

    return "Repository created successfully."



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



 