from linkedin_api import search_jobs
from job_analysis import analyze_job_description
from utils import save_to_s3
from config import S3_BUCKET_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

def main():
  """Main scraping and analysis loop."""
  keywords = "Director of Architecture"
  jobs = search_jobs(keywords)  # Fetch jobs from LinkedIn

  for job in jobs:
    job_description = job['description']  # Retrieve the job description
    analysis_results = analyze_job_description(job_description)  # Analyze
    
    # Save results to S3 
    save_to_s3(analysis_results, f"{job['id']}.json", S3_BUCKET_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY) 

if __name__ == '__main__':
  main()
