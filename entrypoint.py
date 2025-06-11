#!/usr/bin/env python
import os
from mcp_polygon import server

# Ensure the server process doesn't exit immediately when run as an MCP server
def start_server():
    polygon_api_key = os.environ.get("POLYGON_API_KEY", "")
    if not polygon_api_key:
        print("Warning: POLYGON_API_KEY environment variable not set.")
    else:
        print("Starting Polygon MCP server with API key configured.")

    mcp_transport = os.environ.get("MCP_TRANSPORT") or "stdio"

    server.run(mcp_transport)

if __name__ == "__main__":
    start_server()
