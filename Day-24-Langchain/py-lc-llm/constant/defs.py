vars = {
    "OpenAI": ["gpt-3.5"],
    "GoogleAI": ["gemini-pro"]
}

def get_defs(var):
    for k in vars:
        if var in vars:
            return vars[var]
