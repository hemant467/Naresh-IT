from azure.storage.blob import BlobServiceClient

def download_blob_data(connection_string, container_name, blob_name):
    """
    Connects to Azure Blob Storage and downloads the file as bytes.
    """
    try:
        if not connection_string or not container_name or not blob_name:
            print("[read_data] Missing connection parameters.")
            return None

        print(f"[read_data] Connecting to Azure Blob: {blob_name}...")
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        blob_client = blob_service_client.get_container_client(container_name).get_blob_client(blob_name)
        
        pdf_bytes = blob_client.download_blob().readall()
        print(f"[read_data] Download successful. Size: {len(pdf_bytes)} bytes.")
        return pdf_bytes
    except Exception as e:
        print(f"[read_data] Error: {e}")
        return None