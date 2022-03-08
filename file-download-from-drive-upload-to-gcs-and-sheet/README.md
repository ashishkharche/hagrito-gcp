# File download from drive, upload to gcs and sheet

## Create virtualenv

## Install

```
python -m pip install -U pip google-api-python-client oauth2client
```

## Configure oauth client id (desktop app)

On google cloud console.

Download and save as "client_secret.json"

## Enable Google APIs

(Cloud Storage and Cloud Vision) and another pair from G Suite (Google Drive and Google Sheets)

## Create a bucket in Google cloud storage

Add bucket name in the code

## Run

```
python analyze_gsimg.py
```

## References

[Image archiving, analysis, and report generation with G Suite & GCP  |  Google Codelabs](https://codelabs.developers.google.com/codelabs/drive-gcs-vision-sheets/#12)