# CSV to Sheet trigger from GCS function JS

## Create Google Cloud project

Enable Google Sheets, Google Build API

## Service Account

Create a Service Account

## Create a bucket in Google Cloud Storage 

In bucket permissions tab, give storage admin role to the service account email created.

## Create Spreadsheet

In Spreadsheet share -> Share with others, give service account email the editor role.

## Cloud function

### Configuration

Select trigger for Cloud Storage.

Event Type: Finalizing/Creating in bucket

Select Service Account previously created.

![](https://i.imgur.com/IVHJfAr.png)

Environmental variable:

```
SPREADHSHEET_ID -> <ID OF SPREADSHEET>
```

### Code

Select Node JS runtime of your choice like 10, 16

Add code from `index.js` in inline editor.

Change function entry point to the function name of exports.

Modify package.json to include dependencies required.

Click deploy.

## Run

Upload csv file with some content to Cloud Storage bucket.

The cloud function will run and update our sheet with data.+

## References

[Cloud Function to Automate CSV data import into Google Sheets](https://codelabs.developers.google.com/codelabs/cloud-function2sheet?hl=en#5)