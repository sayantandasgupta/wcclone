<div align="center">
  <h1 align="center">wcclone</h1>

  <p align="center">
    A clone of a simple cmd tool
    <br />
    <!-- <a href="https://mwv-blogapi.herokuapp.com">Deployed Application</a>
    ·
    <a href="https://github.com/mindwebs/blog-api/issues">Report Bug</a>
    ·
    <a href="https://github.com/mindwebs/blog-api/issues">Request Feature</a> -->
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