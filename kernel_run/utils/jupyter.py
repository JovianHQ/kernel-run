import os
import json


class JupyterError(Exception):
    """Error in parsing Jupyter notebook"""
    pass


def _truncate(text, limit=200):
    """Truncate text to given number of characters"""
    if len(text) > limit + 40:
        return text[:limit] + "... (truncated)"
    return text


def strip_outputs(nbtext):
    """Parse text as a Jupyter notebook and remove outputs"""
    try:
        nbjson = json.loads(nbtext)
    except:
        raise JupyterError(
            'Failed to parse Jupyter notebook:\n' + _truncate(nbtext))
    if 'cells' in nbjson:
        for cell in nbjson['cells']:
            if 'outputs' in cell and cell['cell_type'] == 'code':
                cell['outputs'] = []
    return json.dumps(nbjson)


def _notfound_msg(path):
    return """ERROR: No such file or directory: '""" + path + "'"


def _invalid_msg(fname):
    return """ERROR: Invalid file '""" + fname + """'. Please provide a Jupyter notebook with '.ipynb' extension."""


def read_nbfile(path):
    # Check if file exists
    if not os.path.exists(path):
        raise JupyterError(_notfound_msg(path))

    # Verify file extension
    fname = os.path.basename(path)
    if not fname.endswith(".ipynb"):
        raise JupyterError(_invalid_msg(fname))

    # Read & strip outputs
    with open(path) as f:
        return fname, strip_outputs(f.read())
