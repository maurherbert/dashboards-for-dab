import os

# Get environment variables or default values
env = os.environ.get("DEPLOY_ENV", "dev")
catalog = os.environ.get("CATALOG_NAME", f"nyctaxi_{env}")

file_path = "src/StarterDashboard.lvdash.json"

# Read the original JSON file with placeholders
with open(file_path, 'r') as file:
    content = file.read()

# Replace placeholders with actual values
content = content.replace('${catalog_name}', catalog)
content = content.replace('${env}', env)

# Write the updated content back to the JSON file
with open(file_path, 'w') as file:
    file.write(content)

print(f"Rendered {file_path} with catalog: {catalog}")
