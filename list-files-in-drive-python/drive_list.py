from __future__ import print_function

from googleapiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
import shutil
import io
from googleapiclient.http import MediaIoBaseDownload

SCOPES = (
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/devstorage.full_control',
    'https://www.googleapis.com/auth/cloud-vision',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/documents'
)
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('./client_id.json', SCOPES)
    creds = tools.run_flow(flow, store)
DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))


def drive_get_img(fname):
    'download file from Drive and return file info & binary if found'

    # search for file on Google Drive
    rsp = DRIVE.files().list(q="name='%s'" % fname,
                             fields='files(id,name,mimeType,modifiedTime)'
                             ).execute().get('files', [])
    # download binary & return file info if found, else return None
    if rsp:
        target = rsp[0]  # use first matching file
        fileId = target['id']
        fname = f'{target["name"]}.html'
        mtype = target['mimeType']
        binary = DRIVE.files().export_media(fileId=fileId, mimeType='text/html').execute()
        file_id = fileId
        request = DRIVE.files().export_media(fileId=file_id,  mimeType='text/html')
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print
            "Download %d%%." % int(status.progress() * 100)

        # The file has been downloaded into RAM, now save it in a file
        fh.seek(0)
        with open(fname, 'wb') as f:
            shutil.copyfileobj(fh, f, length=131072)
        return fname, mtype, target['modifiedTime'], binary


files = DRIVE.files().list().execute().get('files', [])
for f in files:
    if f['name'].endswith('doc'):
        print(f['name'])
        drive_get_img(f['name'])
