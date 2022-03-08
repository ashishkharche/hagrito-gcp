
# Speech To Text to Docs - Java

## Cloud setup

### Create new cloud project

Go to http://console.cloud.google.com/ and create new project or use existing one.

You will need to enable billing in your google cloud account.

### Get a service account key for the Cloud Speech-to-Text API

- Head over to the [GCP console](https://console.cloud.google.com) and find your new project\* Create a service account

- Download a service account key as JSON

- Set the environment variable **_GOOGLE_APPLICATION_CREDENTIALS_** to the file path of the JSON file that contains your service account key.

If you using Git bash, set environmental variable in `~/.bashrc`

If you are using cmd on windows, set environmental variable as usual using the GUI.

#### Git bash example

In `~/.bashrc`

```
export GOOGLE_APPLICATION_CREDENTIALS="/t/github/gcp/speechdocs/docs-transcript-codelab/untitled2/src/main/resources/ServiceAccounts.json"
```

### Get Credentials for the Docs API

- Back in the [GCP console](https://console.cloud.google.com), go to **Credentials**

- Create an OAuth 2.0 key and download it as JSON

- Rename the file `credentials.json` and make sure it is in the `src/main/resources/` directory of your code

Add `redirect_uri` as `http://localhost:8888/Callback`

### Enable APIs

- Select the **Dashboard** tab, click the **Enable APIs and Services** button and enable the following 2 APIs:

- **Speech to Text**

- **Google Docs**

## App setup

### Gradle init

```
$ gradle init --type basic
```

Select groovy or kotlin.

Project name: SpeechToTextDocsJava

### Structure

```
$ tree -f
.
|-- ./build.gradle
|-- ./gradle
|   `-- ./gradle/wrapper
|       |-- ./gradle/wrapper/gradle-wrapper.jar
|       `-- ./gradle/wrapper/gradle-wrapper.properties
|-- ./gradlew
|-- ./gradlew.bat
`-- ./settings.gradle

2 directories, 6 files
```

### Add dependencies

From `build.gradle` file

### Create java and resources directories

```
mkdir -p src/main/java src/main/resources
```

### Add code and resources

```
$ tree -f
.
`-- ./main
    |-- ./main/java
    |   `-- ./main/java/CreateTranscript.java
    `-- ./main/resources
        |-- ./main/resources/ServiceAccounts.json
        |-- ./main/resources/credentials.json
        `-- ./main/resources/soundoftext-8000hz.wav

3 directories, 4 files
```

### Run

```
./gradlew run
```

You will need to give access to the app.

### Output

In the output on terminal, you will see a link to Google docs generated.
