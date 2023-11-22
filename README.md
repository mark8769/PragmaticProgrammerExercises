# Exercises

Point of this repo is to attempt exercises from Pragmatic Programmer 20th Anniversary Edition

Exercise 11 Article 21(Text Manipulation) pg.99

"You're rewriting an application that used to use YAML as a configuration language. Your company has now standardized on JSON, so you have a bunch of .yaml files that need to be turned into .json. Write a script that takes a directory and converts each .yaml file into a corresponding .json file (so database.yaml becomes database.json, and the contents are valid JSON).'"


[Creating Virtual Envs](https://docs.python.org/3/library/venv.html#creating-virtual-environments)

**Windows**

Make a virtual environment with following command, I am using python 3.7.8 https://www.python.org/downloads/release/python-378/

```
python -m venv ./venv
```

On windows, activate environment with this command

```
.\venv\Scripts\activate
```

Update pip inside environment

```
pip3 install -U pip
```


**Macbook Intel Chips**

Make a virtual environment with following command. I am using python 3.7.8.

```
python3 -m virtualenv venv
```

Activate environement

```
source venv/bin/activate
```


**Macbook M1 Chips**

Make virtual environment with following command.


```
python -m venv venv
```

Activate environement

```
source venv/bin/activate
```
