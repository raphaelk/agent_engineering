"""WidgetWare SDR Context Builder Module."""

import os
import copy
import yaml
from widgetware_sdr.instructions import get_system_instructions

def _load_yaml(filename: str) -> dict:
    # Try config/ relative to current working directory first, then relative to the file.
    cwd_path = os.path.join(os.getcwd(), "config", filename)
    file_dir = os.path.dirname(os.path.abspath(__file__))
    relative_path = os.path.abspath(os.path.join(file_dir, "..", "..", "config", filename))
    
    paths_to_try = [cwd_path, relative_path]
    for path in paths_to_try:
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    data = yaml.safe_load(f)
                    if data is None:
                        raise ValueError(f"Configuration file {filename} is empty")
                    return data
            except Exception as e:
                raise ValueError(f"Failed to load configuration file {filename} at {path}: {e}")
                
    raise FileNotFoundError(f"Configuration file {filename} not found in search paths: {paths_to_try}")

def build_context(
    account: dict,
    objective: str,
    evidence: list[dict],
    state: dict | None = None,
) -> dict:
    """Build the structured WidgetWare SDR context package."""
    try:
        products = _load_yaml("products.yaml")
        icp = _load_yaml("icp.yaml")
        policies = _load_yaml("policies.yaml")
    except (FileNotFoundError, ValueError) as e:
        raise ValueError(f"Missing or invalid required configuration: {e}") from e

    system_instructions = get_system_instructions()
    
    business_context = {
        "products": products,
        "icp": icp,
        "policies": policies,
    }
    
    task_context = {
        "account": copy.deepcopy(account),
        "objective": objective,
    }
    
    retrieved_evidence = copy.deepcopy(evidence)
    
    if state is None:
        workflow_state = {}
    else:
        workflow_state = copy.deepcopy(state)
        
    return {
        "system_instructions": system_instructions,
        "business_context": business_context,
        "task_context": task_context,
        "retrieved_evidence": retrieved_evidence,
        "state": workflow_state,
    }
