'''@echo off
for /l %%x in (1, 1, 160) do (
    python "main.py"
    timeout /t 86400  # Sleep for 24 hours (86400 seconds)
)

'''
