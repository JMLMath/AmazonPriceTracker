import http.server
from data import getLastData
from main import VERSION

PORT = 4321 ##listening port

def generateHTMLDashboard():
    """Generate the HTML page to show as dashboard.
    Args:
        No arguments
    Returns:
        str : the genereted HTML page
        """
    lastData = getLastData("data.csv")
    HtmlDashboardFile = open("dashboardHeader.html", "r")
    HTMLPage = HtmlDashboardFile.read()
    HTMLPage = HTMLPage + "<h1>Amazon Price Tracker Dashboard</h1>"

    for i in range(len(lastData[0])):
        HTMLPage = HTMLPage + "<a href='" + str(lastData[0][i]) + "'>" + lastData[1][i] + "</a> <p> Prix actuelle :" + str(lastData[2][i]) + "</p>"

    HTMLPage = HTMLPage + "<p>created by JML Math</p>" \
                          "<p>v."+ str(VERSION[0]) + "." + str(VERSION[1]) + "." + str(VERSION[2]) + "</p> </body>"

    return HTMLPage

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(bytes(generateHTMLDashboard(), "utf-8"))
        return


def startServer():
    """Start the HTTP server on the port specified by PORT value (which is 4321 by default)"""
    httpd = http.server.HTTPServer(("", PORT), Handler)
    print(f"server succesfully started at port {PORT}")
    httpd.serve_forever()