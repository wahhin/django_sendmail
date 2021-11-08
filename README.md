To add a data table to database, add it in to models.py. Follow the format that already exists and look up the documentation for models in django if you need to add additional fields. 

All data manipulation should be done in views.py or index.html or any other html files that you want to use. I manipulated the data from views. Something to note is the fact that whatever data you get from models is in a QuerySet format which you will have to change accordingly, which would explain the float() or string() function in what I have.

You can add charts into the index.html file. Just copy paste the previous chart and add whatever data you need under the lists for data and labels. Just follow what I have done to get a better idea. I advise not changing anything from what is already there to study how I got the outputs. 

settings.py and admin.py will not have to be touched too much. The same goes for urls.py unless you need to add more pages to your app.

REMEMBER TO USE THIS IN A VIRTUAL ENVIRONMENT SO THAT PACKAGES INSTALLED DON'T GET MIXED UP.

Please install the necessary packages from the requirements.txt file by running this code in your command prompt in the folder that your app is in (in virtual environment of course)

```
pip install -r requirements.txt
```

