# SETUP SCRIPT

Pyensemble (ensemble derivative) Setup and Framework for Windows

1. **Clone your desired Directory**
    
    If you have read access
        - Create a new folder in your local GitHub directory (typically found in ~\Documents\GitHub) that is appropriately titled.
        - Then open the folder in your IDE (VS Code) and open the cmd (command prompt)
        ```bash
        git clone git@github.com:username/repository.git
        ```
    Otherwise ~ Github Desktop  

2. **Add this script into your project (either clone or copy)**

3. **Creating the virtual environment:**
     Run the command 
    ```bash
    python setup.py
     ```

4. **Activate the venv as Instructed for your OS**

5. **To install dependencies**
   Run the command 
   ```bash
   python setup.py --install
   ```

# For Pysensemble Projects

6. Change your Directory to the Experiments Folder of your cloned pyensemble Directory

    ```bash
    cd ~
    cd pyensemble/experiments
   ```

7. Clone your sub-projects into the experiments folder of the pyensemble framework by repurposing the commands in step 1

8. To access the server and AWS buckets appropriately you need to modify the params.ini files in the settings folder and activate VPN

9. SUCCESS!

# Additional Documentation