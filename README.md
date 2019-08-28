# Recommender-system
This is an online store developed using Django that makes use of k-means clustering and Apriori algorithms to make recommendations to its user. It is a part of my Bachelor's graduation thesis.

The training data is present in the `FYP.csv` file. It consists of 9400 sample orders. The scripts for k-means clustering and apriori algorithm are present in `k-means.py` and `apriori.py` files resepectively.

The environment is as follows:
- Python 3.6.7
- Anaconda 4.6.14
- Django 1.11.3

To train the data, please see the files mentioned above and execute them. To run the website, execute the code `python manage.py runserver` within the directory in the command line. Then on your browser, visit `http://127.0.0.1:8000`.
