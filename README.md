
# Institute Doctor Management System (Backend) - IT262 Project 

IDMS is a website where the students can book appointments for the Institute Doctor. It also has other features like appointment history, digital prescription, appointment alert.



## Run Locally

Clone the project

```bash
  git clone https://github.com/krish-patel1003/IT262_proj_backend.git
```

Go to the project directory

```bash
  cd IT262_proj_backend
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python manage.py makemigrations
  python manage.py migrate
  python manage.py collectstatic
  python manage.py runserver
```


