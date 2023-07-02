# pyspark-devcontainer
This development container provides a convenient and quick way to get started with Apache Spark and Python 3.

There are some dependencies that should be installed to use VS Code Dev Containers. See instruction [here](https://code.visualstudio.com/docs/remote/containers#_installation).


Install python extension

install findspark with pip install findspark

i think this is optional but this is the configuration file for a pyspark kernel
{"argv": ["/usr/local/spark/bin/pyspark",
 "-m", "ipykernel", "-f", "{connection_file}", "--profile", "pyspark"],
 "display_name":"PySpark",  "language":"python" }