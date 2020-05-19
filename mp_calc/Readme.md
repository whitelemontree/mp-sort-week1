# Mini Project 1: Math Quiz App

## Learning Objectives
In this mini project, you will develop a web app to create and play math quiz for integer arithmetic. By the end of this assignment, you should be able to:
- Create a web app using Flask web framework
- Use database to store and retrieve data
- Implement mergesort for server application library
- Use Stack to evaluate integer expressions

## Setup

### Install Git

You need to have Git to do the project. Download and install the software according to your OS:
- Windows: [Git for Windows](https://git-scm.com/download/win)
- Mac OS: [Git for MacOS](https://git-scm.com/download/mac)

### Downloading Repository
Clone the mini project repository from Github. On your terminal or Git Bash, type the following:

```shell
$ cd Downloads
$ git clone https://github.com/kurniawano/d2w_mini_projects.git
```

### Go to Mini Project 2 Folder

Once you have downloaded the repository, you can go to the repository and to the folder called `mp_calc` for this mini project.

```shell
$ cd d2w_mini_projects/mp_calc
$ ls
```

The last command should output the following:

```shell
app
application.py
migrations
mp2_exercises.ipynb
requirements.txt
```

This handout can be found in the file `Readme.md`.

## Create Virtual Environment (Windows)

**You should open Anaconda Prompt to do the following steps.**

In the following steps, the Windows prompt will be represented by:
```shell
>
```
Go to the root folder `mp_calc`.
```shell
> cd %USERPROFILE%\Downloads\d2w_mini_projects\mp_calc
```
From the root folder, i.e. `mp_calc`, create virtual environment called `virtenv`.

```shell
$ python -m venv virtenv
```

A folder called `virtenv` will be created. Now, activate the virtual environment.
```shell
> virtenv\Scripts\activate
```

You should see the word `virtenv` in your prompt something like:
```shell
(virtenv) folder>
```

_To exit the virtual environment at the end of this mini project, simply type:_
```shell
> deactivate
```

## Create Virtual Environment (MacOS/Linux)


In the following steps, the MacOS/Linux prompt will be represented by:
```shell
$
```

Go to the root folder `mp_calc`. 
```shell
$ cd ~/Downloads/d2w_mini_projects/mp_calc
```

From the root folder, i.e. `mp_calc`, create virtual environment called `virtenv`.

```shell
$ python -m venv virtenv
```

A folder called `virtenv` will be created. Now, activate the virtual environment. 

```shell
$ source virtenv/bin/activate
```

You should see the word `virtenv` in your prompt something like:
```shell
(virtenv) user$
```

_To exit the virtual environment at the end of this mini project, simply type:_
```shell
$ deactivate
```
## Combined (Windows/Mac/Linux)

### Install Python Packages

Install the necessary packages for this mini project. From the root folder, i.e. `mp_calc`, type the following:

For Windows:
```shell
> pip install -r requirements.txt
```

For MacOS/Linux: (For Linux, you might need to type pip3 instead)
```shell
$ pip install -r requirements.txt
```

The above steps will install the following packages:

- Flask
- Transcrypt 
- Flask-SQLAlchemy
- Flask-Migration
- Flask-Bootstrap
- and some other packages

### Exercise 1

#### Brief Overview of Flask Project Structure

We are using Flask web framework to create this web app. There are more files in this mini project as compared to the first one. You should revise your first mini project before proceeding to this mini project. In this notes, we will highlight only those parts which differ from the previous mini project.

The first file you need to take a look is `application.py` in the root folder. Open that file using a text editor. You should see these *additional* lines in that file:

```python
from app import application, db
from app.models import User, Question, Challenge, TimeRecord

@application.shell_context_processor
def make_shell_context():
	return {'db': db, 'User': User, 'Question': Question,
			'Challenge': Challenge,
			'TimeRecord': TimeRecord}
```

The other lines not shown above have been explained in your previous mini project. We will focus more on those lines above. 

- The first change is that we import `db` which is the object that we will use to work with our SQL database. 
- The second line of imports took from the file `app/models.py` the classes definitions called `User`, `Question`, etc. These classes represent your database tables.
- The decorator `@application.shell_context_processor` and the following lines is to allow you to run a python shell by typing `flask shell` where all those names in the dictionary will be added to the shell as an object instance.

Just to recall, both `application` and `db` imported from `app` are defined inside the `__init__.py` file under the `app` folder.

```shell
mp_calc/
  app/
    __init__.py
    forms.py
    models.py
    routes.py
    serverlibrary.py
    static
    templates
```

The file `__init__.py` contains the line that creates the `db` object.

```python
application = Flask(__name__)
application.config.from_object(Config)
db = SQLAlchemy(application)
migrate = Migrate(application, db)
login = LoginManager(application)
login.login_view = 'login'
bootstrap = Bootstrap(application)

from app import routes, models
```

- After the line that defines `application` we have the command to load the database configuration from `Config` which is defined in `config.py` in the root folder.
- The third line defines `db` as an object instance of `SQLAlchemy`
- We also define `migrate` that is used to migrate the database whenever we make changes to the tables or the models. 
- Next, we have two lines to create our login page. `login.login_view` directs the URL and route it to `login()` defined in the `routes.py`.
- Lastly, we defined `bootstrap` which allow us to use some predefined CSS from [Bootstrap](https://pythonhosted.org/Flask-Bootstrap/basic-usage.html).

This file also import the file `routes.py` which defines the URL routing. Open `app/routes.py` to see the whole file. We will focus on the first few lines for the first exercise.

```python
from app.serverlibrary import mergesort, EvaluateExpression, get_smallest_three 

@application.route('/')
@application.route('/index')
@login_required
def index():
	return render_template('index.html', title='Home')

@application.route('/users')
@login_required
def users():
	users = User.query.all()
	mergesort(users, lambda item: item.username)
	usernames = [u.username for u in users]
	return render_template('users.html', title='Users',
							users=usernames)
```

- The only change to the `index` route is the line `@login_required`. This decorator ensures that when a user tries to enter `/index` page, they must login to the page first. If they have not, Flask will redirect them to the login page. The `login()` route is also defined in `routes.py`.
- The second route is when the user go to `/users` either by entering the URL or by clicking "Users" in the navigation bar. 
- `users = User.query.all()` retrieves all users from the database in `User` table (`User` is defined in `models.py`). 
- `mergesort(users, lambda item: item.username)` calls the sorting function to sort the list of users using its `username` attribute. Note that the `User` table has other attributes besides `username`. Refer to `models.py` for all the attributes of `User` table. It should sort the `users` in place. You need to modify your `mergesort()` function as described in **Q1** of `mp2_exercises.ipynb` to complete this. 
- `usernames = [u.username for u in users]` creates a list of usernames from the list of sorted users. 
- In the last line, `render_template('users.html', title='Users', users=usernames)`, we pass the variable `username` to be used in the `users.html` using some jinja templating under the name `users`.


This file `users.html` can be found inside the `templates` folder.

```shell
mp_calc/
  app/
    __init__.py
    forms.py
    models.py
    routes.py
    serverlibrary.py
    static
    templates/
      base.html
      challenges.html
      halloffame.html
      index.html
      login.html
      questions.html
      register.html
      users.html 
```

For Exercise 1, you may want to look into the following files:

- `users.html`: the HTML file to display the list of users.
- `serverlibrary.py`: the python module where you need to implement your `mergesort()` function.

### Exercise 1

Let's open `users.html`. The first few lines are shown here.

```html
{% extends "base.html" %}

{% block app_content %}
<h1>This Platform's Users</h1>
```

- The first line `{% extends "base.html" %}` inherits the `base.html` for some of the common elements such as the navigation bar, importing certain scripts, and CSS files. The javascript which we will transalte from the file `serverlibrary.py` is imported in the last few lines of `base.html`.
- The second line indicates the block `app_content`. Each html file templates we have will modify this block `app_content`. 

This file basically iterates over all users and create rows of users in a table. The table body code is shown below.

```html
<tbody>
  {% for idx in range(users|length) %}
  	<tr>
      <th scope="row" class="lead">{{ idx+1 }}</th>
      <td class="lead">
      	#Replace Me#
      </td>
    </tr>
  {% endfor %}
  
</tbody>
```

#### Exercise 1 - Task 1
You need to replace the text `#Replace Me#` with some jinja templating code such that it displays the items inside `users`. 

#### Exercise 1 - Task 2
You need to do **Q1** in `mp2_exercises.ipynb` before completing this part. Once you finish with Q1, open `serverlibrary.py` and copy your modified `mergesort()` function inside.

#### Exercise 1 - Task 3
This web application makes use of some client javascript library which is translated from `clientlibrary.py` under `app/static/` folder. To be able to run the web application, you need to go to that folder and compile `clientlibrary.py` using Transcrypt. You also need to setup the database. So in this task we do the following:
- compile `clientlibrary.py` into a javascript file
- create database

Follow the steps below.

**Windows**

First, make sure that you have done the following:
- actiate your virtual environment
- install all the required packages (see the instructions above)

Go to your root folder.
```dos
> cd %USERPROFILE\Downloads\d2w_mini_projects\mp_calc
```

Now, we can go to the location of `clientlibrary.py` under `app/static/`.

```dos
> cd app\static
```

Type the following:

```dos
> python -m transcrypt -b clientlibrary.py
```

Make sure you see the the `__target__` folder created successfully. You can check by typing:

```dos
> dir
```

Now you are ready to create your database in your local computer. To do so, you need to go back to the root directory. This can be done with the following:

```dos
> cd ..\..
```

which means go up the folder two times. Or, simply

```dos
> cd %USERPROFILE\Downloads\d2w_mini_projects\mp_calc
```

You should see `application.py` in this root folder. Run the following commands:

```dos
> flask db init
> flask db migrate
> flask db upgrade
```

You should see a file called `app.db` and a folder `migrations`. 

Once this is done, you can run Flask by typing:

or
```dos
> flask run
```

You should see that some output will be thrown out, which one of them would be:

```dos
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Now you can open your browser at `http://127.0.0.1:5000/` to see the web app. You should see something like the following:

![](https://www.dropbox.com/s/nra8ltsjltlylp1/mp2_login.png?raw=1)

To stop the web app type `CTRL+C`. 

**MacOS/Linux**

First, make sure that you have done the following:
- actiate your virtual environment
- install all the required packages (see the instructions above)

Go to your root folder.
```shell
$ cd ~/Downloads/d2w_mini_projects/mp_calc
```

Now, we can go to the location of `clientlibrary.py` under `app/static/`.

```shell
$ cd app/static
```

Type the following:

```shell
$ python -m transcrypt -b clientlibrary.py
```

Make sure you see the the `__target__` folder created successfully. You can check by typing:

```shell
$ ls
```

Now you are ready to run your web app in your local computer. To do so, you need to go back to the root directory. This can be done with the following:

```shell
$ cd ../..
```
which means go up the folder two times. Or, simply
```shell
$ cd ~/Downloads/d2w_mini_projects/mp_calc/
```

You should see `application.py` in this root folder. Run the following commands:

```dos
> flask db init
> flask db migrate
> flask db upgrade
```

You should see a file called `app.db` and a folder `migrations`. 

Once this is done, you can run Flask by typing:

```shell
$ flask run
```

You should see that some output will be thrown out, which one of them would be:

```shell
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Now you can open your browser at `http://127.0.0.1:5000/` to see the web app. You should see something like the following:

![](https://www.dropbox.com/s/nra8ltsjltlylp1/mp2_login.png?raw=1)

To stop the web app type `CTRL+C`. 

#### Exercise 1 - Task 4

- Create several users. More than three users are recommended.
- Login using one of the user account.
- Navigate to the "Users" page using the navigation bar on the top. 

You should see all the users you have created sorted according to their usernames. An example is as shown below.

![](https://www.dropbox.com/s/o2w51fb3w0k8ibv/mp2_ex1.png?raw=1)

### Exercise 2

In this exercise, you will work with `serverlibrary.py` under the `app` folder. In order to do this, you need to complete **Week 4** Exercises in `mp2_exercises.ipynb`, particularly **Q2** onwards. 

#### Exercise 2 - Task 1

Implement the `Stack` class inside `serverlibrary.py`.

#### Exercise 2 - Task 2
Implement the `EvaluateExpression` class inside `serverlibrary.py`.

#### Exercise 3 - Task 3
Test your implementation by doing the following:
- Navigate to "Questions" page.
- Create several integer arithmetic expressions and assign it to different users. Note that you can assign more than one users for the same question.

If your `EvaluateExpression` is correct, you will see the correct **answer** displayed in the table as shown below.

![](https://www.dropbox.com/s/4u61v1hylndkcfl/mp2_questions.png?raw=1)

#### Exercise 3 - Task 4

Test also the other pages and see if they are working fine:
- Logout from your current user and login to one of the users you have assigned a challenge.
- After login, navigate to "Challenge" page and click "Show/Hide" to reveal the question. A timer starts when you click the button to reveal the question. 
- Put the answer in the provided input box, and click "Submit". If your answer is correct, the elapsed time will be displayed on the last column. Otherwise, nothing will be displayed in the last column.
- Answer several challenges with different users, then navigate to "Hall of Fame" page. If your `mergesort()` implementation is correct, you will see a table listing all the challenges with the fastest top three users for each of them.


### Expected Output

The expected output for both exercises 1 and 2 can be found in this video.

[Mini Project 2 Expected Output](http://vdimension.sutd.edu.sg/Player?8xd1aD4xCCP3J3nInZSK0FGXpal8Yr77PMy6PHKBP2k=)

## Optional: Deploying to Amazon Elastic Beanstalk

Check [Deploying to Amazon Elastic Beanstalk](DeployEB.md).

## References
- [Flask Tutorial using Templates](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates)
- [Flask Tutorial using Database](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)
- [Flask Tutorial for Login Page](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins)
- [Bootstrap Documentation](https://getbootstrap.com/docs/4.5/getting-started/introduction/)
- [SQLAlchemy Basic Relationship](https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html)