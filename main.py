import sys
import os

from s3engine import S3Engine

if __name__ == "__main__":
    
    file_path = ""
    upload_key = ""

    if len(sys.argv) != 3:
        print "Usage:"
        print sys.argv[0] + " <file to upload> <upload key>"
        exit(1)
    else:
        file_path = sys.argv[1].strip()
        upload_key = sys.argv[2].strip()

    # Check if file exists
    if not os.path.isfile(file_path):
        print "File to push doesn't exist"
        exit(2)

    # Check that key isn't empty
    if len(upload_key) == 0:
        print "Key can't be empty"
        exit(3)

    s3Engine = S3Engine()
    bytes_pushed = s3Engine.push_file(upload_key, file_path)

    print str(bytes_pushed) + " bytes pushed to S3"
