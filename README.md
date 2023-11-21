# django_ros2_status_push
### Install required files
### Run these codes
> Create a virtual environment
```
python3 -m venv virtual_environment_name
```
> Activate your virtual environment
```
source virtual_environment_name/bin/activate
```
```
python manage.py makemigrations
python manage.py migrate
```
> Run consumer.py
```
daphne -b 192.168.1.69 -p 19301 -v 2 robot_push.routing:application
```
> Run subscriber.py on a new terminal
```
cd robot_push
```
```
python subscriber.py       (<sub> if virtual environment is activated </sub>)
```
```
python3 subscriber.py      (<sub> if virtual environment is not activated </sub>)
