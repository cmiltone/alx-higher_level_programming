#!/bin/bash
# sends get request with header X-School-User-Id set to 98
curl -H "X-School-User-Id: 98" -s "$1"
