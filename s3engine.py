from boto.s3.connection import S3Connection
from boto.s3.key import Key

import conf

class S3Engine:
    
    def __init__(self):

        # Create a connect to S3 and store it
        self.conn = S3Connection(conf.aws_access_key, conf.aws_secret_key)

    def push_file(self, key_name, path_of_file_to_push):
        
        # Get the bucket.
        # Turning validate to off doesn't validate if the specified bucket 
        #  exists, so be make sure it does. (saves money)
        bucket = self.conn.get_bucket(conf.bucket, validate=False) 

        # Prepare a key
        packet = Key(bucket)
        packet.key = key_name

        # Insert the data
        with open(path_of_file_to_push) as f:
            bytes_pushed = packet.set_contents_from_file(f)

        return bytes_pushed
