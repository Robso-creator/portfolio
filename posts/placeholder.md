# Git and GitHub
##### Última modificação: 2024-08-29


Version control is one of the main pillars when it comes to programming. Saving your projects only on your computer is like shooting an arrow upwards and hoping not to hit your own foot! You, Junior, need to champion this with all your might to avoid becoming a Senior who leaves crucial scripts for the company in the "Documents" folder on their computer.

## So, what is Git?

Understanding what Git is will make it easier to use the tool effectively in your daily work or personal projects. Git is one of many code versioning tools available on the market. Other examples include CVS, Perforce, Subversion, and so on. The main difference between Git and other tools lies in how they view data. While competitors often work as "delta-based version control," where information is stored as a list of changes made to files, Git takes a snapshot of how all files are at each change, saving them as "snapshots" every time you make a change. To avoid unnecessary work, this only happens if there is an actual change in the files.

At the end of the day, they all serve the same purpose: to provide control over our code historically, allowing us to revert to a previous state if any of our changes create chaos within applications. It also allows us to compare versions, spot failures, and identify improvement opportunities.

What's interesting about Git is that it was created by the same person who developed Linux! Do you know what that means? It's free, completely [open source](https://www.redhat.com/pt-br/topics/open-source/what-is-open-source).

## Main Git Concepts

**Repository:**
In the context of Git, a repository is the place where different versions of a project are stored. It can be both local, meaning on your own computer, or remote, hosted on a server accessible via the internet.

**Commit:**
A commit represents a specific version of the project. It contains a set of changes made to the files, marking an important point in the development history.

**Branch:**
A branch is an independent development path that allows you to work on features or bug fixes separately. Each branch has its own development line, allowing for an organized approach to developing new features.

**Merge:**
Merge is the process of combining changes from one branch into another. This is especially useful for integrating a feature developed in a feature branch back into the main branch of the project.

**Conflict:**
A conflict occurs when Git finds conflicting changes in the same code section during a merge operation. In such cases, you need to resolve these conflicts manually to ensure proper integration of changes.

**Stash:**
The stash is a feature that allows you to "save" changes that are not yet ready to be committed temporarily. This makes it easier to switch branches without losing your ongoing work.

**Pull Request:**
A Pull Request is a request made on platforms like GitHub to merge changes from one branch into another. This is an essential form of collaboration and code review in collaborative projects.

**Tag:**
A tag is a specific marker on a commit that indicates an important reference point, such as a release version. It is useful for identifying and marking specific versions of the project.

**Clone:**
Cloning is the process of creating a local copy of an existing Git repository. This allows you to work with the code in your local development environment.

**Fork:**
A fork is an independent copy of a repository, often used in open-source projects. This allows for contributions without needing write permissions to the original repository.

**Rebase:**
Rebase is an operation that allows you to rearrange the commit history, changing the order or incorporating changes from one branch into another in a more linear fashion.

**.gitignore:**
The .gitignore file contains a list of patterns that tell Git which files and folders to ignore when tracking changes. It is useful for excluding unnecessary files, such as local configurations or logs, from version control.

## Main Git Commands

Git is a robust tool with COUNTLESS commands to help developers with version control challenges. However, I’ve selected the 11 main commands that, with informed knowledge, I believe are the most important for a Junior to know:

## 1. [Git Init](https://git-scm.com/docs/git-init)

<pre><code>git init</code></pre>

Initializes a new Git repository in a local directory. This command creates a new empty Git repository or turns an existing directory into a Git repository.

## 2. [Git Clone](https://git-scm.com/docs/git-clone)

<pre><code>git clone \\repository-to-clone//</code></pre>

Clones an existing Git repository from a remote repository (like GitHub, GitLab, etc.) to your local system. This creates a local copy of the entire repository, including all version history.

## 3. [Git Add](https://git-scm.com/docs/git-add)

<pre><code>
git add \\file-to-add//

# You can also use "." to add all modified files
</code></pre>

Adds specific files or changes to the “staging area,” preparing them to be included in the next commit. It can be used with file names or wildcards (*.txt, file?.txt) to add multiple files at once.

## 4. [Git Commit](https://git-scm.com/docs/git-commit)

<pre><code>git commit -m "fixed the infinite while loop bug"</code></pre>

Records changes to the local repository, creating a new snapshot with a descriptive message. Changes in the “staging area” are included in the commit.

## 5. [Git Push](https://git-scm.com/docs/git-push)

<pre><code>git push origin master</code></pre>

Sends changes from the local repository to a remote repository, like GitHub. This updates the remote repository with the latest changes.

## 6. [Git Pull](https://git-scm.com/docs/git-pull)

<pre><code>git pull origin master</code></pre>

Fetches the latest changes from a remote repository and automatically merges them with the local repository. It is used to keep the local repository updated with the remote repository.

## 7. [Git Branch](https://git-scm.com/docs/git-branch)

<pre><code>
git branch # Lists all existing branches

git branch \\branch-name// # Creates a new branch
</code></pre>

Creates, lists, or deletes branches. Branches are independent development paths that allow you to work on separate features without affecting the main code.

## 8. [Git Checkout](https://git-scm.com/docs/git-checkout)

<pre><code>
git checkout \\branch-name// # Switches to an existing branch

git checkout -b \\branch-name// # Creates a new branch and switches to it
</code></pre>

Allows switching between different branches or restoring individual files from a previous commit. It can also be used to create new branches from existing commits.

## 9. [Git Merge](https://git-scm.com/docs/git-merge)

<pre><code>git merge feature # You are on the "main" branch and will merge the "feature" branch into it</code></pre>

Combines changes from one branch (or a specific commit) into the current branch. This integrates development work done in different branches.

## 10. [Git Status](https://git-scm.com/docs/git-status)

<pre><code>git status</code></pre>

Shows the current state of the repository, including which files have been modified, which are in the “staging area,” and which are not being tracked by Git.

## 11. [Git Log](https://git-scm.com/docs/git-log)

<pre><code>git log</code></pre>

Displays a detailed history of commits, showing information such as the author, date, message, and unique identifier of each commit.

## The Three States

**Working Directory:**
It is the state of files in your local file system. In this state, files can be modified, added, or deleted without Git being aware of these changes.

**Staging Area (Index):**
It is the intermediate state between the working directory and the local repository. Here, you select which modifications will be included in the next commit. Files added to the staging area are ready to be recorded as a new version.

**Local Repository:**
It is the state where Git stores all recorded versions of your project. Files in the local repository have already been committed as part of the project’s history. They can be retrieved at any time and shared with other team members.

These three states reflect the typical Git workflow. You first make changes to files in the working directory. Then, you add relevant changes to the staging area to prepare them for the next commit. Finally, you make a commit to record these changes in the local repository as a new version.

## Where Does GitHub Fit In?

GitHub is a cloud-based platform that plays a crucial role in the world of software development. It serves as a hosting and collaboration environment for projects using the Git version control system. It is where we store our [remote repositories](https://codigoparatodos.blog/2023/09/24/de-junior-para-junior-introducao-ao-git-e-github/#repositorio)!

## Main Features:

**Git Repository Hosting:**
GitHub provides a centralized location where developers can host their Git repositories, making them accessible to collaborators worldwide.

**Distributed Collaboration:**
It allows teams to collaborate on projects regardless of their geographical location. Multiple developers can contribute simultaneously to a project.

**Efficient Version Control:**
Facilitates version control and tracking of changes

**Issue and Pull Request Management:**
Allows tracking of tasks, bugs, and improvements through the issue tracking system. Pull requests enable developers to request the integration of their changes into the main project.

**Integrated Development Environment (IDE):**
GitHub offers a web-based development environment called “GitHub Codespaces,” which allows developers to edit, compile, and debug code directly in the browser.

**Integration with Automation Tools (CI/CD):**
Easily integrates with various continuous integration/continuous deployment (CI/CD) tools, automating the building, testing, and deployment of projects.

## Common Uses of GitHub:

**Open Source Projects:**
Many open source projects use GitHub to allow community contributions and provide a centralized space for collaborators.

**Enterprise Software Development:**
Companies use GitHub to manage and collaborate on internal software projects, facilitating teamwork and code maintenance.

**Developer Portfolios:**
Many developers use GitHub to showcase their projects and skills to potential employers or collaborators.

**Technical Documentation:**
In addition to code, GitHub is also used to host technical documentation and educational resources.

GitHub plays a crucial role in the software development ecosystem by facilitating collaboration, version control, and project distribution. With a wide range of features and an active community, it is an indispensable tool for developers of all experience levels, and even Juniors cannot escape its reach.

### Interesting Links:

- [PDF with Git Commands List](https://education.github.com/git-cheat-sheet-education.pdf)
- [Fernanda Kipper | Git and GitHub Lecture](https://www.youtube.com/watch?v=pyM5QLS2h6M&pp=ygUDZ2l0)
- [Free Git and GitHub Course](https://www.dio.me/courses/introducao-ao-git-e-ao-github)
- [Official Git Documentation](https://git-scm.com/doc)
- [Official GitHub Documentation](https://docs.github.com/)

### References:

**Examples of wildcard characters**. Available at: https://support.microsoft.com/en-gb/office/examples-of-wildcard-characters-939e153f-bd30-47e4-a763-61897c87b3f4. Accessed on: Sep 24, 2023.

**Git – git documentation**. Available at: https://git-scm.com/docs/git. Accessed on: Sep 24, 2023.

**Git – what is git?**. Available at: https://git-scm.com/book/en/v2/Getting-Started-What-is-Git. Accessed on: Sep 24, 2023.

**What is open source?**. Available at: https://www.redhat.com/pt-br/topics/open-source/what-is-open-source. Accessed on: Sep 24, 2023.
