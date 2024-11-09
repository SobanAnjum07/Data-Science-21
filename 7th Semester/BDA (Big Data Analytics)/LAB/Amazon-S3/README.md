Here's how you can setup and run the code in app.py.
---

# Project Name

This project connects to an AWS S3 bucket, generates sample user data and images using the Faker and Pillow libraries, and uploads them to S3 in organized folders. It also includes uploading data in CSV format for users, posts, friends, and comments.

## Prerequisites

- Python 3.x
- AWS account with access to S3
- AWS credentials for access keys and bucket information
- A `.env` file containing your AWS S3 configuration

## Setup Guide

### Step 1: Clone the Repository
First, clone this repository to your local machine:
```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Set Up a Virtual Environment (Optional but Recommended)
Create a virtual environment to manage dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### Step 3: Install Dependencies
Install all dependencies listed in the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
1. Create a `.env` file in the project root directory.
2. Add the following environment variables to `.env`:

```plaintext
AWS_ACCESS_KEY_ID=<your_aws_access_key>
AWS_SECRET_ACCESS_KEY=<your_aws_secret_key>
AWS_REGION=<your_aws_region>
AWS_BUCKET_NAME=<your_s3_bucket_name>
```

Make sure these values correspond to your AWS S3 credentials and bucket information.

### Step 5: Run the Application
Run the `app.py` script to generate and upload data to your specified S3 bucket:
```bash
python app.py
```

If the connection to S3 is successful, it will create sample images and CSV files and upload them to the configured S3 bucket.

### Output
The script will print messages confirming each file upload:
- Successful connection to the specified S3 bucket
- Upload confirmations for profile pictures, posts, and CSV files for `users`, `posts`, `friends`, and `comments`.

---

## File Structure

- `app.py`: Main application code to generate and upload data.
- `requirements.txt`: List of Python dependencies.
- `.env`: (User-created) Environment file with AWS credentials.
- `README.md`: Guide to setting up and running the project.

---

## Troubleshooting

- **Error Connecting to S3**: Verify the credentials in your `.env` file are correct and have necessary S3 permissions.
- **Library Installation Issues**: Make sure your Python environment matches the project requirements, especially the versions specified in `requirements.txt`.


