This is an app, which can be used only for detecting publicly available Google Sheet column data types, developed for datarobot as home test.

Technical specification

1. Odoo is used as website. You can read more about Odoo here https://www.odoo.com
2. Python as the back-end language for detecting without any additional libraries.
3. Google Sheet API v4 is used for reading sheets info.

You can try using app just now. Please follow these steps.

1. Visit page http://ec2-100-26-10-55.compute-1.amazonaws.com:8069.
2. Register on website.
3. Try your publicly available Google Sheet and get data types.

If you are developer you can also try to build this app locally. Please follow these simple steps.

1. Clone repository.
2. Assume that you already have enabled Google Sheets API and get API key. You can make it here: https://console.developers.google.com
3. Assume that you already have installed docker-compose, docker.
If not follow instructions: https://www.digitalocean.com/community/tutorials/docker-ubuntu-18-04-1-ru
 https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-ubuntu-18-04-ru
4. In root folder of repository run commands:

sudo docker build --no-cache -t datarobot/odoo:latest .
sudo docker-compose up

5. You start your Odoo instance.
6. Open http://127.0.0.1:8069/web/database/manager. Create database via database manager. For master password use admin_passwd from odoo.conf
7. You will be redirected to apps menu in odoo. In Search remove filter, enter datarobot. Install.
You will be redirected to website choose default page. Use default.
8. In the left corner press button and in dropdown menu press Settings.
9. Scroll to bottom of the page. Press Activate the Developer Mode.
10. Open Settings again. You will find at the header new menus. Press Technical, find System Parameters, press it.
11. Press Create. In field key -> google_sheet_api_key, in field value -> your API Key. Save.
12. Open Settings again. Choose website on the left. Find Customer Account. Check Free sign up. Save.
13. Open Website app appeared in dropdown in the left corner. Go to Website.
14. Now you can use this app.
15. You are logged in as Administrator. Other portal users can also use it after register on website.
16. Enjoy!