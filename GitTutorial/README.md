
Git Basics

Here's a tutorial on the very basics of git. These are provided in a logical sequence and do not intend to cover all the options git provides. 

- Account Creation 
  - Head off to http://github.com and create an account there if you haven't already created one.
  - Once you've setup your account and credentials at http://github.com you are now good to create your own repository
  - In git a repository is where you will store all your code. So head over to the "Repository" section and create your new repo (repository) by clicking on "New". You will need to specify the name of the new repo along with some other options i.e. private, public, etc. If you are keen on letting the rest of the world collaborate with you and leverage what you've aldready built so far I would encourage you to keep your repo public.
  - You will now use this repo to create any new code and upload code from the various machines where you perform your development tasks.

- Cloning an existing Repo  
  - Once you've created your new repo at github.com you are now ready to clone the repo locally on your RaspberryPi, Desktop, Laptop, etc. Cloning (download) is required if you intend to work on the repo remotely, make changes and have them synced up with the main repo.
  - Head over to the new repo directory within your github account. Click on the "Clone or Download" option. This will provide you with a link which will end with a .git. Note down this URL, we'll need it for the next step. 
  - As an example head over to my repo at http://github.com/tangowhisky37/RaspiPythonProjects/
  - Click on the "Clone or Download" option and you'll see the following URL, "https://github.com/tangowhisky37/RaspiPythonProjects.git"
  - If you were to clone this repo you would need to copy this URL to the machine where you wanted to clone (Download) the repo.
  - Open up a prompt on the target host and issue the following commands.
  - bash# git clone <URL> (use the URL you've obtained above)

- Git local configuration 
  - Before you can use git you have to setup a few local variables on your machines
  - The following commands setup your local user name and user email for git to reference. 
  - You can refer to the documentation for additional configuration options. 
  - bash# git config --global user.name "John Doe"
  - bash# git config --global user.email "john.doe@doe.com" 

- Adding a file within a Repo
  - So you'll now perform all your development inside the new folder.
  - You are free to copy content from other folders you might have locally which you want to sync up into the repo.
  - To add a new file to a repo issue the following commands
  - bash# git add <filename> 
  - You can also add whole folders, subfolders and files by issuing the following command
  - bash# git add *

- Checking status
  - To check status just issue the following command while still in the folder which includes the changes you've just made
  - bash# git status
  - The above command will tell you what files have changed, which of the changed files you've added (using git add) and which ones have been left out.

- Performing a commit
  - By issuing the commit you are finalizing the changes and providing comments on what they consist of
  - bash# git commit -m "These updates include fixes the way the files are copied onto AWS S3"

- Checking the files and folders into the repo
  - Finally check the files into the repo using the following command
  - bash# git push --set-upstream origin master 
  - You will be asked for your github account details. Once you've provided them the code will by pushed into the main repo.

- Additional Reading
  - For additional reading please visit - 
  - www.tutorialspoint.com/git/index.htm
  - codeacademy/com/learn/learn-git

Would highly recommend that you take one of the online git tutorials to dig into the details of git. This tutorial was put together to help out a few folk get started. It might or might not be what you are looking for. 


