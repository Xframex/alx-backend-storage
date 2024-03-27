#!/usr/bin/env python3
'''Task 12
'''
from pymongo import MongoClient

client = MongoClient()
db = client.logs
collection = db.nginx

total_logs = collection.count_documents({})

http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {
    method: collection.count_documents({"method": method})
    for method in http_methods
}

status_check_count = collection.count_documents({"method": "GET", "path": "/status"})

print(f"{total_logs} logs")
print("Methods:")
for method, count in method_counts.items():
    print(f"    method {method}: {count}")
print(f"{status_check_count} status check")
