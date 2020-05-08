# Flask_Celery_-Boilerplate-mock-task-included-
This Boilerplate solves the issue pf circular importation when using celery

It tries to solve this by spliting the typical make_celery() function into two different ones: 
- The first creating a Celery app instance, and 
- Another performing the tasks needed to bind that exact instance to the Flask app.

