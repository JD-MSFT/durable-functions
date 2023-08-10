# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json

import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    # uncomment this code to test the blob trigger
    # input = context.get_input()
    # result1 = yield context.call_activity('Durable', input['blob_name'])
    result1 = yield context.call_activity('Durable', "Tokyo")
    result2 = yield context.call_activity('Durable', "Seattle")
    result3 = yield context.call_activity('Durable', "London")
    return [result1, result2, result3]

main = df.Orchestrator.create(orchestrator_function)