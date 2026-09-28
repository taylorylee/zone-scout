#!/usr/bin/env python3
"""Run Zone Scout locally with website scanning: python3 server.py, then open http://localhost:8765"""
import os
import sys
import importlib.util
from http.server import ThreadingHTTPServer

ROOT = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("zs_api", os.path.join(ROOT, "api", "index.py"))
api = importlib.util.module_from_spec(spec)
spec.loader.exec_module(api)
PORT = int(os.environ.get("PORT", "8765"))


class Local(api.handler):
    def log_message(self, fmt, *args):
        sys.stderr.write("  " + (fmt % args) + "\n")


if __name__ == "__main__":
    print(f"\n  Zone Scout running at http://localhost:{PORT}  (Ctrl+C to stop)\n")
    ThreadingHTTPServer(("127.0.0.1", PORT), Local).serve_forever()
