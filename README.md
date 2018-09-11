# Simple Directory Manager: Django + Bootstrap

Skillset:
- Django
- Bootstrap + HTML5
- Integration frontend <-> backend

Project summary:
- input: we provide a HTML5 template, based on Bootstrap 4.1
- output: you deliver a working Django 2.1 application, deployed and integrated with the provided frontend.

For the Django application, the following must be provided:
- fully working django app
- with the models / views / urls needed to implement the functionality requested
- detailed list of requirements, preferable with Pipenv

The application is based on the provided frontend template, which must be integrated with the Django backend.
- The template can be seen live here: http://webapplayers.com/inspinia_admin-v2.8/table_data_tables.html
- The template is currently *not* a Django template
- We want to base our application on the HTML5 version of the template (based on Bootstrap 4.1)
- The whole template must be included as part of the static files in the django application (not only the two pages that we will currently need) 
- The page described below must be converted to a Django template.
- The provided template has a lot of features. We want to keep the frontend as it is, with the minimal changes needed to support the features listed below.
- No further customization needs to be done.

We need only one page:

A directory page. This is a simple data table, with the following requirements:
- sorting must work, by clicking on the corresponding table header
- a checkbox must be added to each header. By default all checkboxes are selected. Search / filtering is performed on the selected checkboxes.
- pagination must work
- the CSV button must export the data as filtered, and provide a download.csv file. All pages must be included in the .csv, not only the currently displayed page.

When typing into the search box:
- the table must get updated (dynamic search)
- pagination is done based on the filtered items: pagination display will be updated dynamically while the search is entered (dynamic pager)

Clicking into the checkboxes will update:
- the table, with the corresponding search
- the pager

We will provide access to a GitHub repository where the initial assets (the frontend) will be provided.
The application must be deployed into any online service (Digital Ocean or similar), so that it can be tested live.

A README must be providing detailing:
- technologies and libraries used, for the Django backend and the frontend
- detailed deploy process (preferable with a Dockerfile), so that we can reproduce the deploy in our in-premises systems.

Please note that we will need an invoice for the paid amount.

# Deploy

Deploy is done to Heroku: https://dashboard.heroku.com/teams/cactea/overview
