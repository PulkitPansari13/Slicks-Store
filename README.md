<br>
<p align="center">
  <img src="https://github.com/PulkitPansari13/Slicks-Store/blob/main/static/img/logo_sm.png" alt="Logo" height = "100"/>
  <h3 align="center">Slicks - The Fashion Store</h3>
</p>

## Features 
1. Fully functional and mobile responsive 📱 fashion e-commerce 🤳 website.
2. Ability to build guest cart 🛒 i.e add/remove products to cart while logged out, will be prompted to login to place order.
3. Cloudinary image cdn integration for faster ⚡ load times.
4. Secure payments 💳 integration with razorpay.

## Live demo
Checkout the project deployed at [slicks.herokuapp.com](https://slicks.herokuapp.com/).<br>
To make dummy payment select 'CARD' as payment method and enter '4111111111111111' as card number, any future date as expiry and any random cvv.<br>
PS: Since heroku uses dynos to serve website, it might take time for initial load of the website as dynos wake from sleep if there is no visit to the website in last half hour.

## Running locally
To run the project locally, create a virtual environment and clone the repo.
```
git clone https://github.com/PulkitPansari13/Slicks-Store
```

Install the dependencies from requirements.txt.
```
pip install -r requirements.txt
```

Make database migrations and runserver. Before you run the surver you need to specify the environment variable, follow the guide below. 
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
``` 
Now create a superuser using the `python manage.py createsuperuser` command and try adding some dummy products form the `admin` page.

Done. Everything is setup, try placing a test order. 

## Tech Stack
1. Django
2. HTML
3. CSS
4. Vanilla JS
5. PostgeSQL

---
#### Setting up environment variables:
All the private keys are stored in a separate `.env` file to protect sensitive information.
1. First rename the `.template_env` to `.env`. The file follows the syntax:
``` 
KEY=YourAwesomeKey  --without any quotes.
```
2. `SECRET_KEY` is required or else the server won't start, you can grab one from [here](https://djecrety.ir/) or generate one locally following this [guide](https://humberto.io/blog/tldr-generate-django-secret-key/).
3. This project uses Cloudinary for media storage, you can signup to obtain keys or else you can remove the `CLOUDINARY_STORAGE` and `DEFAULT_FILE_STORAGE` settings from `settings.py` file to serve media locally.
4. If you are using the default SQLite3 database you can leave the DATABASE related values blank or else specify them.
5. EMAIL related values can be blank, it won't cause error but if you do want to send emails on signup and successful order, specify them.
6. For reCaptcha to work correctly specify the keys which you can create from [here](https://www.google.com/recaptcha/admin/create) and select the type as v2.
7. For payments, create an account on razorpay and create a new api key. Copy the same to the respective razorpay variables