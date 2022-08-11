import fnmatch
import os

from azure.storage.blob import BlobServiceClient

try:
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_client = blob_service_client.get_container_client("prod")
    blob_list = container_client.list_blobs("tenant")
    log = open("resultado.txt", "w")
    print("Imprimiendo los resultados en " + log.name)
    for index, blob in enumerate(blob_list):
        blobName = blob.name
        path = blobName.split("/")
        if fnmatch.fnmatch(blobName, "*/resources/*") and len(path) == 4:
            nombre = path[len(path) - 1].encode(encoding='ascii', errors="replace").decode(encoding="ascii",
                                                                                           errors="replace")
            log.write(path[1] + ", " + blobName.replace(path.pop(), "") + ", " + nombre + ", " + str(
                blob.size * 0.001) + "KB \r")
    log.close()
    print("Resultados guardados.")

except Exception as ex:
    print('Exception:')
    print(ex)
