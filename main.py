from subprocess import Popen, PIPE
import requests

def execute_return(cmd):
    args = cmd.split()
    # print("a", args)
    pr = Popen(args, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    out, err = pr.communicate()
    return out, err



# a,b = execute_return("python test.py")
# print(a)
# print(b)
def make_request(error):
    resp = requests.get("https://api.stackexchange.com/"+"/2.3/search?order=desc&sort=activity&tagged=python&intitle={}&site=stackoverflow".format(error))
    return resp.json()

def get_urls(json_dict):
    url_list = []
    count = 0
    for i in json_dict["items"]:
        if i["is_answered"]:
            url_list.append(i["link"])
        count += 1
        if count == 10:
            break
    import webbrowser
    for i in url_list:
        webbrowser.open(i)


if __name__ == "__main__":
    output, error = execute_return("python test.py")
    error_message = error.strip().split("\n")[-1]
    print(error_message)
    if error_message:
        error_filter = error_message.split(":")
        json1 = make_request(error_filter[0])
        json2 = make_request(error_filter[1])
        json = make_request(error_message)
        # print(json)
        get_urls(json1)
        get_urls(json2)
        get_urls(json)
    else:
        print("no error")
