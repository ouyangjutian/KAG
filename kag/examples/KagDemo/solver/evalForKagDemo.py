import logging
import os

from kag.common.env import init_kag_config
from kag.solver.logic.solver_pipeline import SolverPipeline

logger = logging.getLogger(__name__)

class KagDemo:

    def __init__(self):
        pass

    def qa(self, query):
        resp = SolverPipeline()
        answer, trace_log = resp.run(query)
        return answer,trace_log

if __name__ == "__main__":
    demo = KagDemo()
    query = "知识图谱是什么？"
    answer,trace_log = demo.qa(query)
    print(f"Question: {query}")
    print(f"Answer: {answer}")
    print(f"TraceLog: {trace_log}")