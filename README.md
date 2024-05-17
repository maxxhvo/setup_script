# 💡📝 OVERVIEW
This project is implemented to streamline the initial setup of the project environment. It will first guide you through how to replicate a remote repository onto your local machine. (creating a local repository that resides on your machine). Utilizing the setup.py script attached to this project (proceed to step 2 for more information), a properly configured Virtual Environment (venv) and  project-specific dependencies will be properly installed.

This allows for procedural/systematic setup of your developer environment and allows for one to start working on this code at a faster rate.
A separate script may need to be implemented for settings files ~ user-specific

<br />

# 🪜 STEP-BY-STEP RUNDOWN  

## 1. **Clone your desired Directory**
<p class="instructions">
        a. &nbsp; <strong>THIS METHOD ONLY WORKS <ins>IF YOU HAVE READ OR WRITE PERMISSIONS FOR A REPOSITORY</ins></strong><br>
        b. &nbsp; <strong>REMARK</strong>: This step requires you to have set up a personal SSH key previously.<br>
        c. &nbsp; Create an appropriately named folder in your local GitHub directory (typically found in <code>~\Documents\GitHub</code>) to access later.<br>
        d. &nbsp; Then open the folder in your IDE (VS Code) and open the command prompt (<code>cmd</code>).<br>
        <strong>EXAMPLE: Access Powershell and CMD</strong><br>
        <img src="https://github.com/maxxhvo/setup_script/blob/main/Terminal.png?raw=true" alt="Terminal" width="300" height="200"> &nbsp; &nbsp;
        <img src="https://github.com/maxxhvo/setup_script/blob/main/CMD.png?raw=true" alt="CMD" width="500" height="200"><br>
        e. &nbsp; Retrieve the password-protected SSH key for your desired repository (example of how to copy the SSH key of a repository):<br>
        <img src="https://github.com/maxxhvo/setup_script/blob/main/Example_SSH.png?raw=true" alt="SSH" width="300" height="200"><br>
        f. &nbsp; Then clone the repository as follows:<br>
        <pre><code>git clone [your SSH key]
# (SSH key should be in the form git@github.com:username/repository.git)</code></pre>
        g. &nbsp; If the following method does not work, you may need to utilize GitHub Desktop to fix this.
    </p>

## 2. **Add this script into your project**
*  EITHER clone this repository into your project in a similar fashion as in step 1
*  OR download the setup.py file and add it to your project manually

## 3. **Creating the virtual environment:**
Run the command in `cmd`
   ```bash
   python setup.py
   ```

## 4. **Activate the venv as Instructed for your Operating System**
For Windows Run the following command in `cmd`
   ```bash
   .venv\\Scripts\\activate
   ```
For Unix or MacOS Run the following command in `cmd`'
   ```bash
   .venv/bin/activate
   ```
## 5. **To install dependencies**
Run the command in `cmd`
   ```bash
   python setup.py --install
   ```
---
<br />

# 💡For Pysensemble Projects  
6. Change your Directory to the Experiments Folder of your cloned pyensemble Directory
   ```bash
    cd ~
   ```
   ```bash
    cd pyensemble/experiments
   ```

7. Clone your Specific sub-projects into the experiments folder of the by ensemble framework by repurposing the commands in step 1

8. To access the server and AWS buckets appropriately you need to modify the params.ini files in the settings/locals folder (and modify the settings and dev files to match those changes) and activate VPN

9. SUCCESS! You can now utilize -runserver and -shell commands
---
<br />

# 🔎 Additional Documentation

[ARCHIVE](https://docs.google.com/document/d/112po9Mf30oeV9Jc-sMp-tjB23gYOv4xI0MT5Iz9y5ks/edit)

<br />
