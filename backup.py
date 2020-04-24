import os, shutil, datetime, sys
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

assert(len(sys.argv) == 2)
SERVER = sys.argv[1]
ARC_FORMAT = "gztar"

connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

container_name = os.getenv('AZURE_MC_CONTAINER')
container_client = blob_service_client.get_container_client(container_name)


t = datetime.datetime.now()
arc_base = SERVER + t.strftime("_%y-%m-%d-%H%M")
arc_path = shutil.make_archive(arc_base, ARC_FORMAT, "/opt/minecraft", base_dir=SERVER)
with open(arc_path, 'rb') as arc_data:
  container_client.upload_blob(os.path.basename(arc_path), arc_data)
os.remove(arc_path)
