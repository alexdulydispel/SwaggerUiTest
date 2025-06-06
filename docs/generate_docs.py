import app.main as main
import json

def gen_docs():
    with open("docs/openapi.json", "w") as file:
        json.dump(main.app.openapi(), file)
    
    return

if __name__ == "__main__":
    gen_docs()