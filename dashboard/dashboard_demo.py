"""
IMAC3 AI Product Dashboard

Public Showcase Interface
"""

from fastapi.responses import HTMLResponse


def dashboard_page():

    html = """
    <!DOCTYPE html>
    <html>

    <head>

    <title>IMAC3 AI Dashboard</title>

    <style>

    body {
        font-family: Arial, sans-serif;
        background: #0f172a;
        color: white;
        padding: 40px;
    }

    h1 {
        font-size: 36px;
    }

    .container {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
    }

    .card {

        background: #1e293b;
        border-radius: 15px;
        padding: 25px;
        width: 250px;

    }

    .online {

        color: #22c55e;
        font-size: 22px;

    }

    </style>

    </head>


    <body>


    <h1>🚀 IMAC3 AI Dashboard</h1>

    <p>
    Intelligent Agent & AI Systems Platform
    </p>


    <div class="container">


        <div class="card">

            <h3>System</h3>

            <p class="online">
            ONLINE
            </p>

        </div>



        <div class="card">

            <h3>AI Agents</h3>

            <p>
            Active Intelligence Modules
            </p>

        </div>



        <div class="card">

            <h3>Automation</h3>

            <p>
            Workflow Engine Ready
            </p>

        </div>



        <div class="card">

            <h3>Decision Engine</h3>

            <p>
            Intelligence Layer Active
            </p>

        </div>


    </div>


    </body>

    </html>
    """

    return HTMLResponse(content=html)
