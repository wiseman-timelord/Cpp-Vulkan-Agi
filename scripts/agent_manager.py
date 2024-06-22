# .\scripts\agent_manager.py

from qwen_agent.agents import Assistant, BasicDocQA
from qwen_agent.tools.base import BaseTool, register_tool
from qwen_agent.utils.utils import print_traceback
from jupyter_client import BlockingKernelClient
import subprocess
import time
import uuid
import os
import json5
from typing import Dict, List, Optional, Tuple, Union

def create_agent(agent_type, llm_cfg, system_instruction, tools, files=None):
    if agent_type == 'Manager':
        return Assistant(llm=llm_cfg, system_message=system_instruction, function_list=tools, files=files)
    elif agent_type == 'Coder':
        return Assistant(llm=llm_cfg, system_message=system_instruction, function_list=tools)
    elif agent_type == 'Websearch':
        return Assistant(llm=llm_cfg, system_message=system_instruction, function_list=tools)
    elif agent_type == 'Consolidator':
        return BasicDocQA(llm=llm_cfg, system_message=system_instruction, function_list=tools, files=files)
    elif agent_type == 'Creative':
        return Assistant(llm=llm_cfg, system_message=system_instruction, function_list=tools)
    elif agent_type == 'Analyst':
        return Assistant(llm=llm_cfg, system_message=system_instruction, function_list=tools)
    else:
        raise ValueError(f"Unknown agent type: {agent_type}")

def register_tools():
    # Registering the CodeExecutor tool
    @register_tool('code_executor')
    class CodeExecutor(BaseTool):
        description = 'Execute code and return the output.'
        parameters = [{
            'name': 'code',
            'type': 'string',
            'description': 'Code to execute',
            'required': True
        }]

        def call(self, params: str, **kwargs) -> str:
            try:
                params_json = self._verify_json_format_args(params)
                code = params_json['code']
                exec_globals = {}
                exec(code, exec_globals)
                return str(exec_globals)
            except Exception as e:
                print_traceback()
                return str(e)

    # Registering the CodeInterpreter tool
    @register_tool('code_interpreter')
    class CodeInterpreter(BaseTool):
        description = 'Execute Python code and return the output.'
        parameters = [{'name': 'code', 'type': 'string', 'description': 'Python code to execute', 'required': True}]

        def __init__(self, cfg: Optional[Dict] = None):
            super().__init__(cfg)
            self.work_dir = os.path.join(os.getcwd(), 'code_interpreter_workspace')
            os.makedirs(this.work_dir, exist_ok=True)
            self.instance_id = str(uuid.uuid4())

        def _start_kernel(self, kernel_id: str) -> Tuple[BlockingKernelClient, subprocess.Popen]:
            connection_file = os.path.join(self.work_dir, f'kernel_{kernel_id}.json')
            kernel_process = subprocess.Popen(
                [sys.executable, '-m', 'ipykernel_launcher', '--IPKernelApp.connection_file', connection_file],
                cwd=self.work_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            
            # Wait for the connection file to be written
            while not os.path.isfile(connection_file):
                time.sleep(0.1)
            
            with open(connection_file, 'r') as fp:
                json.load(fp)  # Ensuring the JSON file is fully written

            # Setup the kernel client
            kc = BlockingKernelClient(connection_file=connection_file)
            kc.load_connection_file()
            kc.start_channels()
            kc.wait_for_ready()
            return kc, kernel_process

        def _execute_code(self, kc: BlockingKernelClient, code: str) -> str:
            kc.execute(code)
            output = ''
            while True:
                msg = kc.get_iopub_msg()
                if msg['msg_type'] == 'stream':
                    output += msg['content']['text']
                if msg['msg_type'] == 'execute_result':
                    output += msg['content']['data']['text/plain']
                if msg['msg_type'] == 'status' and msg['content']['execution_state'] == 'idle':
                    break
            return output

        def call(self, params: Union[str, dict], files: List[str] = None, timeout: Optional[int] = 30, **kwargs) -> str:
            try:
                params = json5.loads(params)
                code = params['code']
            except Exception:
                code = extract_code(params)

            if not code.strip():
                return ''
            
            kernel_id = f'{self.instance_id}_{os.getpid()}'
            kc, kernel_process = self._start_kernel(kernel_id)
            
            try:
                result = self._execute_code(kc, code)
            finally:
                kc.stop_channels()
                kernel_process.terminate()
            
            return result if result.strip() else 'Finished execution.'

def setup_agents(model_name, device):
    register_tools()
    
    agent_configs = {
        'Manager': {
            'temperature': 0.5, 'top_p': 0.85, 'repeat_penalty': 1.2, 'top_k': 50
        },
        'Coder': {
            'temperature': 0.3, 'top_p': 0.7, 'repeat_penalty': 1.1, 'top_k': 20
        },
        'Websearch': {
            'temperature': 0.7, 'top_p': 0.9, 'repeat_penalty': 1.1, 'top_k': 50
        },
        'Consolidator': {
            'temperature': 0.5, 'top_p': 0.85, 'repeat_penalty': 1.3, 'top_k': 50
        },
        'Creative': {
            'temperature': 0.9, 'top_p': 0.95, 'repeat_penalty': 1.0, 'top_k': 100
        },
        'Analyst': {
            'temperature': 0.6, 'top_p': 0.9, 'repeat_penalty': 1.2, 'top_k': 50
        }
    }

    base_llm_cfg = {
        'model': model_name,
        'model_server': 'http://localhost:8000/v1',  # Ensure this is the correct server address
        'api_key': ''
    }

    system_instructions = {
        'Manager': 'You are a manager, overseeing and coordinating other agents to achieve goals.',
        'Coder': 'You generate and refine code based on user requirements.',
        'Websearch': 'You conduct web searches and gather relevant information.',
        'Consolidator': 'You process large texts and generate concise summaries.',
        'Creative': 'You generate creative text, such as stories and poems.',
        'Analyst': 'You analyze input, brainstorm ideas, and plan projects.'
    }

    common_tools = ['code_executor', 'code_interpreter']
    file_paths = ['./examples/resource/doc.pdf']

    agents = {}
    for agent_type, cfg in agent_configs.items():
        llm_cfg = base_llm_cfg.copy()
        llm_cfg['generate_cfg'] = cfg
        agents[agent_type] = create_agent(agent_type, llm_cfg, system_instructions[agent_type], common_tools, file_paths)
    
    return agents
