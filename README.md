# SETUP SCRIPT

Pyensemble (ensemble derivative) Setup and Framework for Windows

---
## 1. **Clone your desired Directory**

   a. &nbsp; **THIS METHOD ONLY WORKS <u>IF YOU HAVE READ OR WRITE PERMISSIONS FOR A REPOSITORY</u>**  
   b. &nbsp; **REMARK**: This step requires you to have set up a personal SSH key previously.  
   c. &nbsp; Create a new folder in your local GitHub directory (typically found in `~\Documents\GitHub`) that is appropriately titled.  
   d. &nbsp; Then open the folder in your IDE (VS Code) and open the command prompt (`cmd`).  
   e. &nbsp; Retrieve the password-protected SSH key for your desired repository (example of how to copy the SSH key of a repository):  
      ![Alt text](https://github.com/maxxhvo/setup_script/blob/main/Example_SSH.png?raw=true)  
   f. &nbsp; Then clone the repository as follows:  
      ```bash
      git clone [git@github.com:username/repository.git (your ssh key)]
      ```  
   g. &nbsp; If the following method does not work, you may need to utilize GitHub Desktop to fix this.

## 2. **Add this script into your project**
*  EITHER clone this repository into your project in a similar fashion as in step 1
*  OR download the setup.py file and add it to your project manually

## 3. **Creating the virtual environment:**
Run the command 
    ```bash
    python setup.py
     ```

## 4. **Activate the venv as Instructed for your OS**

## 5. **To install dependencies**
Run the command 
   ```bash
   python setup.py --install
   ```
---
# For Pysensemble Projects

6. Change your Directory to the Experiments Folder of your cloned pyensemble Directory

    ```bash
    cd ~
    cd pyensemble/experiments
   ```

7. Clone your sub-projects into the experiments folder of the by ensemble framework by repurposing the commands in step 1

8. To access the server and AWS buckets appropriately you need to modify the params.ini files in the settings/locals folder (and modify the settings and dev files to match those changes) and activate VPN

9. SUCCESS! You can now utilize -runserver and -shell commands

# Additional Documentation
