import os 
print(os.getcwd())
print(os.listdir())
os.makedirs("logs", exist_ok=True)
print(os.path.exists("backup.py"))