<div align="center">
  <h1 align="center">wcclone</h1>

  <p align="center">
    A clone of a simple cmd tool 
    <br />
  </p>
</div>

### Introduction

This is a very small effort to practice my development skills and try to write as much clean code as possible. Also, this is a good opportunity for me to relearn and revise Python as much as possible. Therefore, I am trying to build as many meaningful projects using Python.

I got the idea of making this project after going through this [website](https://codingchallenges.fyi/challenges/intro/). This `Coding Challenges` website contains around 45 challenges till date and a new challenge is added every week. From my research the challenges range from building a full-stack application to a CommandLine Networking Tool. I have started from the first project listed on the website, i.e., building a clone of the `wc` package which is present in Linux. 

Please enjoy building the projects!

### wc - What is it?

The `wc` tool is a very simple tool in Unix / Linux systems which helps us to find the total number of lines, words or bytes a particular file contains.

The basic syntax of the `wc` command is 

```bash
> wc test.txt
  5 37 181 test.txt
> |
```

Here the 3 numbers respectively represent the number of lines, words, and bytes respectively in the `test.txt` file. In this project, I have tried to rebuild the same functionality. You can also add certain options to limit the output of the code.

You can find more information [here](https://en.wikipedia.org/wiki/Wc_(Unix))

### Tech Stack

I have purely used Python to build this simple cmd tool. There are a lot of other languages I could have used but as I mentioned that I wanted to revise Python and to learn it in more depth I decided to build my next set of projects using Python.

Since this is a cmd tool, I had to ensure that we could use a package such that the script may be called from the command-line, with addition to certain options and arguments be provided through the cmd. There are a lot of very useful packages to achieve this but I decided to go with `click` as it provided very flexible funcitonalities.

Also, I have used the `setuptools` library which helps to build Python packages. This part was for my own learning and fun ✌️.

Enough talks, let us now understand how you can also build and run this tool in your own system.

### Build the Tool

#### 1. Fork the Repo

I don't think I need to explain this step further. Fork this repo to your own account

#### 2. Clone the forked Repo

Use the following command in your Git Bash or your Bash Shell to clone the forked repo

```bash
> git clone https://github.com/<YOUR-GITHUB-USERNAME>/wcclone.git
```

#### 3. Checkout a New branch

Don't do anything on the MAIN branch. Instead checkout a new branch and conduct all your tests there. Use the following command

```bash
> git checkout -m <BRANCH-NAME>
```

#### 4. Create a Python virtual environment

You don't need any extra packages to do this. If you have python installed on your machine, you can use the following command.

```bash
> python3 -m venv venv
```

I have written `python3` if you have both Python 2.x and 3.x versions installed on your system or if the `python` command does not work for you.

Activate the environment,

In Unix / Linux,

```bash
> source venv/bin/activate
```

In Windows,

```powershell
> venv\Scripts\activate
```

#### 5. Setup the tool

After the virtual environment has been created, it is pretty straightforward from that. Since most of the code has already been written, all you need to do is just run the `setup.py` file to setup the tool pre-installation.

The command to do this is

```bash
> python setup.py sdist
```

This will create a dist folder and setup your tool there.

#### 6. Install the Tool

Once you have setup the tool, you need to install so that you can properly use the tool just like cmd command. 

Use the following command to install the tool,

```bash
> pip install dist/wcclone-0.1.0.tar.gz
```

The `tar.gz` zipped file contains all the setup information and installation instructions to install the tool required. After the command stops executing, your tool shall be installed.

#### 7. Test the tool

If you have followed all the steps, you can now test the tool.

Use the following command

```bash
> wc test.txt
  5 37 181 test.txt
```

If the command does not give you the necessary output as you expected, do follow the installation steps properly. 

If you want to add any more functionalites please feel free to raise issues. I shall try to add those features.

Cheers!

![Made with love in India](https://madewithlove.now.sh/in?template=for-the-badge)