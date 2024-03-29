# Speech to Text subtitle srt gcs - python

## Create Google cloud project

## Download gcloud locally

## Set project

### Method 1

Check if correct account is logged in.

```
$ gcloud auth list
```

Check if correct project is being worked on.

```
$ gcloud config list project
```

Change project ID to desired project.

```
$ gcloud config set project subtitlespython
```

### Method 2

gcloud init configuration

```
$ gcloud init
```

Set enviromental variable

```
export PROJECT_ID=$(gcloud info --format='value(config.project)')
```

## Enable APIs

```
$ gcloud services enable speech.googleapis.com texttospeech.googleapis.com translate.googleapis.com storage-component.googleapis.com
```

## Create virtualenv

Go to working directory

```
python -m venv venv
```

```
source venv/Scripts/activate
```

## Install dependencies

```
python -m pip install -r requirements.txt
```

## Storage buckets

Create two buckets in Google Cloud Storage

One for input and other for output.

Export enviromental variables.

```
BUCKET_IN=[YOUR_FIRST_BUCKET]
BUCKET_OUT=[YOUR_SECOND_BUCKET]
```

Create buckets:

```
gsutil mb gs://$BUCKET_IN
gsutil mb gs://$BUCKET_OUT
```

## Service Accounts

Create:

```
gcloud iam service-accounts create ml-dev --description="ML APIs developer access" --display-name="ML Developer Service Account"
```

Grant ml developer role

```
gcloud projects add-iam-policy-binding $PROJECT_ID --member serviceAccount:ml-dev@$PROJECT_ID.iam.gserviceaccount.com --role roles/ml.developer
```

Grant Project Viewer role

```
gcloud projects add-iam-policy-binding $PROJECT_ID --member serviceAccount:ml-dev@$PROJECT_ID.iam.gserviceaccount.com --role roles/viewer
```

Grant Storage object admin role

```
gcloud projects add-iam-policy-binding $PROJECT_ID --member serviceAccount:ml-dev@$PROJECT_ID.iam.gserviceaccount.com --role roles/storage.objectAdmin
```

Create json key for service account

```
gcloud iam service-accounts keys create ./ml-dev.json --iam-account ml-dev@$PROJECT_ID.iam.gserviceaccount.com
```

## Transcribe

Upload audio to cloud storage

```
gsutil cp example.wav gs://$BUCKET_IN/
```

Transcribe

```
python3 speech2srt.py --storage_uri gs://$BUCKET_IN/example.wav --sample_rate_hertz 24000
```

## Translate

Copy english text file to input bucket

```
gsutil cp en.txt gs://$BUCKET_IN/
```

Emtpy the output bucket

```
gsutil rm gs://$BUCKET_OUT/*
```

Translate

```
python3 translate_txt.py --project_id $PROJECT_ID --source_lang en --target_lang ko,hi --input_uri gs://$BUCKET_IN/en.txt --output_uri gs://$BUCKET_OUT/
```

Copy output files to local

```
gsutil cp gs://$BUCKET_OUT/* .
```

View the index.csv file, which contains information about the translation operation output files:

Here you can see that the service translated the source file en.txt and wrote two output files, in Hindi and Korean, respectively.

```
cat index.csv
```

Create SRT subtitles from the Hindi and Korean plain text files:

```
python3 txt2srt.py --srt en.srt --index index.csv
```

## References

[Creating translated subtitles with AI  |  Google Cloud Platform Community](https://cloud.google.com/community/tutorials/speech2srt)

[Using the Speech-to-Text API with Python](https://codelabs.developers.google.com/codelabs/cloud-speech-text-python3#3)