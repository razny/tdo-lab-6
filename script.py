import os

message = os.environ.get("MY_MSG", "Domyślna wiadomość")
print(f"Otrzymano skrypt Python: {message}")
