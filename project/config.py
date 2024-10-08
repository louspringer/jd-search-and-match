import os

# LinkedIn API Credentials
LINKEDIN_API_KEY = os.getenv('LINKEDIN_API_KEY')
LINKEDIN_API_SECRET = os.getenv('LINKEDIN_API_SECRET')

# S3 Bucket Configuration
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')

# Master Resume JSON
MASTER_RESUME_FILE = 'master-resume.json'
