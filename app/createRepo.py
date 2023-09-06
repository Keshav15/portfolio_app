
import requests
import json
import os

# Replace with your GitHub organization name, repository name, and Personal Access Token
org_name = 'PortfolioDeveloper'

token = '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'

def createrepo(repo_name):
    os.system('git init')

    # Stage the files
    os.system('git add app/streamlit_app.py app/config_file.json')

    # Commit the changes
    os.system('git commit -m "Initial commit"')


    # Create a new GitHub repository in the organization
    headers = {
        'Authorization': f'token {token}',
    }
    data = {
        'name': repo_name,
        'private': False,  # Set to True for a private repository
        'owner': org_name   # Specify the organization as the owner
    }
    response = requests.post(f'https://api.github.com/orgs/PortfolioDeveloper/repos', headers=headers, json=data)

    if response.status_code == 201:
        print(f'Repository "{repo_name}" created successfully in the organization.')

        # Set the remote origin and push to GitHub
        os.system(f'git remote add origin https://github.com/{org_name}/{repo_name}.git')
        os.system('git branch -M main')
        os.system('git push -u origin main')
    else:
        print(f'Error creating repository: {response.status_code}')


#     # GitHub API authentication using your personal access token
# g = Github("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")
# org = g.get_organization('PortfolioDeveloper')
# def createrepo(name):
#     repo = org.create_repo(name, private=False)


#     # Create the streamlit_app.py file  
#     with open('streamlit_app.py', 'r') as file:
#         content = file.read()
#     with open('app/requirements.txt','r') as file2:
#         requirementals=file2.read()    
#     with open('app/config_file.json','r') as file3:
#         configfile=file3.read()


#         # Create and commit the streamlit_app.py file to the repository
#     repo.create_file("streamlit_app.py", "Initial commit", content)
#     repo.create_file("requirements.txt","newcommit",requirementals)
#     repo.create_file("config.json","adding config file",configfile)
#         # Display success message and link to the newly created repository
#     return repo.html_url

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



 