services:
  - type: web
    name: neurolink
    env: python
    buildCommand: ""
    startCommand: uvicorn main:app --host 0.0.0.0 --port 10000
    plan: free
