from langchain import hub

def get_prompt():
    return hub.pull("hwchase17/react")