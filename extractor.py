import tarfile, zipfile, os

def extract_bundle(file_path, extract_to="data"):
    os.makedirs(extract_to, exist_ok=True)

    if file_path.endswith(".tar.gz"):
        with tarfile.open(file_path, "r:gz") as tar:
            tar.extractall(extract_to)

    elif file_path.endswith(".zip"):
        with zipfile.ZipFile(file_path) as zip_ref:
            zip_ref.extractall(extract_to)

    return extract_to
