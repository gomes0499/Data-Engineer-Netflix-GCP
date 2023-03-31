import os
import json
import random
import time
from faker import Faker
from google.cloud import pubsub_v1
import configparser

# Get the full path to the config.ini file
config = configparser.ConfigParser()
config.read("/Users/gomes/Desktop/Projects/Data Engineer/6-Project /config/config.ini")

fake = Faker()

project_id = config.get("pubsub", "project_id")
topic_id = config.get("pubsub", "topic_id")

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

content_categories = ["TV Show", "Movie", "Documentary", "Stand-up Comedy"]
genres = ["Drama", "Comedy", "Action", "Horror", "Sci-Fi", "Thriller", "Romance", "Adventure", "Crime", "Fantasy", "Mystery", "Animation", "Biography", "Family", "History", "Sport", "Music", "War", "Western"]


def generate_user():
    user = {
        "user_id": fake.uuid4(),
        "name": fake.name(),
        "email": fake.email(),
        "age": random.randint(18, 80),
        "gender": random.choice(["M", "F"]),
        "subscription_plan": random.choice(["Basic", "Standard", "Premium"]),
        "subscription_start_date": str(fake.date_between(start_date="-3y", end_date="today")),
    }
    return user

def generate_interaction(user_id):
    interaction = {
        "user_id": user_id,
        "content_id": fake.uuid4(),
        "content_title": fake.sentence(),
        "content_category": random.choice(content_categories),
        "genre": random.choice(genres),
        "watch_date": str(fake.date_between(start_date="-1y", end_date="today")),
        "rating": random.choice([1, 2, 3, 4, 5]),
        "session_duration": random.randint(1, 180),  # in minutes
    }
    return interaction


def publish_interaction(interaction):
    data = json.dumps(interaction).encode("utf-8")
    future = publisher.publish(topic_path, data)
    return future.result()

num_users = 10

users = [generate_user() for _ in range(num_users)]

while True:
    user = random.choice(users)
    interaction = generate_interaction(user["user_id"])
    message_id = publish_interaction(interaction)
    print(f"Published message {message_id}")

    time.sleep(random.uniform(0.5, 1))  # Adjust the frequency of messages here
