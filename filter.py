from snowflake.snowpark.functions import col

def filter_by_role(session, table_name, id):
  df = session.table(table_name)
  return df.filter(col("ID") == role)
