import fnmatch
import os
from azure.storage.blob import *

connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
container_client = blob_service_client.get_container_client("test")
blob_list = container_client.list_blobs("tenant")
print("rut,ruta,nombre de archivo,peso")
for blob in blob_list:
    path = blob.name.split("/")
    if fnmatch.fnmatch(blob.name, "*/resources/*") and len(path) == 4:
        nombre = path[len(path) - 1]
        print("\t" + path[1] + ",\t" + blob.name.replace(path.pop(), "") + ",\t" + nombre + ",\t" + str(
            blob.size * 0.001) + "KB")


