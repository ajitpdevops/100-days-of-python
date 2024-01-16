# How to get started 
- Clone this repo 
- Create a virtual env and activate it.
- Install all dependancies from requirements.txt
- create a .env file with 2 keys in the root of your project folder and add OPENAI_API_KEY & GOOGLE_API_KEY
- Run the program as follow ```$ python main.py --language java --task "Create an array from 1 to 10" --provider openai```
    - This commandline takes 3 parameter 
        - language - programming language of your choice ( default is python)
        - task - the task you want to write the code & test for
        - provider - google (default) or openai



# Copy to Repo
rsync -av /repos/personal_repos/py-lc-llm /repos/personal_repos/100-days-of-python/Day-24-Langchain