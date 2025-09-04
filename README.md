# Intro to OSS-Fuzz : Build, Break, and Harden Open Source Software


## Description

This repository contains all materials used for the workshop **“Intro to OSS-Fuzz : Build, Break, and Harden Open Source Softwares”**.
It includes the presentation slides, demo files (`Dockerfile`, `build.sh`, `project.yaml`, fuzz harness), and setup instructions to guide participants through integrating a Python project into OSS-Fuzz and discovering real crashes.

---

## Abstract

“10,000+ bugs in open-source software discovered by OSS-Fuzz.”

This number reflects the impact of continuous fuzzing at scale. OSS-Fuzz, Google’s free fuzzing service, has become one of the most effective tools in securing critical open-source projects.

In this workshop, we will explore:

* What fuzzing is and how it works.
* How Atheris enables fuzzing of Python projects.
* How to write a fuzz harness in Python.
* How to integrate a Python project into OSS-Fuzz.
* How to reproduce and analyze crashes.

We will use [`python-markdown2`](https://github.com/trentm/python-markdown2) as a case study, fuzzing its `LinkProcessor.run()` function to uncover real issues.

---

## Setup

```bash
# Clone the OSS-Fuzz repository
git clone https://github.com/google/oss-fuzz

# Clone this repository
git clone https://github.com/mdimado/oosc

# Create project folder inside oss-fuzz
cd oss-fuzz/projects
mkdir python-markdown2
```

---

## Hosts

* @mdimado

