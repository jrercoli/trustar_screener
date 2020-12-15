import build_input_json_list
import mitre_git_browse

def build_request_json(input_data, required_data):
    json_required = {}

    # first, build input list from input_data
    l_out = build_input_json_list.browse_input_json(input_data)
    
    # second, iterating by input list (search required data)
    for required in required_data:
        for l in l_out:             
            # check if l[0] have brackets[], then is a list
            pos = l[0].find('[')
            if (pos >= 0):
                new_l = l[0][:pos]
                if required == new_l:
                    json_required[required] = l[1]
                    break
            if required == l[0]:
                json_required[required] = l[1]
                break
    return json_required

def main():
    # Example input data
    i_data={ 
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
    
    # Example request data
    r_data = ["guid", "content.entities", "content.link.href", "score", "score.sign", "kill_chain_phases[1].phase_name"]

    # Mitre required json data
    mitre_data = ["id", "objects[0].name", "objects[0].kill_chain_phases"] 

    # Request final json object
    final_json = build_request_json(i_data, r_data)
    # final_json = build_request_json(mitre_git_browse.get_mitre_json(), mitre_data)
    print(final_json)

if __name__ == "__main__":
    main()
    
