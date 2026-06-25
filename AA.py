import subprocess 

wynik = subprocess.run(
    ["ls", "-l"],
    capture_output=True,
    text=True
)

#print(wynik.stdout)
#print(wynik.returncode)