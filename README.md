# MojeZeby.pl-Tools

## Description
Helper tools for managing the portal.

### Main functionality
- helps detect empty, or not translated labels

## Usage 
- ### End-users
After you login at [MojeZeby.pl-Tools](https://mojezebypl-tools.herokuapp.com/), you can make use of **Translate** tool, with workflow as follows:
1. upload *.json files with English and Spanish translations to compare
1. browse (and fix) empty, or not translated labels
1. get all available translations as *.json file

- ### Developers
_In order to use this app locally you need to have [Python](https://www.python.org/downloads/) installed on your machine._

```sh
py -m venv venv
source venv/Scripts/activate
git clone https://github.com/pythonsway/mojezebypl-tools.git
cd mojezebypl-tools
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Built with:
* [Django](https://www.djangoproject.com/)


Hosted on [https://mojezebypl-tools.herokuapp.com/](https://mojezebypl-tools.herokuapp.com/)