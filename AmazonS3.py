import boto
import boto.s3
import sys
from boto.s3.key import Key

AWS_ACCESS_KEY_ID = 'AKIAIIEQYE3ADFJSXXBQ'
AWS_SECRET_ACCESS_KEY = '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'

bucket_name = 'recipe-user-uploads'
conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY)


bucket = conn.create_bucket(bucket_name,
    location=boto.s3.connection.Location.DEFAULT)

testfile = "uploads/keto.jpg"
print 'Uploading %s to Amazon S3 bucket %s' % \
   (testfile, bucket_name)

def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()


k = Key(bucket)
k.key = 'my test file'
k.set_contents_from_filename(testfile,
    cb=percent_cb, num_cb=10)