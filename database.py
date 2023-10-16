from sqlalchemy import create_engine,text

db_connection = "mysql+pymysql://n2q6e9hy0fmdn07svd4v:pscale_pw_jIGwVnEsliI1tX3Fis2E4JvlDoL4aCm8zHBNJktfJfw@aws.connect.psdb.cloud/careers?charset=utf8mb4"
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







