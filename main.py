import os
import subprocess


def main():
    print("Hello from hellopy!")

    # Intentional vulnerabilities for testing Semgrep. Do not use in real code.

    name = input("Enter a hostname to ping: ")

    # Command injection: user input passed to a shell (CWE-78)
    os.system("ping -c 1 " + name)
    subprocess.call("ping -c 1 " + name, shell=True)

    # Code injection: eval on user input (CWE-95)
    expr = input("Enter an expression: ")
    print(eval(expr))


if __name__ == "__main__":
    main()