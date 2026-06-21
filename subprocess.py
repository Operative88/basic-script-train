import subprocess

wynik = subprocess.run(
    ["ls," "-l"],
    capture_output=True,
    Text=True
)

print(wynik.returncode)
print(wynik.stdout)