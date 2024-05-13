import subprocess
import sys
import os
import argparse

def create_venv():
    # Change to the project directory
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_dir)

    # Create a virtual environment
    try:
        subprocess.run([sys.executable, "-m", "venv", ".venv"], check=True)
        print("Virtual environment created successfully.")
    except subprocess.CalledProcessError:
        print("Error creating virtual environment.")
        return

    print("Please activate the virtual environment before proceeding.")
    print("On Windows, run: .venv\\Scripts\\activate")
    print("On Unix or MacOS, run: source .venv/bin/activate")

def install_dependencies():
    
    with open('requirements.txt', 'r') as file: # open the file in read mode
        packages = file.read().splitlines() # read the file and split the lines

    failed_packages = [] # create a list to store the failed packages

    for package in packages: # loop through the packages (iterates each element in the list)
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)
            print(f"{package} installed successfully.")
        except subprocess.CalledProcessError:
            print(f"Error installing {package}.")
            failed_packages.append(package) # add the package to the failed_packages list
            continue

    # install the failed packages w/ the latest versions
    for package in failed_packages:
        try:
            package_name = package.split('==')[0]  # Get the package name without the version ~ first element of the list
            subprocess.run([sys.executable, "-m", "pip", "install", package_name], check=True)
            print(f"{package_name} installed successfully on second attempt.")
        except subprocess.CalledProcessError:
            print(f"Error installing {package_name} on second attempt.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--install", action="store_true", help="install dependencies")
    args = parser.parse_args()

    if args.install:
        install_dependencies()
    else:
        create_venv()