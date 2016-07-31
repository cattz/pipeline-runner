BitBucket Pipeline Runner for Bamboo
=========================
Given a bitbucket pipeline file, run all steps locally. This will ignore the given Docker image.


Usage
=====

```bash
$ pip install pipeline-runner
```

Will install the latest version and it's required packages. You can then run the the pipeline runner with a pipeline file:

```bash
$ pipeline-runner
Usage: pipeline-runner [options]

Options:
  -h, --help            show this help message and exit
  -f FILE, --file=FILE  Parse pipeline from FILE
  -b BRANCH, --branch=BRANCH
                        Parse pipeline for branch BRANCH
```

Why?
====
We needed a way for us to move our Bamboo build scripts into version control, and have way to easily migrate our scripts later on. So we build this tool to do that
