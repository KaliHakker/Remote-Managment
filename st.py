from http.server import HTTPServer, BaseHTTPRequestHandler
import http.server
import os
from urllib.parse import quote, unquote
class Serv(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            print(self.authedforadmin)
        except:
            self.authedforadmin = False
        if self.path == '/':
            self.path = '/index.html'
            try:
                os.remove("/home/voldemort/GitHub/Login-Pages/login-form-08/login-form-08/output.txt")
            except FileNotFoundError:
                pass
        if self.path == "/admin":
            try:
                os.remove("/home/voldemort/GitHub/Login-Pages/login-form-08/login-form-08/output.txt")
            except FileNotFoundError:
                pass
        if self.path == "/st.py":
            self.path = "/index.html"
        if (self.path == "/admin.html") and not self.authedforadmin:
            self.path = "/index.html"
        if (self.path == "/index.html") and self.authedforadmin:
            self.path == "/admin.html"
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except FileNotFoundError:
            file_to_open = 'File not found'
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, "utf-8"))
    def do_POST(self):
        try:
            print(self.authedforadmin)
        except:
            self.authedforadmin = False
        print ("MY SERVER: I got a POST request.")
        if self.path == '/admin.html':
            print ("MY SERVER: The POST request is for the /admin URL.")

            content_length = int(self.headers['Content-Length'])
            post_data_bytes = self.rfile.read(content_length)
            print ("MY SERVER: The post data I received from the request has following data:\n", post_data_bytes)

            post_data_str = post_data_bytes.decode("UTF-8")
            print(post_data_str)
            list_of_post_data = post_data_str.split('&')
            print(list_of_post_data)
            post_data_dict = {}
            for item in list_of_post_data:
                variable, value = item.split('=')
                post_data_dict[variable] = value

            print ("MY SERVER: I have changed the post data to a dict and here it is:\n", post_data_dict)
            try:
                name = post_data_dict['name']
                password = post_data_dict["password"]
            except KeyError:
                print("MY SERVER: Client has modified source code.")
                return self.do_GET()
            if (name == "admin") and (password == "IssiOnProgemisesHalb"):
                self.path = '/admin.html'
                print("ADMINADMIN")
                self.authedforadmin = True
            else:
                self.path = '/try_again_index.html'
                print("EBAADMIN")
        if self.path == "/output.txt":
            print ("MY SERVER: The POST request is for the /cmd URL.")

            content_length = int(self.headers['Content-Length'])
            post_data_bytes = self.rfile.read(content_length)
            print ("MY SERVER: The post data I received from the request has following data:\n", post_data_bytes)

            post_data_str = post_data_bytes.decode("UTF-8")
            print(post_data_str)
            list_of_post_data = post_data_str.split('&')
            print(list_of_post_data)
            post_data_dict = {}
            for item in list_of_post_data:
                variable, value = item.split('=')
                post_data_dict[variable] = value
            os.system(unquote(post_data_dict["cmd"]).replace("+", " ") + ">> /home/voldemort/GitHub/Login-Pages/login-form-08/login-form-08/output.txt")
            print("Executed command " + post_data_dict["cmd"] + " > output.txt")
            self.path = "/output.txt"
        if self.path == "/logout" and self.authedforadmin:
            self.authed = False
            self.path = "/index.html"
        return self.do_GET()



httpd = HTTPServer(('localhost', 8081), Serv)
httpd.serve_forever()
