global l_out
l_out=[]

def __checkList(ele, prefix):
    # first add whole list
    __addField(ele, prefix)
    # second, check structure of a list and add elements
    for i in range(len(ele)):
        if (isinstance(ele[i], dict)):            
            __checkDict(ele[i], prefix)

        if (isinstance(ele[i], list)):
            __checkList(ele[i], prefix+"["+str(i)+"]")

        elif (isinstance(ele[i], str)) or (isinstance(ele[i], int)):
            __addField(ele[i], prefix+"["+str(i)+"]")        
        else:
            __checkDict(ele[i], prefix+"["+str(i)+"]")

def __checkDict(jsonObject, prefix):
    for ele in jsonObject:
        if (isinstance(jsonObject[ele], dict)):
            __checkDict(jsonObject[ele], prefix+"."+ele)

        elif (isinstance(jsonObject[ele], list)):
            __checkList(jsonObject[ele], prefix+"."+ele)

        elif (isinstance(jsonObject[ele], str)) or (isinstance(ele[i], int)):
            __addField(jsonObject[ele],  prefix+"."+ele)

def __addField(ele, prefix):  
    l_out.append((prefix, ele))

def browse_input_json(data):    
    #Iterating all the fields of the JSON  
    for element in data:
        #If Json Field value is a Nested Json
        if (isinstance(data[element], dict)):
            __checkDict(data[element], element)

        #If Json Field value is a list
        elif (isinstance(data[element], list)):      
            __checkList(data[element], element)

        #If Json Field value is a string or int
        elif (isinstance(data[element], str)) or (isinstance(data[element], int)):
            __addField(data[element], element)
    
    return l_out
