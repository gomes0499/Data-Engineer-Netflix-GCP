import argparse
import logging
import json
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions
from apache_beam.io import ReadFromPubSub
from apache_beam.io import WriteToText
from apache_beam import WindowInto
from apache_beam.transforms.window import FixedWindows
from apache_beam.transforms.trigger import AfterCount, AccumulationMode


def parse_message(message):
    interaction = json.loads(message)
    return interaction['user_id'], interaction


def calculate_aggregates(user_interactions):
    user_id, interactions = user_interactions
    result = {
        "user_id": user_id,
        "total_movies_watched": len(interactions),
        "total_session_duration": sum(interaction["session_duration"] for interaction in interactions),
    }
    return result


def main(argv=None):
    project_id = 'wu6project'
    input_subscription = f"projects/{project_id}/subscriptions/wu6sub"
    output_path = "gs://wu6process/output"

    pipeline_options = PipelineOptions(
        flags=argv,
        runner='DataFlowRunner',
        project=project_id,
        job_name='wu6job',
        temp_location='gs://wu6process/temp',
        region='us-central1',
        allow_unsafe_triggers=True,
        streaming=True,
        staging_location='gs://wu6process/staging',
    )
    pipeline_options.view_as(SetupOptions).save_main_session = True

    with beam.Pipeline(options=pipeline_options) as p:
        (
            p
            | "Read from Pub/Sub" >> ReadFromPubSub(subscription=input_subscription)
            | "Parse Message" >> beam.Map(parse_message)
            | "Windowing" >> WindowInto(
                FixedWindows(60),
                trigger=AfterCount(10),
                accumulation_mode=AccumulationMode.DISCARDING)
            | "Group by key" >> beam.GroupByKey()
            | "Calculate Aggregates" >> beam.Map(calculate_aggregates)
            | "Serialize to JSON" >> beam.Map(json.dumps)
            | "Write to GCS" >> WriteToText(output_path)
        )

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    main()
