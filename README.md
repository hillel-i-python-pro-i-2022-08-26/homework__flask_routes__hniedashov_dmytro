# Homework # 4. (Flask)

---
![Main workflow](https://github.com/hillel-i-python-pro-i-2022-08-26/shared__python__example/actions/workflows/main-workflow.yml/badge.svg)
![IDE](https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white)
![REPO](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![flask](https://badgen.net/badge/flask/homework/green)
## 👨‍💻 Homework

Homework related actions:

### ▶️ Build dev

Build the project, install requirements

```shell
make init-dev
```

### ▶️ Run

Make all actions needed for run homework from zero.

```shell
make homework-i-run
```

### 🚮 Purge

Delete all created artifacts from run.

```shell
make homework-i-purge
```

### ✨ Pre-commit run-all

Run a pre-commit.

```shell
make pre-commit-run-all
```

### ▶️ Build and run app using docker

Build the project, install requirements

```shell
make docker-i-run
```

### ▶️ Stop docker container

```shell
make docker-i-stop
```

### ▶️ Down docker container

Removes volumes, networks etc. related to the containers

```shell
make docker-i-down
```