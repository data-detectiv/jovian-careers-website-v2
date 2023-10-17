from sqlalchemy import create_engine,text
import os
db_connection = os.environ['DB_CONNECTION_STR']
engine = create_engine(db_connection,connect_args={
      "ssl": {
        "ssl_ca": "/etc/ssl/cert.pem"
      }
  })

def job_listing():
  with engine.connect() as conn:
    result=conn.execute(text("SELECT * FROM jobs"))
    job_list = []
    for row in result.all():
        job_list.append(row)
  return job_list







