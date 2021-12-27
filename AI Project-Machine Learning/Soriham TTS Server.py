import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db
import os
import requests
import glob
import boto3
from google.cloud import storage

#local path -> change if computer change
os.chdir("Downloads/TTS")
path=os.getcwd()
cred = credentials.Certificate("/Users/yunseok/Desktop/firebase_key.json")#경로 수정 필요
firebase_admin.initialize_app(cred)

#start google cloud storage
storage_client = storage.Client.from_service_account_json('/Users/yunseok/Downloads/neon-net-333104-b3f13972ab4a.json')
#파일 공유할 저장소 이름을 설정해 주면됩니다.
#parameter순서대로 공유된 파일이름, 로컬저장된파일 경로, 저장소 이름 
def upload_to_bucket(blob_name, path_to_file, bucket_name):
    """ Upload data to a bucket(아까 만들었던 저장소)"""
    # Explicitly use service account credentials by specifying the private key
    # file.
    storage_client = storage.Client.from_service_account_json('/Users/yunseok/Downloads/neon-net-333104-b3f13972ab4a.json')
    #print(buckets = list(storage_client.list_buckets())
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(path_to_file)
    #접근권한 public 으로 설정
    blob.make_public()    
    #파일 url 만들어주기
    url = blob.public_url
    #returns a public url
    return url
#parameter순서대로 공유된 파일이름, 로컬저장된파일 경로, 저장소 이름 

def removeAllFile(filepath):
    if os.path.exists(filepath):
        for file in os.scandir(filepath):
            os.remove(file.path)
        return 'Remove All File'
    else:
        return 'Directory Not Found'

def download(url, file_name):
    with open(file_name+".mp3", "wb") as file:
        response=requests.get(url)
        file.write(response.content)
        os.system('ffmpeg -i '+file_name+".mp3 -vn output.m3u8")

db=firestore.client()
users_ref = db.collection(u'chats')
query=users_ref.order_by("createdAt")

list=[]
docs = query.get()
for doc in docs:
    list.append(u'{}'.format(doc.to_dict()['text']))

file_path="/Users/yunseok/Downloads/TTS"
removeAllFile(file_path)
#read last sentence
text=list[-1]
#TTS 서버 수정 해줘야 함
url='http://TTS server link/tts-server/api/infer-glowtts?text='+text
download(url, "TTS")

#Upload TTS(m3u8, ts) file to google cloud storage
if user=="엄마" : 
    upload_to_bucket("mom/TTS.mp3","/Users/yunseok/Downloads/TTS/TTS.mp3","uploadtts")
    upload_to_bucket("mom/output.m3u8","/Users/yunseok/Downloads/TTS/output.m3u8","uploadtts")
    tsCounter=len(glob.glob1("/Users/yunseok/Downloads/TTS","*.ts"))
    for number in range(0, tsCounter):
        file_name="output"+str(number)+".ts"
        upload_to_bucket("mom/output"+str(number)+".ts","/Users/yunseok/Downloads/TTS/output"+str(number)+".ts","uploadtts")
elif user=="아빠" :
    upload_to_bucket("dad/TTS.mp3","/Users/yunseok/Downloads/TTS/TTS.mp3","uploadtts")
    upload_to_bucket("dad/output.m3u8","/Users/yunseok/Downloads/TTS/output.m3u8","uploadtts")
    tsCounter=len(glob.glob1("/Users/yunseok/Downloads/TTS","*.ts"))
    for number in range(0, tsCounter):
        file_name="output"+str(number)+".ts"
        upload_to_bucket("dad/output"+str(number)+".ts","/Users/yunseok/Downloads/TTS/output"+str(number)+".ts","uploadtts")