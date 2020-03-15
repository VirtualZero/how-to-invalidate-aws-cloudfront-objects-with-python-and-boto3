import boto3
from time import time


cloudfront_dist_id='DistId123'

cloudfront = boto3.client('cloudfront')
response = cloudfront.create_invalidation(
    DistributionId=cloudfront_dist_id,
    InvalidationBatch={
        'Paths': {
            'Quantity': 3,
            'Items': [
              '/dir1/file1',
              '/dir1/file2',
              '/dir2/file3'
            ]
        },
        'CallerReference': str(time()).replace(".", "")
    }
)
