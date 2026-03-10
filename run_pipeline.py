import yaml
import papermill as pm

# load yaml
with open("pipeline.yaml", "r") as f:
    config = yaml.safe_load(f)

steps = config["pipeline"]

for step in steps:
    
    notebook_path = step["notebook"]
    output_path = "executed_" + notebook_path.replace("/", "_")
    
    print(f"Running step: {step['step']}")
    
    pm.execute_notebook(
        notebook_path,
        output_path
    )

print("Pipeline finished successfully")