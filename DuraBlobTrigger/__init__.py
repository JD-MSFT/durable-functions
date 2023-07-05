import logging

import azure.functions as func
import azure.durable_functions as df


async def main(myblob: func.InputStream, starter: str):
    logging.info(
        f"Python blob trigger function processed blob \n"
        f"Name: {myblob.name}\n"
        f"Blob Size: {myblob.length} bytes"
    )
    client = df.DurableOrchestrationClient(starter)
    instance_id = await client.start_new(
        "DurableFunctionsOrchestrator", client_input={"blob_name": myblob.name}
    )

    logging.info(f"Started the orchestration from blob trigger! {instance_id}")
