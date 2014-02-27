import os
import tarfile

class Archiver:
    def create_archive(self, source_folder_path, destination_path):
        with tarfile.open(destination_path, "w:gz") as tar:
            tar.add(source_folder_path, 
                    arcname=os.path.basename(source_folder_path))
