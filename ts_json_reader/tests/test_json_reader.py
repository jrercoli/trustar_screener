import pytest
from ts_json_reader import json_request

@pytest.fixture
def example_input_data():
    d={ 
        "guid": "1234", 
        "content":
            {
            "type": "text/html", 
            "title": "Challenge 1", 
            "entities": [ "1.2.3.4", "wannacry", "malware.com"],
            "link":
                {"href": "www.jr.com"
                },
            },
        "kill_chain_phases": [
                    {
                        "kill_chain_name": "mitre-attack",
                        "phase_name": "defense-evasion"
                    },
                    {
                        "kill_chain_name": "mitre-attack",
                        "phase_name": "privilege-escalation"
                    },
                ], 
        "score": 74, 
        "time": 1574879179 }
    return d

@pytest.fixture
def example_request_data():
    d = ["guid", "content.entities", "content.link.href", "score", "score.sign", "kill_chain_phases[1].phase_name"]
    return d

def test_required_output_json(example_input_data, example_request_data):
    assert build_request_json(example_input_data, example_request_data) == {'guid': '1234', 'content.entities': ['1.2.3.4', 'wannacry', 'malware.com'], 'content.link.href': 'www.jr.com', 'score': 74, 'kill_chain_phases[1].phase_name': 'privilege-escalation' }
