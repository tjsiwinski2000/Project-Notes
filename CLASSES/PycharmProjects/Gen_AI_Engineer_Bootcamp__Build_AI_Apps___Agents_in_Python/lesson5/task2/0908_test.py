from langgraph.checkpoint.sqlite import SqliteSaver
import os

print("CWD:", os.getcwd())

with SqliteSaver.from_conn_string('checkpoints2.db') as checkpointer:
    print("Checkpointer created")
    print("File exists right after connect?", os.path.exists('checkpoints2.db'))