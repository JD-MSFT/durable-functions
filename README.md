# Azure Durable Functions Demo

Demonstration of Python [Durable Functions](https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-overview?tabs=python).

This demonstration is of the [Function Chaining Pattern](https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-overview?tabs=python#chaining), triggered either by HTTP or Blob upload.
There are several [common Durable patterns](https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-overview?tabs=python) and [trigger types](https://learn.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings?tabs=python).

Configure the host.json to update desired "hubName" and "functionTimeout" time (-1 for infinite) when deploying in Azure.

Create a [local.settings.json](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-local#local-settings-file) configuration in the root directory for local testing and development.
