import os
import boto3
import pandas as pd
from faker import Faker
from PIL import Image
import io
import random
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


def connect_to_s3():

    try:
        aws_access_key_id = os.getenv("####")
        aws_secret_access_key = os.getenv("#####")
        aws_region = os.getenv("####")
        bucket_name = os.getenv("####")

        s3_client = boto3.client(
            "s3",
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=aws_region,
        )

        buckets = s3_client.list_buckets().get("Buckets", [])
        if any(bucket["Name"] == bucket_name for bucket in buckets):
            print(f"Connected to bucket '{bucket_name}' successfully!")
            return s3_client
        else:
            print(f"Bucket '{bucket_name}' does not exist.")
            return None
    #! errors
    except Exception as e:
        print("Error connecting to S3:", e)
        return None


def create_sample_image(size=(100, 100)):

    image = Image.new(
        "RGB",
        size,
        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
    )
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format="PNG")
    return img_byte_arr.getvalue()


def upload_image_to_s3(s3_client, image_name, image_data):

    try:
        s3_client.put_object(
            Bucket=os.getenv("AWS_BUCKET_NAME"),
            Key=image_name,
            Body=image_data,
            ContentType="image/png",
        )
        print(f"{image_name} uploaded successfully.")
    #! error
    except Exception as e:
        print(f"Error uploading {image_name} to S3:", e)


def upload_csv_to_s3(s3_client, df, file_key):

    try:
        csv_buffer = io.StringIO()
        df.to_csv(csv_buffer, index=False)
        s3_client.put_object(
            Bucket=os.getenv("AWS_BUCKET_NAME"),
            Key=file_key,
            Body=csv_buffer.getvalue(),
        )
        print(f"{file_key} uploaded successfully.")
    #! error
    except Exception as e:
        print(f"Error uploading {file_key} to S3:", e)


def generate_and_upload_data(s3_client):

    fake = Faker()

    # Generate Users data
    users = []
    for user_id in range(1, 11):
        profile_pic = f"users/profile_{user_id}.png"
        upload_image_to_s3(s3_client, profile_pic, create_sample_image())
        users.append([user_id, fake.name(), profile_pic, fake.text(50)])
    users_df = pd.DataFrame(users, columns=["UserID", "Name", "ProfilePicture", "Bio"])
    upload_csv_to_s3(s3_client, users_df, "users/users.csv")

    # Generating Posts data
    posts = []
    for post_id in range(1, 21):
        user_id = random.randint(1, 10)
        post_pic = f"posts/post_{post_id}.png"
        upload_image_to_s3(s3_client, post_pic, create_sample_image(size=(200, 200)))
        posts.append([post_id, user_id, fake.text(100), post_pic, datetime.now()])
    posts_df = pd.DataFrame(
        posts, columns=["PostID", "UserID", "Content", "PostPicture", "Timestamp"]
    )
    upload_csv_to_s3(s3_client, posts_df, "posts/posts.csv")

    # Generating Friends data
    friends = set()
    while len(friends) < 15:
        user_pair = tuple(sorted(random.sample(range(1, 11), 2)))
        if user_pair not in friends:
            friends.add(user_pair)
    friends_data = [[*pair, datetime.now().date()] for pair in friends]
    friends_df = pd.DataFrame(
        friends_data, columns=["UserID1", "UserID2", "FriendshipDate"]
    )
    upload_csv_to_s3(s3_client, friends_df, "friends/friends.csv")

    # Generating Comments data
    comments = [
        [
            comment_id,
            random.randint(1, 20),
            random.randint(1, 10),
            fake.text(50),
            datetime.now(),
        ]
        for comment_id in range(1, 51)
    ]
    comments_df = pd.DataFrame(
        comments, columns=["CommentID", "PostID", "UserID", "Content", "Timestamp"]
    )
    upload_csv_to_s3(s3_client, comments_df, "comments/comments.csv")


if __name__ == "__main__":
    s3_client = connect_to_s3()
    if s3_client:
        generate_and_upload_data(s3_client)
